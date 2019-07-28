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
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        # 通过Django内置方法查询用户名和密码是否存在，如果直接使用user的models还需要考虑密码加密问题
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            # 自动设置cookie 以及Session
            login(request, user)
            # 使用render虽然页面一致，但是URL会存在问题
            # return render(request, 'index.html')
            return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
