from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.user.forms import LoginForm, DynamicLoginForm

# Create your views here.
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))

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
