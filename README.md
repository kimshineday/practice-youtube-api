# PRACTICE-YOUTUBE-API
## 🐳 Docker
프로세스를 격리하는 컨테이너 플랫폼.  
'작은 OS를 하나 더 띄운다.'

작업, 개발하면서 일관된 실행 환경이 필요할 경우, 운영체제 차이로 인한 배포 오류를 줄이기위해 사용되어지고 있다.
빠른 시작, 버전관리가 가능하다는 점, 확장성이 좋다.
### 구성요소
애플리케이션 실행 단위(격리된 프로세스 집합) >> **컨테이너**  
컨테이너 실행에 필요한 파일 시스템 >> **이미지**

> Docker file >>build>> Docker image >>run>> Docker Container  

Docker Daemon : 컨테이너 관리를 담당하는 백그라운드 프로세스  
Docker CLI : Daemon과 통신하는 명령줄 도구  
Registry : 이미지 저장소 (꽁용 Dock)
### Docker Image / Docker Container
#### 🖼️ Image
: 애플리케이션을 실행하기 위한 정보들을 가지고 있다. (읽기 전용)
#### 📦 Container
: 이미지 기반으로 생성된 정보들을 실행할 수 있는 (가상)환경

이 프로젝트에서의 컨테이너 구성 :
- container 1 : Django
- container 2 : DataBase [Postgre SQL]
- container 3 : NGINX 