# Django-web
html+css+js+vuejs+django 基于B站UP主九弓子从零开始
https://space.bilibili.com/22690066

* 前端：html css js 
* 前后端分离：Vuejs
* 后端：Python Django框架

# python 环境

# git 同步仓库
1. 根目录下执行
1. ```git add .``` 
1. ```git commit -am "初始化"``` 
1. ```git remote add origin git@github.com:Smecta/django-web.git```
1. ```git push -u origin master```

# 安装Django框架 后端架设
1. ```pip3 install django``` pip 安装django

1. ```pip3 install django==2.1``` ==是指定版本安装

1. 命令行或者终端运行 python3 
   * ```import django``` 引入django模块
   * ```django.VERSION``` 查看django 版本

2. 开设一个django的(mysite)新项目  ```django-admin startproject mysite``` 
3. ```cd mysite``` 进入mysite 输入```python3 manage.py runserver``` 运行服务

## 新建app
1. ```python3 manage.py startapp myblog```

## 合并（迁移）数据库 同步执行--数据库迁移
1. 首先制作数据库 ```python3 manage.py makemigrations``` 检查数据库是否被改变
1. 然后合并(迁移）数据库 ```python3 manage.py migrate``` 将改变和之前的数据库进行合并

## 设置mysite下的settings.py 项目配置

1. 找到ALLOWED_HOSTS 添加'*'  ``` ALLOWED_HOSTS = ['*'] ```
2. 找到 INSTALLED_APPS,在中括号列表里最后一行添加 新建的app名称,如下：
``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',  #添加
]
```
3. 找到 TEMPLATES ， 在对象里面找到DIRS修改为以下：
``` python
'DIRS': [os.path.join(BASE_DIR,'templates').replace('\\','/')],  # 添加
```
4. 找到 STATIC_URL，在后面添加upload文件夹和路径
``` python
STATIC_URL = '/static/'
MEDIA_URL = '/upload/'  # 添加media文件 upload
MEDIA_ROOT = os.path.join(BASE_DIR,'upload').replace('\\','/')  # 添加 upload 文件路径
```
总结：
   1. 第3点 和 第4点 配置了模板文件 templates 目录和静态文件static 目录
   2. 最后配置了媒体文件目录 upload文件夹
   3. 文件路径
      1. mysite 下 upload 文件夹
      2. website 下 templates文件夹和static文件夹
   
## 配置路由 (mysite下的 url.py)
全站可被访问的路径---（网址）
导包操作和添加静态文件夹目录以及媒体文件夹目录
``` python
# 新增导包部分
from django.conf import settings
from django.conf.urls.static import static

# 列表以后是新增部分
urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \ # 添加
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \ # 添加

```

## Django的MVC模式渲染方式（概念）
M = Model （模型-数据库）
V = View (视图-页面) 
C = Controller (控制器-用户交互的记录)

Django MTV模式 (实际使用)
M = model层 数据库
T = template 模板 页面
V = view 视图层 views.py

松耦合的流程：
> 用户---->浏览器---->通过url.py(被允许的访问)---->通过请求request---->views.py---->访问数据库models.py---->返回数据views.py---->template(可复用html文件)---->制作网页(一次性)---->返回resp到浏览器

操作流程：
1. 在mysite下 urls.py添加一个index路由
   ``` python
   # 导包
   from website import views  #新增
   urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), # 添加index 路由
   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```
2. 在website下views.py 添加一个函数
   ``` python
   from django.shortcuts import render

   # Create your views here.
   # 新增添加函数
   # 写业务逻辑 & 读取数据库
   def index(request):
      return render(request, 'index.html')

   ```
3. 在website下templates下新建html文件 index.html
   
## 配置第一个页面配置路由
1. 修改mysite下 urls.py 
   ``` python
   urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index), #修改内容将index/路径修改为空
   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   ```
2. 修改index.html 文件下的所有本地路径，添加/static/
   如js文件：
   ``` html
   <!-- 注意路径前面添加/static/ -->
   <script src="/static/js/vue.js"></script>
   ```

## 创建数据表
1. 在website下的models.py 写数据表
2. 创建一个标题 title 和一个头像 logo
   ``` python
   from django.db import models

   # Create your models here.
   # 写数据表 写法 表名字：SiteInfo
   class SiteInfo(models.Model):
      # title 定义标题的字段类型 models.CharField 查找九弓子提供的字段文档
      # max_length 最大长度50 null（空值） 和blank（不填写） 建议开启
      title = models.CharField(null=True, blank=True, max_length=50)
     
      # upload_to 后面跟路径添加子文件夹logo/
      logo = models.ImageField(upload_to='logo/',blank=True, null=True)
      # 定义个函数，指本表展现形式，int为整数数字，self自身，return 返回id，也可以返回title,这里目前id
      def __int__(self):
         return self.id

   ```
> 注意：安装vscode的快捷输入插件，插件名称 django 1.0.2 Django Templates and Backend snippets
> mch  = models.CharField
> mig  = models.ImageField 

3. 合并迁移数据库
   1. ```python3 manage.py makemigrations website```
   注意：此处会提示安装pillow
   方法：pip install pillow
   2. ```python3 manage.py migrate website```

4. 将SiteInfo表放到admin管理可视化后台
   1. 在website下的 admin.py
   ``` python
   # 导包载入
   from django.contrib import admin
   from website.models import SiteInfo #新增

   # Register your models here.
   # 将SiteInfo 注册到 admin里
   admin.site.register(SiteInfo) # 新增
   ```

## 创建admin管理员
1. admin 网址
   网址/admin
2. 创建管理员
``` python manage.py createsuperuser ```

   记录: 
      username:admin
      userpasswd:admin12345
   注意：
   密码解密的key在mysite下 settings.py 下的SECRET_KEY 
3. 打开SiteInfo add创建title 和 logo
   
## 升级Django3 项目搬家(python3.8与django2.1兼容问题需升级)

1. 清空数据库文件
   1. 删除项目根目录的 db.sqlite3
   2. 删除website下的 `__pychache__` 和 migrations 两个文件夹
   3. 
2. 卸载django2 安装django3
   ``` pip uninstall django```
   ``` pip install django ```
3. 创建数据库文件并迁移合并数据库
   1. ``` python manage.py migrate ```
   2. ``` python3 manage.py makemigrations website```
   3. ``` python3 manage.py migrate website```
4. 重启服务
   ``` python3 manage.py runserver```
5. 创建管理员账户
   ``` python manage.py createsuperuser ```

## 更改django数据库为mysql
1. 安装mysql
2. 配置数据库在mysite下 settings 下 DATABASES 
   ``` python
   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      },
      'mysql': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'website',
         'USER': 'root',
         'PASSWORD': 'admin123456',
         'HOST': '127.0.0.1',
         'PORT': '3306'
      }
   }
   ```
3. 安装用于驱动django与mysql的连接
   ``` pip install pymysql ```
   配置mysite下 ` __init__.py `文件
   ``` python
   import pymysql
   
   # 替换操作
   pymsql.install_as_MySQLdb

   ```
4. 注释 site-packages/...../bash.py
   line 37  if...raise... 注释即可
5. 在mysql下新建 website 数据库
6. 合并迁移数据库（makemigrations是制作，migrate是写入）
   1. python manage.py migrate --database mysql
7. 将settings内default数据库注释，然后将新写的mysql数据库改名为default
8. 重新创建admin管理员账号

## django数据库连接mongodb
1. 安装mongodb
2. 安装djongo模块
   ` pip install djongo`
3. 修改website下models.py内的 导包
   ``` python
   from djongo import models #修改
   ```
4. 修改mysite下 settings.py 内的 DATABASES
   ``` python
   # 连接本地mongodb
   DATABASES = {
      'default': {
         'ENGINE': 'djongo',
         'ENFORCE_SCHEMA': True,
         'NAME': 'website',
         'CLIENT': {
               'host': '127.0.0.1',
         }
      }
   }
   # 连接异地mongodb
   DATABASES = {
      'default': {
         'ENGINE': 'djongo',
         'ENFORCE_SCHEMA': True,
         'LOGGING': {
               'version': 1,
               'loggers': {
                  'djongo': {
                     'level': 'DEBUG',
                     'propogate': False,                        
                  }
               },
            },
         'NAME': 'your-db-name',
         'CLIENT': {
               'host': 'host-name or ip address',
               'port': port_number,
               'username': 'db-username',
               'password': 'password',
               'authSource': 'db-name',
               'authMechanism': 'SCRAM-SHA-1'
         }
      }
   }
   ```
5. 合并迁移数据库
6. 创建admin管理员账户
   admin admin123456

## 视图层views读取数据到html模板




Django 视图的“上下文对应”
每一个需要携带进网页视图的内容，都需要上下对应


## Django rest framework
1. 安装`pip3 install djangorestframework`
2. 在setting 文件内 installed_apps 加入
```python
   installed_apps = [
      'rest_framework', #新增
      'website'
   ]
```
3. 在website下 新建 app.py
   需要在app.py文件里 导包
   ``` python
   # 装饰器
   from rest_framework.decorators import api_view  
   from rest_framework.response import Response
   from website.models import Classes,Userinfo
   from website.toJson import Classes_data,Userinfo_data


   @api_view(['GET','POST'])

   def api_test(request):
      classes = Classes.objects.all()
      print(classes)
      classes_data = Classes_data(classes, many=True)
      userlist = Userinfo.objects.all()
      userlist_data = Userinfo_data(userlist,many=True)

      data = {
         'classes': classes_data.data,
         'userlist': userlist_data.data
      }
      return Response({'data': data})
   ```
4. 在website下 新建tojson.py
   ``` python
   # 序列化
   from rest_framework import serializers
   from website.models import Classes,Userinfo

   class Classes_data(serializers.ModelSerializer):
      class Meta:
         depth = 1
         model = Classes
         fields = '__all__'

   class Userinfo_data(serializers.ModelSerializer):
      class Meta:
         depth = 1
         model = Userinfo
         fields = '__all__'
   ```
5. 不用序列化和元祖转换，利用python语法进行转换
   ``` python
   # 装饰器
   from rest_framework.decorators import api_view  
   from rest_framework.response import Response
   from website.models import Classes,Userinfo

   @api_view(['GET','POST'])

   def api_test(request):
      classes = Classes.objects.all()
      data = {
         'classes': []
      }
      # classes
      for c in classes:
         data_item = {
            'id': c.id,
            'text': c.text,
            'userlist': []
         }
         # userlist
         userlist = c.userinfo_classes.all()
         for user in userlist:
            user_data = {
                  'id': user.id,
                  'nickName': user.nickName,
                  'headImg': str(user.headImg)
            }
            # 利用append 填入上层for循环 userlist里
            data_item['userlist'].append(user_data)
         # 利用append 填入上层 data里
         data['classes'].append(data_item)
      return Response({'data':data})

   ```
6. 使用ajax vuejs的axios对api获取数据
   ``` js
   new Vue({
      delimiters:['[[',']]'],
      el: "#home",
      data:{
         choosed:1,
         classes:[],
         onOff: false,
      },
      mounted(){
         this.getData()
      },
      methods: {
         getData(){
               axios({
                  url:'/api/',
                  type:'json',
                  method:'get',
               }).then((res)=>{
                  console.log(res.data.classes)
                  this.classes = res.data.classes
               })
         },
         chooseClass(id){
               console.log(id)
               this.choosed = id 
         }
      },
   })

   ```

# cors 安装和配置

1. django-cors-headers

2. 载入 项目 settings.py 内
   1. 添加APPS
``` python 
   INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
   ]

```
   2.  添加中间件：
``` python
   MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
    ...
    'corsheaders.middleware.CorsMiddleware', #新增
    'django.middleware.common.CommonMiddleware',
    ...
   ]

```
   3. 开启配置CorsHeaders
      ``` python
      # 跨域增加忽略
      CORS_ALLOW_CREDENTIALS = True
      CORS_ORIGIN_ALLOW_ALL = True
      CORS_ORIGIN_WHITELIST = [
         "http://expame.org"
      ]
      # 允许跨域请求的方法
      CORS_ALLOW_METHODS = [
         'DELETE',
         'GET',
         'OPTIONS',
         'PATCH',
         'POST',
         'PUT',
         'VIEW',
      ]
      # 允许跨域请求头的
      CORS_ALLOW_HEADERS = [
         'XMLHttpRequest',
         'X_FILENAME',
         'accept',
         'accept-encoding',
         'authorization',
         'content-type',
         'dnt',
         'origin',
         'user-agent',
         'x-csrftoken',
         'x-requested-with',
         'Pragma',
      ]


      ```





# Vue-cli >4.0 
启动vuecli ui
vue ui
安装插件 axios route vuex



# 前端页面架设

> 待更新 VueJS常用的知识（重要）
例如： 
``` js
   v-for=" item in items " :key="xxx.id"
```
``` js
   # 父组件向子组件通信方法
   v-bind
   
   # 子组件
   popros

```


# 实战
## 前台-用户

## 后台-管理员
1. 页面规划
   1. 页面大小，常见尺寸
   2. 后台元素 
      1. 顶部导航栏
      2. 左侧侧边栏
         1. 文章管理
         2. 用户管理
         3. 打赏记录
         4. 栏目管理
         5. 登出
      3. 中间内容区

## 功能设计-数据库
1. 在app-models.py 设计数据库
   1. 博客功能
      1. 用户
      2. 文章
      3. 评论
      4. 收藏
      5. 点赞
      6. 打赏


## 功能设计-api文档
使用国人开发工具apipost
[文章发布api](https://docs.apipost.cn/view/584765e23b4ad52f#2452848)

# 杂项

根目录下创建 firsthtml 

进入firsthtml 下创建 index.html

网页的构成 使用adobe XD设计UI稿
* html
* css样式
* js脚本编程
semantic-ui
semantic-ui.com

css div 分层找出方法

盒模型

绝对定位

index 层级
绝对定位


from rest_framework import serializers
from rest_framework.response import Response   //返回器