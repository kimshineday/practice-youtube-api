from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase

class VideoAPITestCase(APITestCase):
    # 테스트 코드 케이스 실행 전 먼저 실행되는 함수 > 테스트 전 데이터 생성
    # 1. 유저 생성 및 로그인
    def setUp(self): pass

    # api/v1/videos [GET]
    def test_video_list_get(self): pass
    def test_video_list_post(self): pass
    # 특정 비디오 조회
    def test_video_detail_get(self): pass
    # 특정 비디오 업데이트(수정)
    def test_video_detail_put(self): pass
    # 특정 비디오 삭제
    def test_video_detail_delete(self):pass
    