#  Python 3.11이 설치된 Alpine Linux 3.19
# Alpine Linux는 경량화된 리눅스 배포판으로, 컨테이너 환경에 적합
FROM python:3.11-alpine3.19
# FROM : 어떠한 이미지를 선택을 할것인지. / 이미지 라이브러리가 있다.

# LABEL 명령어는 이미지에 메타데이터를 추가합니다. 여기선 관리자 이름 추가.
LABEL maintainer="kimshineday"

# 환경 변수 PYTHONUNBUFFERED를 1로 설정합니다. 
# 이는 Python이 표준 입출력 버퍼링을 비활성화하게 하여, 로그가 즉시 콘솔에 출력되게 합니다. : 실시간으로 확인하는.
# 이는 Docker 컨테이너에서 로그를 더 쉽게 볼 수 있게 합니다.
ENV PYTHONUNBUFFERED 1
# python에서는 0 : False / 1 : True

# 로컬 파일 시스템의 requirements.txt 파일을 컨테이너의 /tmp/requirements.txt로 복사합니다. : 로컬에서 작업한 파일들을 Docker 이미지로 업로드.
# 이 파일은 필요한 Python 패키지들을 명시합니다.
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

# 기본이 되는 폴더
WORKDIR /app
# Django 포트
EXPOSE 8000

ARG DEV=false

# 파이선 패키지 설치하는 명령어. : 본격적인 개발환경을 만들어주는?
RUN python -m venv /py && \ 
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user