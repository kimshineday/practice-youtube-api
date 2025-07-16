from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
# Video와 관련된 REST API

# 1. VideoList
# api/v1/videos
# [GET]: 전체 비디오 목록 조회
# [POST]: 새로운 비디오 생성
# [PUT], [DELETE] : X
class VideoList(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

# 2. VideoDetail
# api/v1/videos/{video_id}
# [GET]: 특정 비디오 조회
# [POST]: X
# [PUT]: 특정 비디오 업데이트
# [DELETE]: 특정비디오 삭제
class VideoDetail(APIView):
    def get(self, request):
        pass

    def put(self, request):
        pass