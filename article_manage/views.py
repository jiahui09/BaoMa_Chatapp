from itertools import takewhile
from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
#导入数据库模板
from models import article


# Create your views here.



#接收文章数据，文章数据格式分为题头与内容
def add_article(request):
    if request.method == "POST":
        req = json.loads(request.body)
        key_flage = req.get("title") and req.get("content") and len(req)==2
        
    if key_flage:
        title = req["title"]
        content = req["content"]
        
        add_art = article(title=title,content=content,status="alive")
        add_art.save()
    
        return JsonResponse({"status":"BS.200","msg":"publish article sucess."})
    else:
        return JsonResponse({"status":"BS.400","message":"publish article failed!!!"})


#接收文章数据，文章数据格式分为题头与内容
def add_article(request):
    if request.method == "POST":
        req = json.loads(request.body)
        key_flage = req.get("content") and len(req)==2
        
    if key_flage:
        title = req["title"]
        content = req["content"]
        
        add_comm = article(title=title,content=content,status="alive")
        add_comm.save()


#接收用户请求，返回文章数据
def load_article(request):
    if request.method == "GET":
        req = article.objects.order_by('?')[:10]
        articles=[]
    for article in req:
        articles.append(article)
        
    return JsonResponse(articles,safe=False)

#返回用户创作的文章
def my_article(request):
    articles=[]
    if request.method == "GET":
        req = article.objects.order_by(user_id=request.user.id)
    for acticle in req:
        articles.append(article)
    return JsonResponse(articles,safe=False)