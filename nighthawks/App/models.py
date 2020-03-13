from django.db import models

# Create your models here.
# class system_object(models.Model):
#     id = models.AutoField(primary_key=True)
#     object_type = models.IntegerField()
#     object_name = models.CharField(max_length=64)
#     operation_code = models.CharField(max_length=32,null=True)
#     description = models.CharField(max_length=100,null=True)
#     belong_to = models.IntegerField(null=True)

class SystemObject(models.Model):
    object_type = models.IntegerField()
    object_name = models.CharField(max_length=64)
    operation_code = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    belong_to = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_object'

class SystemRole(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=64)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:

        db_table = 'system_role'


class SystemRoleRight(models.Model):
    role_id = models.IntegerField()
    sysobjectid = models.IntegerField()
    operation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_role_right'


class SystemUserRole(models.Model):
    role_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'system_user_role'

