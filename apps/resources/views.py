# Create your views here.
import os
import math
import pandas as pd

from django.views import View
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins,viewsets,filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


from .models import SourcesCore
from .filters import SourcesCoreFilter
from .serializers import SourcesCoreSerializers
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


