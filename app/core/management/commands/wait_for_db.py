# 'wait_for_db' 라는 명령어를 만듦
# Django가 DB가 준비되고 나서 연결하게끔 하기 위함 > 하나의 도커 이미지에 각 컨테이너(app, db)가 존재하기 때문.

from django.core.management.base import BaseCommand
from django.db import connections # DB와 연결을 시도
import time
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError

class Command(BaseCommand):
    def handle(self, *args, **options): # 유연한 함수
        self.stdout.write('Wating for DB Connection ...')

        is_db_connected = None

        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except:
                self.stdout.write('Retry DB Connection ...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Success to PostgreSQL connection'))