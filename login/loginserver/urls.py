from django.conf.urls import url

from loginserver import views

app_name = 'loginserver'
urlpatterns = [
    url(r'^index/', views.index,name="主页"),
    url(r'^login/', views.loginin, name="登录"),
    url(r'^logout/', views.loginout, name="登出"),
    url(r'^register/', views.register, name="注册"),
    url(r'^user_center/', views.user_center, name="用户中心"),
    url(r'^edit_profile/', views.edit_profile, name="编辑个人信息"),
    url(r'^change_pwd/', views.change_pwd, name="修改密码"),
]