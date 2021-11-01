import pandas as pd
import json

from django.db import connection
from django.core.cache import cache


from .models import Gallery
from .serializers import GallerySerializers

GALLERY_INFO_CACHE_KEY = 'gallery_info_cache_key'

def genGalleryCache():
    try:
        contexts = Gallery.objects.all().order_by('id')
        serializer = GallerySerializers(contexts, many=True)
        query_sql = "select * from resources_photos"
        all_data = pd.read_sql(query_sql, connection)
        all_photoes = all_data.groupby('gallery_id').apply(
            lambda x: json.loads(x.to_json(orient='records'))).to_json()
        galleries = {"photos": json.loads(
            all_photoes), "galleries": serializer.data}
        cache.set(GALLERY_INFO_CACHE_KEY, galleries,  timeout=None)
        data = {"code": 200, "msg": "success", "data": galleries}
    except:
        data = {"code": 400, "msg": "", "count": 1, "data": 2}
    return data