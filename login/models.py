from django.db import models

# Create your models here.
# user
# 用户名 密码 邮箱  性别  创建时间

class User(models.Model):

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True) # name必填不超过128字节，并且唯一
    password = models.CharField(max_length=256) # 必填
    email = models.EmailField(unique=True) # 唯一
    sex = models.CharField(max_length=32, choices=gender, default='男') # 默认男
    create_time = models.DateTimeField(auto_now_add=True) # 创建时间
    has_confirmed = models.BooleanField(default=False) #  是否在邮件里激活

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

# User模型新增了has_confirmed字段，这是个布尔值，默认为False，也就是未进行邮件注册；
# ConfirmString模型保存了用户和注册码之间的关系，一对一的形式；
# code字段是哈希后的注册码；
# user是关联的一对一用户；
# c_time是注册的提交时间。
class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"

