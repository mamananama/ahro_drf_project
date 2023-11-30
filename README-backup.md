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
* TDD 방법론 도입
  * test 기반의 개발 방법론
* JWT를 사용한 사용자 인증 관리
  * 토큰을 통해 인증이 관리되어야 함

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
  * AWS Lightsail
    * Ubuntu

# 페이지 디자인
Link: https://www.figma.com/file/tCeQczwVeGsv9PKTyDdufc/Untitled?type=design&node-id=0%3A1&mode=design&t=soJvn1KAzm7DTD5Z-1
|||
|:---:|:---:|
|![idle](https://github.com/mamananama/ahro_drf_project/assets/114140050/3d1b3fe9-7fda-4f7e-9634-1601707af4ea)|![login](https://github.com/mamananama/ahro_drf_project/assets/114140050/d2fc641f-b663-4d8f-ad33-24b9049920b3)|
|메인 페이지|메인 페이지(로그인 상태)|
|![signup](https://github.com/mamananama/ahro_drf_project/assets/114140050/ed1a26e9-8900-497f-b166-efb6b5985184)|![login](https://github.com/mamananama/ahro_drf_project/assets/114140050/99a9305c-0689-4aa7-9e1b-5a45279c336e)|
|회원가입 페이지|로그인 페이지|





# WBS
Link: https://1drv.ms/x/s!AiyH75cHF2uNheJxLhLGTF2vIjmFlg?e=B5sFTF&nav=MTVfe0VFNDFCOEI2LURBRkEtNDAwMS05MUJFLTY0MjJEMjNBQUZBM30

# URL 설계
|URL|설명|CREATE|READ|UPDATE|DELETE|
|:---|:---|:---:|:---:|:---:|:---:|
|1. main|
|/main/index/|메인페이지|X|GET: O|X|X|
|2. account|
|/account/signup/|회원가입 페이지|POST: O|GET: O|X|X|X|
|/account/login/|로그인 페이지|POST: O|GET: O|X|X|X|
|/account/profile/\<str:username\>/|개인 프로필 페이지|X|로그인 User - GET: O<br>비로그인 User - GET: X|로그인 한 본인 User - PUT: O<br>로그인 한 본인 제외 모든 User - PUT: X|X|X|
|/account/delete/\<str:username\>/|회원 탈퇴 페이지|X|X|X|<로그인 한 본인 User - DELETE: O<br>로그인 한 본인 제외 모든 User - DELETE: X
|3. schedule|
|/schedule/|나의 스케쥴 목록과 스케쥴을 등록할 수 있는 페이지|로그인 User - POST: O<br>비로그인 User - POST: X|로그인 User - GET: O<br>비로그인 User - GET: X|X|X|
|/schedule/chat/|ChatGPT API를 통하여 GPT와 User의 채팅이 이루어지고,<br>일정의 등록, 열람, 수정, 삭제가 발생하는 페이지|로그인 User - POST: O<br>비로그인 User - POST: X|로그인 User - GET: O<br>비로그인 User - GET: X|로그인 User - PUT: O<br>비로그인 User - PUT: X|로그인 User - DELETE: O<br>비로그인 User - DELETE: X|
|4. rounge|
|/rounge/|자유게시판 페이지|로그인 User - POST: O<br>비로그인 User - POST: X|GET: O|X|X|
|/rounge/\<int:post_pk\>|게시물 상세 페이지|X|GET: O|로그인 한 본인 User - PUT: O<br>로그인 한 본인 제외 모든 User - PUT: X|로그인 한 본인 User - DELETE: O<br>로그인 한 본인 제외 모든 User - DELETE: X|
