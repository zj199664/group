from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=11)

    class Meta:
        db_table = 'user'


class Address(models.Model):
    addr_id = models.AutoField(primary_key=True, auto_created=True)
    detail_addr = models.CharField(max_length=255)
    # 地址表示，1代表默认地址，0代表普通地址
    status = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'address'
