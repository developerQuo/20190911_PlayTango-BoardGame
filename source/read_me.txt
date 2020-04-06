widget_screen.py
- 스크린 이름 변경: 번호 -> 놀이판 식별번호
- 인식범위 이름 변경: 인식범위 -> 인식시킬 카드범위지정
- 작업 후 저장하지 않고 다른 스크린 눌렀을 때 작업내용 저장할 것인지 확인
- 미리보기 버튼 위치 오른쪽 위로 변경
- 멀티 셀럭트된 table item 타공위치 버튼으로 한꺼번에 변경 가능
- table widget 타공된 위치는 white, 타공되지 않은 위치는 black 으로 색을 표시
- table widget item 드래그: copy&paste -> multiselect
- 음원 파일 정보 기입 양을 직접 추가 삭제할 수 있도록 변경

widget_block.py
- 블럭이름을 타이핑하면 별명도 같이 되도록 연동 (별명은 개별적으로 변경가능)
- 작업 후 저장하지 않고 다른 블럭 눌렀을 때 작업내용 저장할 것인지 확인
- 입력버튼 생성 (멀티셀렉트 후 한꺼번에 변경 가능)
- 미리보기, 생성, 삭제 버튼 위치 변경
- 수정 후 저장없이 미리보기 가능하도록 변경
- 블럭 정보 입력 후 새로 생성하면 그 정보가 저장되도록 변경
- table widget item 드래그: copy&paste -> multiselect

widget_QnA.py
- 기존 widgetlist, graphicsview, controlbox -> controlbox, widgetlist, graphicsview로 순서 변경 (공통)
- 문제와 정답의 graphicsview에서 블럭 회전 시 alias도 함께 돌아가도록 수정
- 음원(self.mp3_list)의 데이터 구조를 딕셔너리에서 객체로 변환
- 음원 요소 모두를 사용자가 지정할 수 있도록 데이터 입력 칸을 변경
- 작업 후 저장하지 않고 다른 것을 눌렀을 때 작업내용 저장할 것인지 확인

block_init.py
- Tango_block을 ScreenObject, BlockObject, QuestionObject, AnswerObject, Mp3Object에 상속하고 변수 오버라이딩
- 페인트 함수 삭제