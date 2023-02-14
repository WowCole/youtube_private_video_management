# 유튜브 비공개 회원관리

### 디자인 업데이트 예정

<img src="./스크린샷%202023-02-14%20오전%2011.01.20.png"/>

---

## 프로그램 주요 기능

- 회원제로 비공개 영상 혹은 라이브를 진행하게 될때 수동으로 이메일을 추가해야하는 번거로움을 해결하고자 만들어진 프로그램
- 여러가지 채널을 동시에 관리할 수 있음.
- 회원들의 정보가 변화했을떄 비공개 영상들을 확인하여 이메일을 수정
- 일부공개영상을 업로드 하거나 일부공개 라이브를 진행한 경우 해당 영상이 업데이트 되어야 하는 요일을 체크하여 선택해서 비공개로 전환하고 이메일을 추가.

## 필수 준비물

- 회원 정보 파일의 구성
  - CSV 확장자
  - '이메일' 칼럼
    - '이메일' 이라는 칼럼 아래에 회원들의 이메일이 추가 되어야함
  - 파일의 제목
    - 채널명과 태그 그리고 요일은 "," 로 구분
    - 채널명
    - 태그
    - 요일(영어로 작성)
      - mon,tue,thu,
      - 요일과 요일 사이는 "&" 로 구분
    - ex) 채널명,@태그,요일&요일.csv
- 폴더의 구성
  - 폴더는 로그인하는 하나의 계정 안의 수정하고자 하는 채널 정보가 담겨야함
    - 다른 계정으로 로그인할 때에는 해당 계정에 맞는 폴더를 선택해야함
  - 폴더 구조 예시
    - 계정1폴더
      - 채널명,@태그,요일&요일.csv
      - 채널명,@태그,요일&요일.csv
      - 채널명,@태그,요일&요일.csv
      - 채널명,@태그,요일&요일.csv
      - 채널명,@태그,요일&요일.csv
    - 계정2폴더
      - 채널명,@태그,요일&요일.csv
      - 채널명,@태그,요일&요일.csv
      - 채널명,@태그,요일&요일.csv
      - 채널명,@태그,요일&요일.csv
      - 채널명,@태그,요일&요일.csv

## 사용법

1. 관리하고자 하는 유튜브 아이디로 로그인 한다.
2. 일부공개 영상에 이메일을 추가할것인지 혹은 비공개 영상들의 회원을 수정할것인지 선택한다.
3. 로그인

## 주요 알고리즘

### 일부공개 혹은 비공개

1.  비공개

    - 비공개 영상 수정 시에 마지막으로 프로그램을 실행 한 시간이 timestamp 의 형태로 save.txt에 저장된다. 프로그램이 시작될때마다 마지막으로 회원 정보가 담긴 CSV파일의 수정 시간과 비교하여 프로그램을 마지막으로 실행했던 시간 이후 새로 바뀐 변경 사항이 있는 자료만 선택하여 진행한다.
      - 만약 바뀐 자료가 없다면 바로 종료
      - 비공개 선택시 이미 저장된 회원 이메일과 CSV파일 상의 회원 이메일을 비교하여 이메일이 다를 때에만 수정

2.  일부공개
    - 일부공개 선택시 모든 영상을 비공개로 설정하고 모든 회원의 이메일 정보를 삽입
    - 시간과 관계 없이 새로운 일부공개 영상이 추가된 날짜에 해당하는 영상을 모두 변경

- 리셋버튼은 프로그램에 저장되는 최근 로그인한 이메일 정보와 마지막 사용 시간정보 삭제

## 사용시 주의사항

- 구글 로그인 이후 2차 인증이 있다면 수동으로 해주어야 함.
- 만약 비밀번호가 틀려서 로그인이 되지 않았다면 끄지 말고 떠있는 브라우져에 그대로 비밀번호를 입력하고 확인버튼만 눌러주면 됨.
- undetected-chromedriver 3.2.1 작동 확인완료
