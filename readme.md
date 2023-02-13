# 유튜브 비공개 회원관리

<img src="./스크린샷%202023-02-13%20오후%204.32.31%20복사본.png">

## 필수 준비물

- 회원 이메일이 담긴 테이블로 구성된 CSV파일
  - 테이블에 어떠한 칼럼이 담겨도 상관 없으며 이메일만 한글로 '이메일' 이라는 명칭의 테이블로 만들면 됨
  - 파일의 이름은 로그인 한 이후 선택하게될 체널명과 체널의 태그로 이루어져야 하며 그 사이는',' 콤마로 구분되어야함
    - ex) 채널명,@태그.csv
  - 만약 채널명과 태그 이후 다른 내용을 추가하여 구분해야 한다면 띄어쓰기 이후 작성할것
    - ex) 채널명,@태그 기타등등.csv

---

- 하나의 폴더 안에 여러 회원 파일을 담을 수 있다.
  - 유튜브 비공개 정원이 50명이기 때문에 만약 50명 이상으로 넘어가면 새로운 채널을 만들어 배정할 수 있고 하나의 폴더 안에 다른 채널의 정보를 넣어 같이 실행시킬 수 있다.

## 주요 알고리즘

- 마지막으로 프로그램을 실행 한 시간이 timestamp 의 형태로 save.txt에 저장된다. 프로그램이 시작될때마다 마지막으로 회원 정보가 담긴 CSV파일의 수정 시간과 비교하여 프로그램을 마지막으로 실행했던 시간 이후 새로 바뀐 변경 사항이 있는 자료만 선택하여 진행한다.
- 만약 바뀐 자료가 없다면 바로 종료
- 일부공개 혹은 비공개
  - 일부공개 선택시 모든 영상을 비공개로 설정하고 모든 회원의 이메일 정보를 삽입
  - 비공개 선택시 이미 저장된 회원 이메일과 CSV파일 상의 회원 이메일을 비교하여 이메일이 다를 때에만 수정
- 리셋버튼은 프로그램에 저장되는 최근 로그인한 이메일 정보와 마지막 사용 시간정보 삭제

## 사용시 주의사항

- 구글 로그인 이후 2차 인증이 있다면 수동으로 해주어야 함.
- 만약 비밀번호가 틀려서 로그인이 되지 않았다면 끄지 말고 떠있는 브라우져에 그대로 비밀번호를 입력하고 확인버튼만 눌러주면 됨.
