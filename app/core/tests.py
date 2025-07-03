from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from unittest.mock import patch # 연결, 시도 하는 것들을 가로채올 수 있는.
from django.core.management import call_command
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError

# Command test
@patch('django.db.utils.ConnectionHandler.__getitem__') # DB 연결 시도를 가져오는
class CommandsTests(SimpleTestCase):
    # 'wait_for_db'가 잘 작동하는지 체크 (: DB 준비되었을때 django와의 연결시도)
    def test_wait_for_db_ready(self, patched_getitem):
        patched_getitem.return_value = True # 연결 성공 시
        
        call_command('wait_for_db') # 명령어 불러오기
        
        self.assertEqual(patched_getitem.call_count, 1) # call_count가 1번일때 테스트 통과 
    

    # DB 연결에 오류가 발생했다는 가정, 테스트
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        patched_getitem.side_effect = [Psycopg2OperationalError] + \
            [OperationalError] * 5 + [True]
        
        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)


    # 테스트 실행 명령어 
    # docker-compose run --rm app sh -c 'python manage.py test core'