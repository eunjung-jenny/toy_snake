import pygame as pg
from random import randint
 
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

apple = []
done = False
clock = pg.time.Clock()
blocks = [[5, 5]]

def get_apple_coord():
    x = randint(0, 19)
    y = randint(0, 14)
    # apple = pg.Rect((x, y), (BLOCK_SIZE, BLOCK_SIZE))
    # pg.draw.rect(screen, RED, apple)
    return [x, y]


while not done:
    # 1초당 화면 출력 횟수 (10, 30 60 정도로 설정)
    clock.tick(10) 
    
    screen.fill(WHITE)
    # [y, x]
    

    # 게임 실행 중 발생하는 이벤트를 포착
    ## 게임 종료 이벤트가 발생하면 메인 루프 종료하도록 처리
    for event in pg.event.get():
        # 게임 실행 창의 종료 버튼 클릭시
        if event.type == pg.QUIT:
            done = True
        # 키보드가 눌렸다면
        elif event.type == pg.KEYDOWN:
            # 어떤 키보드가 눌렸는지에 따라
            if event.key == pg.K_UP:
                blocks[0][1] -= 1
            elif event.key == pg.K_DOWN:
                blocks[0][1] += 1
            elif event.key == pg.K_LEFT:
                blocks[0][0] -= 1
            elif event.key == pg.K_RIGHT:
                blocks[0][0] += 1

    draw_block(screen, GREEN, blocks)
    
    # screen에 사과가 없을 때에만 새로운 사과를 생성
    if not apple:
        apple.append(get_apple_coord())
    
    draw_block(screen, RED, apple)

    # 메인 루프의 끝에 반드시 display.flip()을 통해 메인 루프에서 진행된 작업을 화면에 업데이트 해주어야 함
    pg.display.flip()

pg.quit()