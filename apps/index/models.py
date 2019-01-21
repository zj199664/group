from django.db import models

from apps.account.models import User


class Banner(models.Model):
    nav_id = models.AutoField(primary_key=True, auto_created=True)
    image_url = models.CharField(max_length=255)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'banner'


class Category(models.Model):
    cate_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=64)
    level = models.IntegerField()
    parent_id = models.IntegerField()
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category'


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    promote_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    quantity = models.IntegerField(default=0)
    cate_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='cate_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop'


class ShopProperty(models.Model):
    property_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_property'


class ShopImage(models.Model):
    image_id = models.AutoField(primary_key=True, auto_created=True)
    image_url = models.CharField(max_length=255)
    # 图片类型:small,mid,big
    type = models.CharField(max_length=20)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_image'


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, auto_created=True)
    content = models.CharField(max_length=4000)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='comment'
