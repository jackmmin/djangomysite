## django 튜토리얼 - windows 환경
	• DataGrip을 활용해 사이트를 mysql을 사용하여 관리
## 사용 프로그램
	• Pycharm( Professional )
	• DataGrip
	• mysql( [MySQL Community Server 8.0.18 ], [Windows (x86, 64-bit), ZIP Archive] 설치 )
## 실습 시작 !
### 1. 프로젝트 생성, 서버 실행 확인
	• 사진01. 프로젝트 생성
  <img width="910" alt="스크린샷 2019-11-19 오후 6 49 20" src="https://user-images.githubusercontent.com/49246977/69136075-8f92fd00-0afd-11ea-8fb8-5cd6d30e8ec4.png">

	• 사진02. 프로젝트 종류 django 선택, 생성( 이름은 이후 순서에 수정해서 생성합니다. )
  ![67696234-d94e6300-f9e9-11e9-83ce-34f9ba6bc90f](https://user-images.githubusercontent.com/49246977/69136262-e26cb480-0afd-11ea-9b7e-285a0a6391a5.png)
```bash  
cd untitled
```
	• 이제 실습에 필요한 설정들이 들어있는 프로젝트를 진짜 다운로드 합니다.( mysitedjango2 라는 이름으로 시작합니다. )
```bash
django-admin startproject mysitedjango2
cd mysitedjango2
```
	• 원활한 진행을 위해 프로젝트를 mysitedjango2 폴더로 다시 open 합니다.( File -> open -> 생성한 프로젝트 디렉터리 선택 -> OK 클릭 )
```bash
  python manage.py runserver
```
	• 사진03. 홈페이지 뜨는지 확인
![67685482-84eeb780-f9d8-11e9-9af6-b5b91e8a97d3](https://user-images.githubusercontent.com/49246977/69136351-0fb96280-0afe-11ea-8d75-6af6638d5b5a.PNG)

※ 홈페이지 띄우는 터미널은 계속 유지합니다. 터미널을 하나 더 생성 후 필요한 명령을 수행합니다. 홈페이지가 안뜰 땐 Ctrl+c 후 다시 서버를 실행합니다.
### 2. mysql 에서 database 생성
	• mysql 접속 -> mysitedjango2 생성 처음 프로젝트를 생성하고 프로젝트명/setting.py 를 확인했을 때 databases는 sqlite로 설정되어있습니다. 하지만 sqlite는 테스트용이기 때문에 mysql을 사용할 것을 추천합니다.
```bash
create database mysitedjango;
show databases;
```
	• 사진04. database 생성, 확인
![67779076-7cb17d80-faa7-11e9-9780-4c3ea794e14b](https://user-images.githubusercontent.com/49246977/69136329-029c7380-0afe-11ea-8284-f2e416d6cc89.PNG)

### 3. mysitedjango2/setting.py 수정, 서버 실행 확인
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysitedjango2',
        'USER': 'root',
        'PASSWORD': '11111111',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
.
.
.
.

TIME_ZONE = 'Asia/Seoul'
```
```bash
python manage.py runserver
```
※ 만약 Did you install mysqlclient? 에러가 발생한다면
	• 사진05.
  ![67686723-7e613f80-f9da-11e9-802d-c4d837b5ce41](https://user-images.githubusercontent.com/49246977/69136406-22339c00-0afe-11ea-8af3-f9f9bed23c5e.PNG)

	1. File -> Setting -> Project: mysitedjango -> Project Interpreter -> + 클릭( Alt + Insert )
	2. mysqlclient 검색 -> 선택 후 Install Package 클릭
	3. 닫기 -> 설치된 것 확인 -> OK 클릭
	• 사진06.
![67686762-8e791f00-f9da-11e9-86cf-d21b20f705db](https://user-images.githubusercontent.com/49246977/69136430-2d86c780-0afe-11ea-934f-47f8c8e8c70c.PNG)

### 4. polls 앱 시작하기
```bash
python manage.py startapp polls
cd polls
touch urls.py
```
polls/views.py
```python
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
polls/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
mysitedjango/urls.py
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
	• 사진07. http://127.0.0.1:8000/polls/ 로 접속해서 확인하기
![67688712-9ab2ab80-f9dd-11e9-98df-2b11d74f6312](https://user-images.githubusercontent.com/49246977/69136457-3bd4e380-0afe-11ea-866a-1b65a0f7788d.PNG)

### 5. 모델만들기
polls/models.py
```python
import datetime
from django.db import models
from django.utils import timezone
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
def __str__(self):
        return self.question_text
def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
def __str__(self):
        return self.choice_text
mysitedjango2/settings.py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
	• 사진08. 모델 makemigrations -> migrate
![67689718-13fece00-f9df-11e9-9da0-00812e1ab64b](https://user-images.githubusercontent.com/49246977/69136547-5dce6600-0afe-11ea-9bbc-da44fa026755.PNG)

python manage.py makemigrations
python manage.py migrate
### 6. 데이터베이스에서 모델 확인
	• 사진09. + 클릭 -> Data Source -> MySQL 클릭 -> 좌측에 Drivers는 MySQL 클릭 -> MySQL Connector설치
![9](https://user-images.githubusercontent.com/49246977/69136727-b998ef00-0afe-11ea-84ac-74b054734524.png)

<
	• 사진10. User(mysql ID, root), Password(mysql pw, 본인이 입력한했던 root의 pw), Database 입력 -> Test Connection 클릭
※ 만약 timezone 에러가 발생하면 mysql로 접속 후 set global time_zone='+0:00'; 입력 후 다시 Test Connection 클릭
![10](https://user-images.githubusercontent.com/49246977/69136758-c3225700-0afe-11ea-8a86-569cc2194d9b.png)

	• 사진11. DataGrip에서 생성한 db 확인
![11](https://user-images.githubusercontent.com/49246977/69136763-c4ec1a80-0afe-11ea-91f4-9275a021024d.png)

### 7. DB에 Question 저장하기
	• python console 에서 명령 수행한다.( = 터미널에서 python manage.py shell )
```bash
python manage.py shell
```
```python
from polls.models import Choice, Question
from django.utils import timezone
q = Question(question_text="What's up?", pub_date=timezone.now())
q.save()
```
	• 사진12.
![12](https://user-images.githubusercontent.com/49246977/69136803-d9301780-0afe-11ea-925d-6903361971df.png)

### 8. DB에 pk=1인 Question에 choice 저장하기
	• python console 에서 명령 수행
```bash
python manage.py shell
```
```python
from polls.models import Choice, Question
from django.utils import timezone
q = Question.objects.get(pk=1)
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
```
	• 사진13.
![13](https://user-images.githubusercontent.com/49246977/69136807-dfbe8f00-0afe-11ea-956b-18a2018f66af.png)

### 9. 관리자 생성하기
```bash
python manage.py create superuser
```
	• 사진14. 관리자 생성( id: admin, pw: 1111, email: admin@example.com )
![14](https://user-images.githubusercontent.com/49246977/69136810-e0572580-0afe-11ea-8105-db51e819b5fc.png)
