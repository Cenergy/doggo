# Create your views here.
import os
import json
import math
from django.http.response import HttpResponse
import pandas as pd

from django.views import View
from django.db import connection
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from django.core.serializers import serialize


from .models import SourcesCore, Photos, Gallery
from .filters import SourcesCoreFilter
from .serializers import SourcesCoreSerializers, GallerySerializers
from utils.get_sources import get_source, get_source_by_id
from utils.tuling_answer import get_tuling_answer


sysfile = os.path.abspath('.')


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_query_param = "page"


class SourcesCoreViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        资源分类列表数据
    retrieve:
        获取资源分类详情
    """

    queryset = SourcesCore.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = SourcesCoreSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # filter_fields = ('question_type', 'sourcename')
    filter_class = SourcesCoreFilter
    search_fields = ('sourcename',)


class SourcesListView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        page = request.query_params.get("page", 1)
        num = request.query_params.get("num", 10)
        key_word = request.query_params.get("key_word", False)
        objStart = (int(page)-1)*int(num)
        objEnd = int(page)*int(num)

        if key_word:
            query_sql = "SELECT * FROM resources_sourcescore where sourcename like '%{0}%'LIMIT {1},{2} ".format(
                key_word, objStart, objEnd)
            datas = pd.read_sql(query_sql, connection)
            count = len(datas)
        else:
            count_sql = "SELECT * FROM resources_sourcescore "
            datas = pd.read_sql(count_sql, connection)
            count = len(datas)
            # SELECT * FROM resources_sourcescore LIMIT  10 offset 1
            query_sql = "SELECT * FROM resources_sourcescore LIMIT  {1} offset {0}".format(
                objStart, num)
        snippets = SourcesCore.objects.raw(query_sql)
        serializer = SourcesCoreSerializers(snippets, many=True)
        pages = math.ceil(int(count)/int(num))
        data = {"code": 0, "msg": "", "pages": pages,
                "count": count, "data": serializer.data}
        return Response(data)


class SourcesList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        print(request.query_params)
        question_type = request.query_params.get("question_type", -1)
        key_word = request.query_params.get("key_word", False)
        if key_word:
            query_sql = "SELECT * FROM resources_sourcescore where sourcename like '%{0}%'".format(
                key_word)
            datas = pd.read_sql(query_sql, connection)
            count = len(datas)
        else:
            if int(question_type) == -1:
                count_sql = "SELECT * FROM resources_sourcescore"
                datas = pd.read_sql(count_sql, connection)
                count = len(datas)
                query_sql = "SELECT * FROM resources_sourcescore"
            else:
                count_sql = "SELECT * FROM resources_sourcescore where question_type={0}".format(
                    question_type)
                datas = pd.read_sql(count_sql, connection)
                count = len(datas)
                query_sql = "SELECT * FROM resources_sourcescore where question_type={0}".format(
                    question_type)
        snippets = SourcesCore.objects.raw(query_sql)
        serializer = SourcesCoreSerializers(snippets, many=True)
        data = {"code": 0, "msg": "", "count": count, "data": serializer.data}
        return Response(data)


class GithubContritutions(APIView):
    def get(self, request, id):
        try:
            query_sql = "SELECT * FROM resources_imagematch where id={0}".format(
                id)
            data = pd.read_sql(query_sql, connection)

            if len(data):
                img_id = data['img_id'].iloc[0]
                img_type = data['type'].iloc[0]
                img_info = data.iloc[0]
                query_img = "SELECT * FROM resources_imagesource where id={0}".format(
                    img_info.img_id)
                imageData = pd.read_sql(query_img, connection)
                if len(imageData):
                    selectData = imageData.iloc[0]
                    img_path = os.path.join(
                        settings.MEDIA_URL, selectData.pic_webp)
                    if img_info.type == -1:
                        img_path = os.path.join(
                            settings.MEDIA_URL, selectData.pic)
                    if img_info.type == 1:
                        img_path = os.path.join(
                            settings.MEDIA_URL, selectData.pic_thumb)
                    # image_data = open(img_path,"rb").read()
                    return redirect(settings.AIGISSS_HOST+img_path, permanent=True)
        except:
            img_path = os.path.join(
                settings.MEDIA_ROOT, 'images/webp/default.webp')
            # image_data = open(img_path,"rb").read()
            return redirect(settings.AIGISSS_HOST+img_path)


class GalleryInfos(APIView):
    def get(self, request):
        try:
            # origin_data = Photos.objects.all()
            contexts = Gallery.objects.all().order_by('id')
            serializer = GallerySerializers(contexts, many=True)
            query_sql = "select * from resources_photos"
            all_data = pd.read_sql(query_sql, connection)
            # all_photoes = all_data.to_json(orient='records')
            all_photoes = all_data.groupby('gallery_id').apply(lambda x: json.loads(x.to_json(orient='records'))).to_json()
            data = {"code": 200, "msg": "success", "data": {
                "photos": json.loads(all_photoes), "galleries": serializer.data}}
            # serialized_data = serialize('json',origin_data)
        except:
            data = {"code": 400, "msg": "", "count": 1, "data": 2}
        return Response(data)
