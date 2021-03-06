import sys
import pygame as pg
from random import randint

pg.init()

WHITE =   (255, 255, 255)
BLACK =   (  0,   0,   0)
GRAY =    (202, 204, 203)
GREEN =   ( 12, 107,  31)
D_GREEN = ( 11,  84,  26)
RED =     (255,   0,   0)

PAUSE_KEYS = (pg.K_SPACE, pg.K_p)
DIRECTION_KEYS = (pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BLOCK_SIZE = 20
MAX_X = SCREEN_WIDTH // BLOCK_SIZE - 1
MAX_Y = SCREEN_HEIGHT // BLOCK_SIZE - 1

YUMMY_SOUND = pg.mixer.Sound('apple_crunch.wav')
SCREAM_SOUND = pg.mixer.Sound('game_over.wav')

pg.display.set_caption('Snake')
font = pg.font.SysFont('comicsans', 20, True)
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

apple = []
snake = []
tail = [None, None]

def paint_score(snake, screen):
    score = len(snake)
    text = font.render("Score: " + str(score), 1, BLACK)
    screen.blit(text, (320, 10))

def quit_game():
    pg.quit()
    sys.exit()
    quit()

def pause():
    pause = True
    while pause:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key in (pg.K_SPACE, pg.K_p):
                pause = False
            if event.type == pg.QUIT:
                quit_game()

def move_snake(direction):
    tail[0] = snake[-1][0]
    tail[1] = snake[-1][1]

    for i in range(len(snake)-1, 0, -1):
        snake[i] = snake[i-1][:]
           
    if direction == 'UP':
        snake[0][1] -= 1
    elif direction == 'DOWN':
        snake[0][1] += 1
    elif direction == 'LEFT':
        snake[0][0] -= 1
    elif direction == 'RIGHT':
        snake[0][0] += 1

def draw_snake(screen, snake):
    """ screen의 position 위치에 color 색으로 블록을 그립니다. """
    # snake : [(y, x), ...]
    # pg.Rect 인스턴스 ((x, y), (w, h))
    if snake:
        head = pg.Rect((snake[0][0]*BLOCK_SIZE, snake[0][1]*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
        pg.draw.rect(screen, D_GREEN, head)
    if len(snake) > 1:
        for y, x in snake[1:]:
            block = pg.Rect((y*BLOCK_SIZE, x*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
            pg.draw.rect(screen, GREEN, block)

def change_direction(key):
    if key == pg.K_UP:
        return 'UP'
    elif key == pg.K_DOWN:
        return 'DOWN'
    elif key == pg.K_LEFT:
        return 'LEFT'
    elif key == pg.K_RIGHT:
        return 'RIGHT'

def is_valid_change(direction, key):
    if direction == 'DOWN' and key == pg.K_UP:
        return False
    elif direction == 'UP' and key == pg.K_DOWN:
        return False
    elif direction == 'LEFT' and key == pg.K_RIGHT:
        return False
    elif direction == 'RIGHT' and key == pg.K_LEFT:
        return False
    else:
        return True

def get_apple_coord():
    x = randint(0, MAX_X)
    y = randint(0, MAX_Y)
    while [x, y] in snake:
        x = randint(0, MAX_X)
        y = randint(0, MAX_Y)
    # apple = pg.Rect((x, y), (BLOCK_SIZE, BLOCK_SIZE))
    # pg.draw.rect(screen, RED, apple)
    return [x, y]

def draw_apple(spot):
    """ screen의 position 위치에 color 색으로 블록을 그립니다. """
    # blocks : [(y, x), ...]
    # pg.Rect 인스턴스 ((x, y), (w, h))
    apple = pg.Rect((spot[0]*BLOCK_SIZE, spot[1]*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pg.draw.rect(screen, RED, apple)

def put_apple():
    spot = get_apple_coord()
    draw_apple(spot)
    apple.append(spot)

def is_over():
    if not (0 <= snake[0][0] <= MAX_X and 0 <= snake[0][1] <= MAX_Y):
        pg.mixer.Sound.play(SCREAM_SOUND)
        return True
    elif snake[0] in snake[1:]:
        pg.mixer.Sound.play(SCREAM_SOUND)
        return True
    else:
        return False

def eat_n_grow():
    if apple and snake[0] == apple[0]:    
        pg.mixer.Sound.play(YUMMY_SOUND)
        apple.clear()      
        snake.append(tail)

def paint_text(command):
    global snake
    if command == "intro":
        font = pg.font.SysFont('comicsans', 50)
        title = font.render('SNAKE', 1, BLACK)
        titlepos = title.get_rect()
        titlepos.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        screen.blit(title, titlepos)
        
        font = pg.font.SysFont('comicsans', 25)
        start = font.render('Press ARROW BUTTONS to start!', 1, RED)
        startpos = start.get_rect()
        startpos.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+40)
        screen.blit(start, startpos)

    elif command == "game_over":
        font = pg.font.SysFont('comicsans', 50)
        title = font.render(f'Your score: {len(snake)}', 1, BLACK)
        titlepos = title.get_rect()
        titlepos.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        screen.blit(title, titlepos)

        font = pg.font.SysFont('comicsans', 25)
        start = font.render('Press ENTER to restart!', 1, RED)
        startpos = start.get_rect()
        startpos.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+40)
        screen.blit(start, startpos)

def game_over_screen():
    pg.mixer.music.stop()
    game_over = True

    while game_over:
        clock.tick(10)
        paint_text("game_over")
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                game_over = False
                game_loop()

def game_intro():
    global snake
    snake = [[5, 5]]
    screen.fill(GRAY)
    draw_snake(screen, snake)
    paint_score(snake, screen) 
    intro = True

    while intro:
        clock.tick(10)
        # screen.fill(WHITE)
        paint_text("intro")
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
            elif event.type == pg.KEYDOWN and event.key in DIRECTION_KEYS:
                intro = False
                return change_direction(event.key)    

def game_loop():
    pg.mixer.music.load('bgm.mp3')
    pg.mixer.music.play(-1)
    current_direction = game_intro()

    while True:
        # 1초당 화면 출력 횟수 (10, 30 60 정도로 설정)
        clock.tick(10) 
        screen.fill(GRAY) 
        
        # 게임 실행 중 발생하는 이벤트를 포착
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()

            elif event.type == pg.KEYDOWN:
                if event.key in PAUSE_KEYS:
                    pause()
                elif event.key in DIRECTION_KEYS and is_valid_change(current_direction, event.key):
                    current_direction = change_direction(event.key)
                
        move_snake(current_direction)
        
        eat_n_grow()        

        draw_snake(screen, snake)    
                
        if is_over():
            game_over_screen()
            # game_loop()
        
        if not apple:
            put_apple()
        if apple:
            draw_apple(apple[0])

        paint_score(snake, screen)

        # 메인 루프의 끝에 반드시 display.flip()을 통해 메인 루프에서 진행된 작업을 화면에 업데이트 해주어야 함
        pg.display.flip()

# game_intro()
game_loop()

pg.quit()