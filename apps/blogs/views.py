from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Blog,BlogType
from .serializers import BlogSerializers

# 博客
class BlogListView(APIView):
    """
    blog列表
    """

    def get(self, request):
        try:
            contexts = Blog.objects.all().order_by('-id')
            serializer = BlogSerializers(contexts, many=True)
            context = {"code": 0, "msg": "success", "data": serializer.data}
        except:
            context = {
                "code": 200,
                "message": "failed",
                "data": "失败"
            }
        return Response(context)


class BlogDetailView(APIView):
    """
    blog详情
    """

    def get(self, requset, blog_pk):
        try:
            contexts = Blog.objects.filter(id=blog_pk)
            if contexts.exists():
                serializer = BlogSerializers(contexts, many=True)
                context = {"code": 200, "msg": "success",
                           "data": serializer.data}
            else:
                context = {"code": 200, "msg": "请求数据不存在", "data": []}
        except:
            context = {
                "code": 401,
                "message": "failed",
                "data": "失败"
            }
        return Response(context)


class BlogTypeView(APIView):
    def get(self, requset, blog_type):
        try:
            blog_tp = BlogType.objects.filter(id=blog_type)
            contexts = Blog.objects.filter(blog_type=blog_tp)
            if contexts.exists():
                serializer = BlogSerializers(contexts, many=True)
                context = {"code": 200, "msg": "success",
                           "data": serializer.data}
            else:
                context = {"code": 200, "msg": "请求数据不存在哦0!!!", "data": []}
        except:
            context = {
                "code": 401,
                "message": "failed",
                "data": "失败!!"
            }
        return Response(context)
