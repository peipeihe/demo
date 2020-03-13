from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import ourform,oureditform,ourloginform
from .models import average_user
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from captcha.models import CaptchaStore
# Create your views here.


def index(request):
    return render(request,'loginserver/index.html')

#登录
def loginin(request):
    if request.method == 'POST':
        login_form = ourloginform(data=request.POST)
        if login_form.is_valid():
            user = authenticate(request,username=login_form.cleaned_data['username'],password= login_form.cleaned_data['password'])
            login(request,user)
            return redirect('loginserver:主页')
    else:
        login_form=ourloginform()

    content = {'登录表单':login_form,'用户':request.user}
    return render(request,'loginserver/login.html',content)


def loginout(request):
    logout(request)
    return redirect("loginserver:主页")


def register(request):
    if request.method=='POST':
        register_form = ourform(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = authenticate(username=register_form.cleaned_data['username'], password=register_form.cleaned_data['password1'])
            user.email = register_form.cleaned_data['email']
            average_user(user=user,name=register_form.cleaned_data['name'],birthday=register_form.cleaned_data['birthday']).save()
            login(request,user)
            return redirect("loginserver:主页")
    else:
        register_form = ourform()

    content = {'注册表单':register_form}
    return render(request,'loginserver/register.html',content)

#用户中心
@login_required(login_url="loginserver:登录")
def user_center(request):
    content = { '用户': request.user}
    return render(request,'loginserver/user_center.html',content)

#编辑个人信息
@login_required(login_url="loginserver:登录")
def edit_profile(request):
    if request.method=='POST':
        edit_form = oureditform(request.POST,instance=request.user) #想修改哪个用户，创建表单
        if edit_form.is_valid():
            edit_form.save()
            request.user.average_user.name = edit_form.cleaned_data['name']
            request.user.average_user.birthday = edit_form.cleaned_data['birthday']
            request.user.average_user.save()#修改表单要保存
            #average_user(user=user,name=register_form.cleaned_data['name'],birthday=register_form.cleaned_data['birthday']).save()
            return redirect("loginserver:用户中心")
    else:
        edit_form = oureditform(instance=request.user) #预填信息

    content = {'编辑表单':edit_form,'用户':request.user}
    return render(request,'loginserver/edit_profile.html',content)


#修改密码
@login_required(login_url="loginserver:登录")
def change_pwd(request):
    if request.method == 'POST':
        pwd_form = PasswordChangeForm(data=request.POST, user=request.user)  # 想修改哪个用户，创建表单
        if pwd_form.is_valid():
            pwd_form.save()
            return redirect("loginserver:登录")
    else:
        pwd_form = PasswordChangeForm(user=request.user)  # 预填信息

    content = {'改密表单': pwd_form, '用户': request.user}
    return render(request, 'loginserver/change_pwd.html', content)




def ajax_val(request):
    if  request.is_ajax():
        cs = CaptchaStore.objects.filter(response=request.GET['response'], hashkey=request.GET['hashkey'])
        if cs:
            json_data={'status':1}
        else:
            json_data = {'status':0}
        return JsonResponse(json_data)
    else:
        # raise Http404
        json_data = {'status':0}
        return JsonResponse(json_data)
