from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
from App import models
from App.models import SystemRole


def roles(request):
    roles = SystemRole.objects.all()
    ret = models.SystemRole.objects.all().count()
    data = {
        "roles":roles,
        "ret":ret,
    }
    return render(request,'role_list.html',context=data)


# 删除
def delete_roles(request):
    role_id = request.GET.get('roleId')
    role_obj = models.SystemRole.objects.filter(id=role_id).first()
    models.SystemRole.objects.filter(id=role_id).delete()
    return redirect('/roles_list/')

# 编辑
def edit_roles(request):
    id = request.POST.get('roleId')
    name = request.POST.get('roleName')
    models.SystemRole.objects.filter(id=id).update(role_name=name)
    return redirect('/roles_list/')



# 添加
def add_roles(request):
    if request.method == 'POST':
        name = request.POST.get('roleName')
        role_obj = models.SystemRole.objects.filter(role_name=name).first()
        if not role_obj:
            models.SystemRole.objects.create(role_name=name)
            return HttpResponse('添加成功')
        return HttpResponse('该角色已存在')



def get_roles_by_id(request):
    role_id = request.GET.get('role_id')
    role_obj = models.SystemRole.objects.get(id=role_id)
    role_dict = model_to_dict(role_obj)
    #print(role_dict)
    # for obj in role_id.objects.all():
    #     print(obj.role_name)
    return JsonResponse(role_dict, safe=False)