from django.http import HttpResponse

from django.shortcuts import render

import datetime

def hello(request):
    return HttpResponse('Hello Python')

def runoob(request):
    context = {}
    context['hello'] = 'Python'
    views_name = "whldk"
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    num = 1024
    now = datetime.datetime.now()
    return render(
        request,
        "runoob.html", {
            "name":views_name,
            'content':context,
            'list':views_list,
            'kb':num,
            'now' : now
        })
