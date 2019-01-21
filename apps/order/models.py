from django.db import models

from apps.account.models import User
from apps.index.models import Shop


class ShopCar(models.Model):
    car_id = models.AutoField(primary_key=True, auto_created=True)
    shop_number = models.IntegerField()
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_car'


class Order(models.Model):
    oid = models.AutoField(primary_key=True, auto_created=True)
    order_code = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    receiver = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    message = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.CharField(max_length=64)
    confirm_time = models.CharField(max_length=64)
    # 订单状态：-1代表删除，0代表取消，1代表支付，2代表未支付，3代表完成
    status = models.IntegerField(default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', db_index=True)
    car_id = models.OneToOneField(ShopCar, on_delete=models.CASCADE, db_column='car_id', db_index=True)

    class Meta:
        db_table = 'order'
