from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from apps.user.forms import LoginForm, DynamicLoginForm, DynamicLoginPostForm, RegisterGetForm, RegisterPostForm
from apps.utils.YunPian import send_single_sms
from apps.utils.random_str import generate_random
from myedu.settings import apikey, REDIS_HOST, REDIS_PORT
import redis
from apps.user.models import UserProfile
# Create your views here.
class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        send_sms_form = DynamicLoginForm(request.POST)
        re_dict = {}
        if send_sms_form.is_valid():
            mobile = send_sms_form.cleaned_data['mobile']
            # 随机生成数字验证码
            code = generate_random(4, 0)
            re_json = send_single_sms(apikey, mobile, code)
            if re_json['code'] == 0:
                re_dict['status'] = 'success'
                r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, charset="utf8", decode_responses=True)
                r.set(str(mobile), code)
                r.expire(str(mobile), 60*5) # 设置验证码5分钟过期
            else:
                re_dict['msg'] = re_json['msg']
        else:
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]
        return JsonResponse(re_dict)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class RegisterView(View):
    def get(self,request, *args, **kwargs):
        register_get_form = RegisterGetForm()
        return render(request, 'register.html', {'register_get_form': register_get_form})

    def post(self, request, *args, **kwargs):
        register_post_form = RegisterPostForm(request.POST)
        dynamic_login = True
        if register_post_form.is_valid():
            mobile = register_post_form.cleaned_data['mobile']
            password = register_post_form.cleaned_data['password']
            # 新建用户
            user = UserProfile(username=mobile)
            user.set_password(password)
            user.mobile = mobile
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            register_get_form = RegisterGetForm()
            return render(request, 'register.html', {
                'register_get_form': register_get_form,
                'register_post_form': register_post_form
            })




class LoginView(View):
    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticate:
        #     return HttpResponseRedirect(reverse("index"))
        login_form = DynamicLoginForm()
        return render(request, 'login.html', {'login_form': login_form})
    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
        # user_name = request.POST.get('username')
        # pass_word = request.POST.get('password')
        # 前端是不靠谱的，所以后端也许要进行验证
        # 这种验证太过于繁杂，所以我们通常使用django自身验证
        # if user_name is '':
        #     return render(request, 'login.html', {'msg': '用户名不能为空'})
        #
        # if pass_word is '':
        #     return render(request, 'login.html', {'msg': '密码不能为空'})
        #
        # if len(pass_word) <8:
        #     return render(request, 'login.html', {'msg': '密码格式有误'})
            # login_form 特殊方法取出传入值

            user_name = login_form.cleaned_data["username"]
            pass_word = login_form.cleaned_data["password"]
        # 通过Django内置方法查询用户名和密码是否存在，如果直接使用user的models还需要考虑密码加密问题
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # 自动设置cookie 以及Session
                login(request, user)
                # 使用render虽然页面一致，但是URL会存在问题
                # return render(request, 'index.html')
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class DynamicLoginView(View):
    def post(self, request, *args, **kwargs):
        login_form = DynamicLoginPostForm(request.POST)
        dynamic_login = True
        if login_form.is_valid():
            mobile = login_form.cleaned_data['mobile']
            existed_user = UserProfile.objects.filter(mobile=mobile)
            if existed_user:
                user = existed_user[0]
            else:
                # 新建用户
                user = UserProfile(username=mobile)
                password = generate_random(10, 2)
                user.set_password(password)
                user.mobile = mobile
                user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

        else:
            d_form = DynamicLoginForm()
            return render(request, 'login.html', {'login_form': login_form,
                                                  'd_form': d_form,
                                                  'dynamic_login': dynamic_login})
