# 요구사항
* DRF로 웹 서비스를 제공한다.
* 계정 기능
  * 회원가입
  * 로그인
* ChatGPT 기능
  * ChatGPT로 요청을 보내는 API를 Django 내에서 구현
  * 챗봇 API는 로그인 한 유저만 사용가능하도록 구현
  * 각 user는 하루에 5번만 요청이 가능하도록 구현
* 데이터베이스 기능
  * GPT와 나눈 대화는 데이터베이스에 저장되어야 함
  * 저장된 채팅 내역을 조회가능 해야 함
  * 저장된 채팅 내역은 로그인 한 본인만 볼 수 있음

# 사용기술

* ENVIROMENT
  * Visual Studio Code
* BACKEND
  * Python
  * Django
  * Django Rest Framework
* FRONTEND
  * HTML
  * Tailwind
* DB
  * sqlite
* CLOUD SERVER
  * Amazone Lightsail
    * Ubuntu

# WBS
Link: https://1drv.ms/x/s!AiyH75cHF2uNheJxLhLGTF2vIjmFlg?e=B5sFTF&nav=MTVfe0VFNDFCOEI2LURBRkEtNDAwMS05MUJFLTY0MjJEMjNBQUZBM30

# URL 설계
|URL|설명|CREATE|READ|UPDATE|DELETE|
|:---|:---|:---:|:---:|:---:|:---:|
|1. main|
|/main/index/|메인페이지|X|GET: O|X|X|
|2. account|
|/account/signup/|POST: O|GET: O|X|X|X|
|/account/login/|POST: O|GET: O|X|X|X|
|/account/profile/\<str:username\>/|X|비로그인 User - GET: X<br>로그인 User - GET: O|로그인 한 본인 User - PUT: O<br>로그인 한 본인 제외 모든 User - PUT: X|X|X|
|/account/delete/\<str:username\>/|X|X|X|로그인 한 본인 User - DELETE: O<br>로그인 한 본인 제외 모든 User - DELETE: X|