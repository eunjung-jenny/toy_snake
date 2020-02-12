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
