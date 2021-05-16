from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SuggestionSerializers
from .models import Suggestion
from utils.email_send import  common_send_email


class SuggestionsView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        try:
            contexts = Suggestion.objects.all().order_by('-id')
            serializer = SuggestionSerializers(contexts, many=True)
            context = {"code": 200, "msg": "success", "data": serializer.data}
        except:
            context = {
                "code": 400,
                "message": "failed",
                "data": "失败"
            }
        return Response(context)

    def post(self, request, format=None):
        try:
            suggest_email = request.data.get("suggest_email", None)
            suggest_user = request.data.get("suggest_user", None)
            suggest_message = request.data.get("suggest_message", None)
            if suggest_email == None or suggest_user == None or suggest_message == None:
                reginfs = {
                    "code": 400,
                    "message": "failed",
                    "data": "邮箱，用户名，反馈信息一个都不能为空"
                }
                return Response(reginfs)
            suggest_data = Suggestion()
            suggest_data.email = suggest_email
            suggest_data.suggest_name = suggest_user
            suggest_data.suggest_content = suggest_message
            suggest_data.save()
            # 发邮件回复用户已收到
            common_send_email("673598118@qq.com",
                              suggest_email, suggest_message)
            reginfs = {
                "code": 202,
                "message": "success",
                "data": "恭喜，成功了"
            }
        except:
            reginfs = {
                "code": 400,
                "message": "failed",
                "data": "失败"
            }
        return Response(reginfs)
