# 프로젝트 설계
## 요구사항
* DRF로 웹 서비스를 제공한다.
* 계정 기능
  * 회원가입
  * 로그인
* 데이터베이스 기능
  * Post 글을 저장, 조회, 수정이 가능해야 함
* JWT를 사용한 사용자 인증 관리
  * 토큰을 통해 인증이 관리되어야 함

## 사용기술

* ENVIROMENT
  * ![Static Badge](https://img.shields.io/badge/visualstudiocode-%23007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
* BACKEND
  * ![Static Badge](https://img.shields.io/badge/python-%233776AB?style=flat-square&logo=python&logoColor=white)
  * ![Static Badge](https://img.shields.io/badge/django-%23092E20?style=flat-square&logo=django&logoColor=white)
  * Django Rest Framework
* FRONTEND
  * ![Static Badge](https://img.shields.io/badge/html5-%23E34F26?style=flat-square&logo=html5&logoColor=white)
  * ![Static Badge](https://img.shields.io/badge/tailwindcss-%2306B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
* DB
  * ![Static Badge](https://img.shields.io/badge/sqlite-%23003B57?style=flat-square&logo=sqlite&logoColor=white)


## 페이지 디자인
Link: https://www.figma.com/file/tCeQczwVeGsv9PKTyDdufc/Untitled?type=design&node-id=0%3A1&mode=design&t=soJvn1KAzm7DTD5Z-1
|||
|:---:|:---:|
|![idle](https://github.com/mamananama/ahro_drf_project/assets/114140050/3d1b3fe9-7fda-4f7e-9634-1601707af4ea)|![login](https://github.com/mamananama/ahro_drf_project/assets/114140050/d2fc641f-b663-4d8f-ad33-24b9049920b3)|
|메인 페이지|메인 페이지(로그인 상태)|
|![signup](https://github.com/mamananama/ahro_drf_project/assets/114140050/ed1a26e9-8900-497f-b166-efb6b5985184)|![login](https://github.com/mamananama/ahro_drf_project/assets/114140050/99a9305c-0689-4aa7-9e1b-5a45279c336e)|
|회원가입 페이지|로그인 페이지|


## WBS
Link: https://1drv.ms/x/s!AiyH75cHF2uNheJxLhLGTF2vIjmFlg?e=B5sFTF&nav=MTVfe0VFNDFCOEI2LURBRkEtNDAwMS05MUJFLTY0MjJEMjNBQUZBM30

## ERD
![drf_project](https://github.com/mamananama/ahro_drf_project/assets/114140050/da9ac7b4-5d1a-4ead-985f-045e49490f41)



## URL 설계
|URL|설명|CREATE|READ|UPDATE|DELETE|
|:---|:---|:---:|:---:|:---:|:---:|
|1. main|
|/main/index/|메인페이지|X|GET: O|X|X|
|2. account|
|/account/signup/|회원가입 페이지|POST: O|GET: O|X|X|X|
|/account/login/|로그인 페이지|POST: O|GET: O|X|X|X|
|3. rounge|
|/rounge/|자유게시판 페이지|로그인 User - POST: O<br>비로그인 User - POST: X|GET: O|X|X|
|/rounge/post/\<int:post_pk\>|게시물 상세 페이지|X|GET: O|로그인 한 본인 User - PUT: O<br>로그인 한 본인 제외 모든 User - PUT: X|로그인 한 본인 User - DELETE: O<br>로그인 한 본인 제외 모든 User - DELETE: X|

## 아키텍처
![architecture](https://github.com/mamananama/ahro_drf_project/assets/114140050/57a3b1f1-8836-4c11-b12e-8c83301a782b)



# 프로젝트 설명
## 프로젝트 결과
### 메인페이지
![image](https://github.com/mamananama/ahro_drf_project/assets/114140050/0286cc01-d320-4a93-9207-4042695d9307)

### 로그인페이지
![image](https://github.com/mamananama/ahro_drf_project/assets/114140050/b69b93d3-6914-4832-8cfa-bba36f82ec79)

### 로그인이후
![image](https://github.com/mamananama/ahro_drf_project/assets/114140050/b18f0ab0-0e6d-4289-b4f3-2ab077ce49fa)

### ROUNGE 게시판
![image](https://github.com/mamananama/ahro_drf_project/assets/114140050/8b56e0f8-99a2-4b14-908f-e1cb21e2c840)

### 게시물 작성
![image](https://github.com/mamananama/ahro_drf_project/assets/114140050/503ebde8-4807-4a81-949f-60e06f86de92)

### 게시물 작성 이후
![image](https://github.com/mamananama/ahro_drf_project/assets/114140050/11f9657f-66ec-49ea-95ab-b42b498fc006)

## 사용자 인증
* JWT 토큰을 통해 현재 사용자를 인증받습니다.
  * 로그인 상태에서 local storage에 access 토큰과 refresh 토큰을 받습니다.
 ![image](https://github.com/mamananama/ahro_drf_project/assets/114140050/7f30ba8c-acd2-403e-a4ce-5093cd05de4c)
  * 로그아웃을 실행하면 local storage에 저장된 access 토큰과 refresh 토큰을 삭제합니다.
 ![image](https://github.com/mamananama/ahro_drf_project/assets/114140050/b12673c8-57a0-41b7-96aa-85f577367262)

