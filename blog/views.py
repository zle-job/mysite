from django.shortcuts import render, get_object_or_404

from blog.models import Blog, Category


# / 博客首页，显示博文列表
def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    context['categories'] = Category.objects.all()
    return render(request, 'blog/blog_list.html', context)


# /blog/blog_pk 博客详情页，显示博文详细信息
def blog_detail(request, blog_pk):
    context = {}
    # 查询不到数据就返回404页面
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'blog/blog_detail.html', context)


# /blog/category/category_pk 博客分类中的博文
# 注意：函数的参数名需要和url中的参数名相同（url中定义的是blogs__category,函数中需要参数名为blogs_category）
# blogs_category这里指的是分类pk
def blogs_with_category(request, blogs_category):
    context = {}
    print('&&&&&&&&&&&&', blogs_category)
    category = get_object_or_404(Category, pk=blogs_category)
    # 当前分类
    context['category'] = category
    context['blogs'] = Blog.objects.filter(category=category)
    # 所有分类，用于页面展示。
    context['categories'] = Category.objects.all()
    return render(request, 'blog/blogs_with_category.html', context)
