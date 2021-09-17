# Create your views here.
import requests  # 导入requests库，
import sys  # 导入系统库
import socket
import json
import re
import os
import uuid
import base64
import datetime
import numpy as np
import pandas as pd
from aip import AipOcr
from rest_framework import status


from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache


from doggo.settings import BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY, BAIDU_MAP_KEY
from doggo.settings import MEDIA_ROOT, STATIC_ROOT

sysfile = os.path.abspath('.')

ty = sys.getfilesystemencoding()  # 这个可以获取文件系统的编码形式
timeout = 20

recognition_image_upload_path = '/recognition/images/'
recognition_image_result_path = '/recognition/results/'
relative_recognition_image_upload_path = '/media/recognition/images/'
relative_recognition_image_result_path = '/media/recognition/results/'
full_recognition_image_upload_path = MEDIA_ROOT+recognition_image_upload_path
full_recognition_image_result_path = MEDIA_ROOT+recognition_image_upload_path


class SourcesUpload(APIView):
    def get(self, request):
        try:
            reginfs = {
                "code": 400,
                "message": "success",
                "data": "hello"
            }
        except:
            reginfs = {
                "code": 200,
                "message": "failed",
                "data": "注册失败"
            }
        return Response(reginfs)

    def post(self, request):
        # 上传图片的处理
        try:
            stick_img = request.POST.get("stick_img", False)
            upload_img_uuid = (str(uuid.uuid1())).replace("-", "")
            img_file_name = upload_img_uuid + '.jpg'
            upload_img_path = full_recognition_image_upload_path + img_file_name
            if stick_img:
                img_path = base64.b64decode(stick_img.split(',')[-1])
                with open(upload_img_path, 'wb') as f:
                    f.write(img_path)
                reginfs = {
                    "code": 200,
                    "message": "success",
                    "data": {
                        "id": upload_img_uuid
                    }
                }
            else:
                f = request.FILES["file"]
                with open(upload_img_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                reginfs = {
                    "code": 200,
                    "message": "success",
                    "data": {
                        "id": upload_img_uuid
                    }
                }
        except Exception as e:
            reginfs = {
                "code": 400,
                "message": "failed",
                "data": str(e)
            }
        return Response(reginfs)


class ImageUpload(APIView):
    def get(self, request):
        try:
            reginfs = {
                "code": 200,
                "message": "success",
                "data": "hello"
            }
        except:
            reginfs = {
                "code": 400,
                "message": "failed",
                "data": "注册失败"
            }
        return Response(reginfs)

    def post(self, request):
        # 上传图片的处理
        try:
            stick_img = request.data.get("stick_img", None)
            if stick_img:
                upload_img_uuid = (str(uuid.uuid1())).replace("-", "")
                img_file_name = upload_img_uuid + '.jpg'
                upload_img_path = full_recognition_image_upload_path + img_file_name
                img_path = base64.b64decode(stick_img.split(',')[-1])
                with open(upload_img_path, 'wb') as f:
                    f.write(img_path)
                reginfs = {
                    "code": 200,
                    "message": "success",
                    "data": {
                        "id": upload_img_uuid
                    }
                }
            else:
                reginfs = {
                    "code": 400,
                    "message": "failed",
                    "data": '上传失败!!'
                }
        except Exception as e:
            reginfs = {
                "code": 400,
                "message": "failed",
                "data": str(e)
            }
        return Response(reginfs)


class ImgtoWords(APIView):
    def get(self, request):
        img_uuid = request.query_params.get("id", None)
        if img_uuid == None:
            reginfs = {
                "code": 400,
                "message": "failed",
                "data": "失败"
            }
        else:
            img_file_name = img_uuid + '.jpg'
            relative_img_path = relative_recognition_image_upload_path + img_file_name
            try:
                options = {
                    'detect_direction': 'true',
                    'language_type': 'CHN_ENG',
                }
                img_target_path = full_recognition_image_upload_path + img_file_name
                aipOcr = AipOcr(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
                result = aipOcr.webImage(
                    self.get_file_content(img_target_path), options)
                statusCode = 200
                if result["words_result_num"] == 0:
                    vector_word = "图中没有文字或未能识别"
                else:
                    pic_words = [i["words"] for i in result["words_result"]]
                    pic_word_data = [(i + '<br>') for i in pic_words]
                    vector_word = ''.join(pic_word_data)
            except:
                statusCode = 204
                vector_word = "不支持的该格式的文字识别！"
            imginfo = {}
            imginfo["vector_words"] = vector_word
            imginfo["img_uuid"] = img_uuid
            imginfo["img_path"] = relative_img_path
            reginfs = {
                "code": statusCode,
                "message": "success",
                "data": imginfo
            }
        return Response(reginfs)

    def delete(self, request):
        img_uuid = request.query_params.get("id", None)
        if img_uuid == None:
            reginfs = {
                "code": 400,
                "message": "failed",
                "data": "失败"
            }
        else:
            img_file_name = img_uuid + '.jpg'
            delete_img_path = full_recognition_image_upload_path+img_file_name
            try:
                os.remove(delete_img_path)
                reginfs = {
                    "code": 200,
                    "message": "success",
                    "data": "success"
                }
            except:
                reginfs = {
                    "code": 400,
                    "message": "failed",
                    "data": "失败"
                }
        return Response(reginfs)

    def get_file_content(self, filepath):
        with open(filepath, 'rb') as fp:
            return fp.read()


class ImgtoExcel(APIView):
    def delete(self, request):
        img_uuid = request.query_params.get("id", None)
        if img_uuid == None:
            reginfs = {
                "code": 400,
                "message": "failed",
                "data": "失败"
            }
        else:
            try:
                img_file_name = img_uuid + '.jpg'
                imgpath = full_recognition_image_upload_path + img_file_name
                os.remove(imgpath)
                reginfs = {
                    "code": 444,
                    "message": "success",
                    "data": "hello"
                }
            except:
                reginfs = {
                    "code": 222,
                    "message": "failed",
                    "data": "失败"
                }
        return HttpResponse(json.dumps(reginfs), content_type='application/json')

    def get(self, request):
        # 图片的处理
        # h获取图片的路径

        img_uuid = request.query_params.get("id", None)
        if img_uuid == None:
            reginfs = {
                "code": 400,
                "message": "failed",
                "data": "失败"
            }
        else:
            file_name = img_uuid + '.jpg'
            relative_img_path = relative_recognition_image_upload_path + file_name
            unknownimgpath = full_recognition_image_upload_path + file_name
            options = {
                'detect_direction': 'true',
                'language_type': 'CHN_ENG',
            }
            picUrl = "error"
            message = "识别失败"
            try:
                aipOcr = AipOcr(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
                result = aipOcr.tableRecognitionAsync(
                    self.get_file_content(unknownimgpath), options)
                starttime = datetime.datetime.now()
                # api-1
                # sub_one_sql = "UPDATE 'sources_sourcelimit' SET num_count=num_count-1"
                # sub_one_cursor = connection.cursor()
                # sub_one_cursor.execute(sub_one_sql)
                while True:
                    try:
                        requestId = result["result"][0]["request_id"]
                        aaa = aipOcr.getTableRecognitionResult(
                            requestId, options)
                        picUrl = aaa["result"]
                        percent = picUrl["percent"]
                        if picUrl != '' and percent == 100:
                            message = '识别成功'
                            break
                    except:
                        picUrl = "error"
                        message = "识别失败"
                    endtime = datetime.datetime.now()
                    if (endtime - starttime).seconds > 20:
                        picUrl = "error"
                        message = '识别超时,请重试!'
                        break
                if picUrl == "error":
                    os.remove(unknownimgpath)
                    reginfs = {
                        "code": 400,
                        "message": message,
                        "data": "fail"
                    }
                else:
                    excel_json = {}
                    excel_url = picUrl["result_data"]
                    picUrl["imgPath"] = relative_img_path
                    excel_source = pd.read_excel(excel_url)
                    excel_html = excel_source.to_html(
                        classes='reg-img-excel-table', index=False)
                    excel_json["excel_html"] = excel_html
                    excel_json["img_path"] = relative_img_path
                    excel_json["excel_url"] = excel_url
                    excel_json["origin_data"] = picUrl
                    reginfs = {
                        "code": 200,
                        "message": message,
                        "data": excel_json
                    }
            except:
                picUrl = "error"
                os.remove(unknownimgpath)
                reginfs = {
                    "code": 400,
                    "message": message,
                    "data": "fail"
                }
            return HttpResponse(json.dumps(reginfs), content_type='application/json')

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


def getdata(url):
    try:
        socket.setdefaulttimeout(timeout)
        html = requests.get(url)
        data = html.json()
        if data['results'] != None:
            return data['results']
        return []
        # time.sleep(1)
    except:
        getdata(url)


class POIbyName(APIView):

    def get(self, request):
        name = request.query_params.get("name", None)
        city = request.query_params.get("city", None)
        print(name, city, "====")
        urls = []  # 声明一个数组列表
        for i in range(0, 20):
            page_num = str(i)
            url = 'http://api.map.baidu.com/place/v2/search?query='+name+'&region=' + \
                city+'&page_size=20&page_num=' + \
                str(page_num)+'&output=json&ak='+BAIDU_MAP_KEY
            urls.append(url)
        print('url列表读取完成')

        results = []
        for url in urls:
            res = getdata(url)
            if res != []:
                results += res
        df = pd.DataFrame(results)
        excel_uuid = (str(uuid.uuid1())).replace("-", "")
        excel_file_name = excel_uuid + ".xls"
        relative_excel_path = relative_recognition_image_result_path + excel_file_name
        excel_path = full_recognition_image_result_path + excel_file_name
        # df['coord'] = ["[{},{}]".format(res["location"]["lng"],res["location"]["lat"]) for res in results]
        df.to_excel(excel_path)

        excel_json = {}
        excel_json["excelpath"] = relative_excel_path
        excel_json["id"] = excel_uuid
        excel_json["data"] = results

        reginfs = {
            "code": 200,
            "message": "success",
            "data": excel_json
        }
        return Response(reginfs)

    def post(self, request):
        reginfs = {
            "code": 400,
            "message": "failed",
            "data": str(e)
        }
        return Response(reginfs)


class POIbyRegion(APIView):
    def get(self, request):
        name = request.query_params.get("name", None)
        minLng = request.query_params.get("minLng", None)
        minLat = request.query_params.get("minLat", None)
        maxLng = request.query_params.get("maxLng", None)
        maxLat = request.query_params.get("maxLat", None)

        lng_c = float(maxLng)-float(minLng)
        lat_c = float(maxLat)-float(minLat)

        lng_num = int(lng_c/0.1)+1
        lat_num = int(lat_c/0.1)+1
        # minLng, minLat, maxLng, maxLat
        arr = np.zeros((lat_num+1, lng_num+1, 2))
        for lat in range(0, lat_num+1):
            for lng in range(0, lng_num+1):
                arr[lat][lng] = [float(minLng)+lng*0.1, float(minLat)+lat*0.1]

        urls = []

        bounds = '{},{},{},{}'.format(minLat, minLng, maxLat, maxLng)
        for lat in range(0, lat_num):
            for lng in range(0, lng_num):
                for b in range(0, 20):
                    page_num = str(b)
                    url = 'http://api.map.baidu.com/place/v2/search?query='+name+'&bounds='+bounds + \
                        '&page_size=20&page_num=' + \
                        str(page_num)+'&coord_type=2&output=json&ak='+BAIDU_MAP_KEY
                    urls.append(url)

        results = []
        for url in urls:
            res = getdata(url)
            if res != []:
                results += res
        df = pd.DataFrame(results)
        excel_uuid = (str(uuid.uuid1())).replace("-", "")
        excel_file_name = excel_uuid + ".xls"
        relative_excel_path = relative_recognition_image_result_path + excel_file_name
        excel_path = full_recognition_image_result_path + excel_file_name
        # df['coord'] = ["[{},{}]".format(res["location"]["lng"],res["location"]["lat"]) for res in results]
        df.to_excel(excel_path)

        excel_json = {}
        excel_json["excelpath"] = relative_excel_path
        excel_json["id"] = excel_uuid
        excel_json["data"] = results

        reginfs = {
            "code": 200,
            "message": "success",
            "data": excel_json
        }
        return Response(reginfs)

    def post(self, request):
        reginfs = {
            "code": 400,
            "message": "failed",
            "data": str(e)
        }
        return Response(reginfs)


class Test(APIView):
    def get(self, request):
        reginfs = {
            "code": 400,
            "message": "failed",
            "data": 123456
        }
        return Response(reginfs)


def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


def getdata(name):
    gitpage = requests.get("https://hub.fastgit.org/" + name)
    data = gitpage.text
    datadatereg = re.compile(r'data-date="(.*?)" data-level')
    datacountreg = re.compile(r'data-count="(.*?)" data-date')
    datadate = datadatereg.findall(data)
    datacount = datacountreg.findall(data)
    datacount = list(map(int, datacount))
    contributions = sum(datacount)
    datalist = []
    for index, item in enumerate(datadate):
        itemlist = {"date": item, "count": datacount[index]}
        datalist.append(itemlist)
    datalistsplit = list_split(datalist, 7)
    returndata = {
        "total": contributions,
        "contributions": datalistsplit
    }
    return returndata


class GithubContritutions(APIView):
    def get(self, request, username):
        import datetime
        now_time = datetime.datetime.now()
        date_day_string = now_time.strftime('%Y%m%d')
        cache_key_string = username+'_'+date_day_string
        try:
            is_exist_key = cache.has_key(cache_key_string)
            if is_exist_key:
                return Response(cache.get(cache_key_string), status=status.HTTP_200_OK)
            else:
                github_data = getdata(username)
                cache.set(cache_key_string, github_data, 60*60*24)
                return Response(github_data, status=status.HTTP_200_OK)
        except:
            reginfs = {
                "code": 500,
                "message": "failed",
                "data": "请求失败"
            }
        return Response(reginfs, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
