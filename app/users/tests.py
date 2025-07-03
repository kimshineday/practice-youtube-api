from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
# TDD : Test Driven Development 테스트 주도 개발
class UserTestCase(TestCase):
    # test 함수와 일반 함수를 구분하기 위해서 함수 이름 앞에 'test_' 표기
    
    def test_create_user(self): # 일반 유저 생성 테스트
        email = 'usertest@email.com'
        password = 'userpass0987'

        user = get_user_model().objects.create_user(email=email, password=password)

        # 유저 생성이 잘 되었는지 확인
        self.assertEqual(user.email, email)
        # self.assertEqual(user.check_password(password), True)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)
        # self.assertEqual(user.is_superuser, False)

        # self.assertFalse(user.is_superuser)
    # 유저 입장에서 생각해서 작성.

    def test_create_superuser(self): # 슈퍼 유저 생성 테스트
        email = 'superusertest@email.com'
        password = 'superpass0987'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        # super user
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

# docker compose run --rm app sh -c 'python manage.py makemigrations'
# docker compose run --rm app sh -c 'python manage.py migrate'
# docker compose run --rm app sh -c 'python manage.py test users'