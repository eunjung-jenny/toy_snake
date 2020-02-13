# [토이] 스네이크 게임

- pygame 모듈을 활용하여 스네이크 게임을 구현해 보자.

## 1. pygame

- `pip3 install pygame` 로 pygame 모듈을 설치

### 1) pygame 사용을 위한 기본 구조

> [참고자료](https://kkamikoon.tistory.com/129)

1. `import pygame`
2. `pygame.init()` 으로 초기화
3. 전역변수 선언 (아래는 대표적으로 필요한 전역변수)
   - `size = [x 크기, y 크기]` : 게임이 실행될 창의 크기
   - `screen = pygame.display.set_mode(size)` : size 변수에 맞게 창을 생성하며, screen 변수를 통해 화면을 초기화하거나 화면에 요소를 추가하는 등의 작업을 수행
   - `clock = pygame.time.Clock()` : 초당 화면 출력 횟수를 설정
   - 게임 상에서 사용할 색상 등.
4. while 문을 활용한 pygame 메인 루프
   4-1. pygame 이벤트 설정
   4-2. pygame 화면 설정
   4-3. 사용자 행위

### 2) screen에 블럭 그리기

> [참고자료](https://python.bakyeono.net/chapter-12-1.html)

1. `block = pygame.Rect((coord_x, coord_y), (width, height))` 인스턴스 생성
2. `pygame.ddraw.rect(screen, color, block)` : screen의 position 위치에 color 색으로 블록을 그립니다.

### 3) pygame event list

> [참고자료](https://kkamikoon.tistory.com/132)

- 아래의 이벤트명들은 `pygame.이벤트명` 의 형식으로 사용한다.
- 이벤트를 확인할 때는 `if event.type == pygame.이벤트명` 으로 체크한다.
1. QUIT : 
2. KEYDOWN: 키보드를 누른 후 떼는 순간에 발생 | KEYUP : 키보드를 누르는 순간에 발생
   1. [각 키보드 버튼에 대한  pygame 상수명](https://www.pygame.org/docs/ref/key.html)


## 2. 게임 구현

### 1) 필요 기능

- [x] 뱀이 돌아다닐 좌표 구현
   - [x] screen
- [x] 뱀의 이동
   - [x] 머리 이동
   - [x] 몸통 이동
   - [] 자동 이동
   - [x] 머리 색상 다르게 표현
   - [] 진행 방향의 반대 방향 키보드 입력 무시
- [] 랜덤한 시간, 랜덤한 위치에 먹이 생성
   - [x] 랜덤한 위치에 먹이 생성
   - [x] 먹이는 한 개씩만 생성
   - [] 랜덤한 시간에 생성
   - [x] 뱀의 몸통이 있는 곳은 제외
- [] 뱀의 머리가 먹이가 있는 좌표와 겹쳤을 때 뱀의 몸통 길이 1 증가
   - [x] 사과를 제거
   - [x] 몸통 길이 증가
- [x] 게임 오버
   - [x] 뱀이 좌표 밖으로 이동하는 경우 게임 종료
   - [x] 뱀의 머리가 몸통과 겹칠 경우 게임 종료
- [] 뱀 길이 표시
- [] 랭킹