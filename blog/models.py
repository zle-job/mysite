from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    '''
    博客分类
    '''
    name = models.CharField(max_length=20, verbose_name='分类')

    def __str__(self):
        return self.name


class Blog(models.Model):
    '''
    博客表
    '''

    # 标题
    title = models.CharField(max_length=30, verbose_name='标题')
    # 作者
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    # 正文
    content = models.TextField()
    # 分类
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类')
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 修改时间
    last_modified_time = models.DateTimeField(auto_now=True)
