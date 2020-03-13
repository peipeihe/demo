app_name = 'App'
from django.conf.urls import url
from App import views
urlpatterns = [
    url(r'^roles_list/', views.roles),
    url(r'^delete_roles/', views.delete_roles),
    url(r'^role/', views.edit_roles),
    url(r'^add_roles/', views.add_roles),
    url(r'^roles/edit/',views.get_roles_by_id),
]
