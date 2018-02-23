from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404

# Create your views here.


# def home(request):
#     return HttpResponse('Hello World, Django')

# def detail(request, my_args):
#     return HttpResponse("you're looking at my_args %s." % my_args)


# def detail(request, my_args):
#     post = Article.objects.add()[int[my_args]]
#     string = ('title=%s, category=%s, date_time=%s, content=%s' % (post.title, post.category,
#                                                                    post.date_time, post.content))
#     return HttpResponse(string)

def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

'''主页'''
def home(request):
    post_list = Article.objects.all()  # 获取全部Article对象
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404

'''分类
'''
def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})


'''
关于
'''
def about_me(request):
    return render(request, 'aboutme.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})
