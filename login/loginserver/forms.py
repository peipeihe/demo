from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json




class ourform(UserCreationForm):
    name = forms.CharField(required=False,max_length=50)
    birthday = forms.DateField(required=False)
    verification = CaptchaField()

    class Meta:
        model = User
        fields = ('username','password1','password2','email','name','birthday')

        #自定义错误信息
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].error_messages = {'unique':'用户名已存在！！！'}


class oureditform(UserChangeForm):
    name = forms.CharField(required=False,max_length=50)
    birthday = forms.DateField(required=False)


    class Meta:
        model = User
        fields = ('username','password','email','name','birthday')

        #自定义错误信息
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].error_messages = {'unique':'用户名已存在！！！'}


class ourloginform(AuthenticationForm):
    verification = CaptchaField()

