import pygame as pg
 
pg.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLOCK_SIZE = 20

# 게임 창의 이름 설정
pg.display.set_caption("Snake")

def draw_block(screen, color, blocks):
    """ screen의 position 위치에 color 색으로 블록을 그립니다. """
    # blocks : [(y, x), ...]
    # pg.Rect 인스턴스 ((x, y), (w, h))
    for y, x in blocks:
        block = pg.Rect((y*BLOCK_SIZE, x*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
        pg.draw.rect(screen, color, block)


done = False
clock = pg.time.Clock()

while not done:
    # 1초당 화면 출력 횟수 (10, 30 60 정도로 설정)
    clock.tick(10) 
    
    # 게임 실행 중 발생하는 이벤트를 포착
    ## 게임 종료 이벤트가 발생하면 메인 루프 종료하도록 처리
    for event in pg.event.get():
        # 게임 실행 창의 종료 버튼 클릭시
        if event.type == pg.QUIT:
            done = True

    # 화면 배경 색상 설정
    screen.fill(WHITE)

    blocks = [(0, 0)]
    draw_block(screen, GREEN, blocks)
    
    '''
    작업
    '''

    # 메인 루프의 끝에 반드시 display.flip()을 통해 메인 루프에서 진행된 작업을 화면에 업데이트 해주어야 함
    pg.display.flip()

pg.quit()