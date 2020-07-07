from django.db import models
# 导包user表单
from django.contrib.auth.models import User
# Create your models here.

# 用户信息
# 头像和昵称
class Userinfo(models.Model):
    headImg = models.ImageField()
    nickName = models.CharField(max_length=50)
    # 关联用户 关联User 一对一 
    belong = models.OneToOneField(User)
    #查询函数为id
    def __int__(self):
        return self.id

# 文章分类
class Category(models.Model):
    # 递归
    # 分类名称 字符串
    name = models.CharField(max_length=50)
    # 查询分类上级和下级 表示树结构 一对多 父级
    belong = models.ForeignKey(self)
    #查询函数为id
    def __int__(self):
        return self.id



# 文章
# 文章列表
# 文章标题 和 文章封面 文章主题内容(排班样式)多行文本
class Article(models.Model):
    title = models.CharField(max_length=50)
    cover = models.CharField(max_length=50)
    text = models.TextField()
    # 关联用户信息 属于哪个用户 一对多 
    belong = models.ForeignKey(Userinfo)
    #查询函数为id
    def __int__(self):
        return self.id

# 收藏
# 查询哪个用户
# 查询哪个文章
class Favourite(models.Model):
    # 关联用户 每一个收藏关联的哪个用户
    belong_user = models.ForeignKey(Userinfo)
    # 关联文章 每一个收藏关联的哪个文章
    belong_art = models.ForeignKey(Article)
    #查询函数为id
    def __int__(self):
        return self.id

# 点赞
# 同收藏，一般点赞不可查询只能查询一部分数据
# 统计数据，一个文章有多少点赞
class Like(models.Model):
    # 关联文章  每一个赞关联的哪个文章
    belong_art = models.ForeignKey(Article)
    # 计数 用户每次点击 num 自增1
    # num = models.IntegerField()
    # 关联用户 每一个赞关联的哪个用户
    belong_user = models.ForeignKey(Userinfo)
    #查询函数为id
    def __int__(self):
        return self.id

# 打赏
class PayOrder(models.Model):
    # 订单号 字符串
    order = models.CharField(max_length=50)
    # 价格 字符串
    price = models.CharField(max_length=50)
    # 支付状态 布尔值
    status = models.BooleanField()
    #查询函数为id
    def __int__(self):
        return self.id