# spartamarket

## 프로젝트 개요

`spartamarket`은 회원 관리와 물건 게시 기능을 제공하는 웹 애플리케이션입니다.  
유저는 회원가입, 로그인, 로그아웃을 통해 서비스를 이용하며, 각 유저는 자신의 물건을 등록하고, 마음에 드는 물건을 찜할 수 있습니다.  
이 애플리케이션에서는 물건을 등록하고 관리하는 기능에 집중하고 있으며, 구매 기능은 포함되지 않습니다.  
또한, 유저 간의 팔로우 기능과 프로필 사진 기능도 제공합니다.

---
<details>
<summary>주요 기능</summary>

## 주요 기능

### 1. 회원 기능
- **회원가입 / 로그인 / 로그아웃**: 유저는 회원가입을 통해 계정을 생성하고 로그인하여 서비스를 이용할 수 있습니다. 비회원은 서비스를 이용할 수 없습니다.
- **유저 프로필 페이지**: 각 유저는 자신이 등록한 물건과 찜한 물건들을 프로필 페이지에서 확인할 수 있습니다.
- **팔로우 기능**: 유저는 다른 유저를 팔로우할 수 있으며, 팔로워 수와 팔로잉 수를 확인할 수 있습니다.
- **프로필 사진 기능**: 유저는 프로필 사진을 수정할 수 있으며, 기본 프로필 사진이 제공됩니다.

### 2. 게시 기능
- **물건 게시 및 관리**: 유저는 물건을 등록, 수정, 삭제할 수 있습니다.
- **물건 목록 및 디테일 페이지**: 물건 목록을 확인하고, 개별 물건에 대한 상세 정보를 볼 수 있습니다.
- **찜하기 기능**: 유저는 물건을 찜할 수 있으며, 찜한 물건은 찜수와 함께 표시됩니다.
- **물건 정렬**: 물건 목록을 최신순으로 정렬할 수 있습니다.

### 3. 해시태그 기능
- **해시태그 설정**: 유저는 각 물건에 해시태그를 설정할 수 있습니다.
- **해시태그 규칙**: 해시태그는 유일하고, 띄어쓰기 및 특수문자는 허용되지 않습니다. 중복된 해시태그는 등록할 수 없습니다.

</details>

<details>
<summary>설치 방법</summary>

## 설치 방법

### 리포지토리 클론
```
git clone https://github.com/seunghwan-jang4/spartamarket.git
cd spartamarket
```

### 가상 환경 설정
```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 필요한 패키지 설치
```
pip install -r requirements.txt
```


### 데이터베이스 마이그레이션
```
python manage.py migrate
```

### 서버 실행
```
python manage.py runserver
```
</details>

## 사용 방법
### 회원가입 및 로그인
/signup/ 페이지에서 회원가입을 하고, /login/ 페이지에서 로그인하여 시스템에 접근할 수 있습니다.

### 프로필 페이지
로그인 후 /profile/ 페이지에서 자신의 프로필을 확인하고, 프로필 사진을 수정할 수 있습니다.

### 물건 게시 및 관리
/add-item/ 페이지에서 새로운 물건을 등록하고, /items/ 페이지에서 물건 목록을 볼 수 있습니다.
각 물건은 찜하기 기능을 지원하며, 게시물 수정 및 삭제도 가능합니다.

### 정렬 기능
물건 목록 페이지에서 최신순으로 물건을 정렬할 수 있습니다.

### 해시태그 설정
물건 등록 시, 해시태그를 설정할 수 있으며, 해시태그는 띄어쓰기나 특수문자 없이 유일한 값으로 등록됩니다.


## sparta_market의 ERD 

![스크린샷 2024-12-27 234956](https://github.com/user-attachments/assets/ccb15e62-dc29-4ef7-9cfb-816191842771)

