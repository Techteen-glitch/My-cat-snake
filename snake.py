import pygame, sys, random
from pygame.math import Vector2
cell_size=40
cell_number=20
class SNAKE:
    def __init__(self):
        self.body=[Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction=Vector2(1,0)
        self.next_direction = Vector2(1, 0) 
        self.new_block=False
        self.head_up=pygame.image.load('head_up.png').convert_alpha()
        self.head_up=pygame.transform.scale(self.head_up,(cell_size,cell_size))
        self.head_right=pygame.image.load('head_right.png').convert_alpha()
        self.head_right=pygame.transform.scale(self.head_right,(cell_size,cell_size))
        self.head_down=pygame.image.load('head_down.png').convert_alpha()
        self.head_down=pygame.transform.scale(self.head_down,(cell_size,cell_size))
        self.head_left=pygame.image.load('head_left.png').convert_alpha()
        self.head_left=pygame.transform.scale(self.head_left,(cell_size,cell_size))
        self.tail_up=pygame.image.load('tail_up.png').convert_alpha()
        self.tail_up=pygame.transform.scale(self.tail_up,(cell_size,cell_size))
        self.tail_down=pygame.image.load('tail_down.png').convert_alpha()
        self.tail_down=pygame.transform.scale(self.tail_down,(cell_size,cell_size))
        self.tail_right=pygame.image.load('tail_right.png').convert_alpha()
        self.tail_right=pygame.transform.scale(self.tail_right,(cell_size,cell_size))
        self.tail_left=pygame.image.load('tail_left.png').convert_alpha()
        self.tail_left=pygame.transform.scale(self.tail_left,(cell_size,cell_size))
        self.body_vertical=pygame.image.load('body_vertical.png').convert_alpha()
        self.body_vertical=pygame.transform.scale(self.body_vertical,(cell_size,cell_size))
        self.body_horizontal=pygame.image.load('body_horizontal.png').convert_alpha()
        self.body_horizontal=pygame.transform.scale(self.body_horizontal,(cell_size,cell_size))
        self.body_tr=pygame.image.load('body_tr.png').convert_alpha()
        self.body_tr=pygame.transform.scale(self.body_tr,(cell_size,cell_size))
        self.body_tl=pygame.image.load('body_tl.png').convert_alpha()
        self.body_tl=pygame.transform.scale(self.body_tl,(cell_size,cell_size))
        self.body_br=pygame.image.load('body_br.png').convert_alpha()
        self.body_br=pygame.transform.scale(self.body_br,(cell_size,cell_size))
        self.body_bl=pygame.image.load('body_bl.png').convert_alpha()
        self.body_bl=pygame.transform.scale(self.body_bl,(cell_size,cell_size))
        self.crunch_sound=pygame.mixer.Sound('cat_meow.MP3')
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            block__rect=pygame.Rect(int(block.x*cell_size),int(block.y*cell_size), cell_size, cell_size)
            if index==0:
                screen.blit(self.head,block__rect)
            elif index==len(self.body)-1:
                screen.blit(self.tail,block__rect)
            else:
                previous_block=self.body[index+1]-block
                next_block=self.body[index-1]-block
                body_relation=next_block-previous_block
                if previous_block.x==next_block.x:
                    screen.blit(self.body_vertical, block__rect)
                if previous_block.y==next_block.y:
                    screen.blit(self.body_horizontal, block__rect)
                else:
                    if previous_block.x== -1 and next_block.y== -1 or previous_block.y== -1 and next_block.x== -1:
                        screen.blit(self.body_tl, block__rect)
                    if previous_block.x== -1 and next_block.y== 1 or previous_block.y== 1 and next_block.x== -1:
                        screen.blit(self.body_bl, block__rect)
                    if previous_block.x== 1 and next_block.y== -1 or previous_block.y== -1 and next_block.x== 1:
                        screen.blit(self.body_tr, block__rect)
                    if previous_block.x== 1 and next_block.y== 1 or previous_block.y== 1 and next_block.x== 1:
                        screen.blit(self.body_br, block__rect)

    def update_tail_graphics(self):
        tail_relation=self.body[-2]-self.body[-1]
        if tail_relation==Vector2(1,0):
            self.tail=self.tail_right     
        elif tail_relation==Vector2(-1,0):
            self.tail=self.tail_left
        elif tail_relation==Vector2(0,1):
            self.tail=self.tail_down
        elif tail_relation==Vector2(0,-1):
            self.tail=self.tail_up

    def update_head_graphics(self):
        head_relation=self.body[1]-self.body[0]
        if head_relation==Vector2(1,0):
            self.head=self.head_left
        elif head_relation==Vector2(-1,0):
            self.head=self.head_right
        elif head_relation==Vector2(0,1):
            self.head=self.head_up
        elif head_relation==Vector2(0,-1):
            self.head=self.head_down
    def move_snake(self):
        if (self.next_direction.x != -self.direction.x or self.next_direction.y != -self.direction.y):
            self.direction = self.next_direction
        if self.new_block==True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy
            self.new_block=False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy
    def add_block(self):
        self.new_block=True
    def play_crunch_sound(self):
        self.crunch_sound.play()
    def reset(self):
        self.body=[Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction=Vector2(1,0)
        self.next_direction = Vector2(1, 0)

class FRUIT:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        fruit_rect=pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size), cell_size, cell_size)
        screen.blit(apple,fruit_rect)

    def randomize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x,self.y)
class MAIN:
    def __init__(self):
        self.snake=SNAKE()
        self.fruit=FRUIT()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake() 
        self.draw_score()
    def check_collision(self):
        if self.fruit.pos==self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
        for block in self.snake.body[1:]:
            if block==self.fruit.pos:
                self.fruit.randomize()
    def check_fail(self):
        if not 0 <=self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0 <=self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        self.snake.reset()
    def draw_grass(self):
        grass_color=(144,213,255)
        for row in range(cell_number):
            if row%2==0:
                for col in range(cell_number):
                    if col%2==0:
                        grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col%2!=0:
                        grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    def draw_score(self):
        score_text=str(len(self.snake.body)-3)
        font=pygame.font.Font('Carnevalee Freakshow.ttf',25)
        score_surface=font.render(score_text,True,(56,74,12))
        score_x=cell_size*cell_number-60
        score_y=cell_size*cell_number-40
        score_rect=score_surface.get_rect(center=(score_x,score_y))
        apple_rect=apple.get_rect(midright=(score_rect.left-5,score_rect.centery))
        bg_rect=pygame.Rect(apple_rect.left-3,apple_rect.top,apple_rect.width+score_rect.width+15,apple_rect.height)
        pygame.draw.rect(screen,(144,213,255),bg_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()
SCREEN_UPDATE=pygame.USEREVENT
apple=pygame.image.load('shrimp.png').convert_alpha()
apple=pygame.transform.scale(apple,(cell_size,cell_size))
pygame.time.set_timer(SCREEN_UPDATE,150)
main_game=MAIN()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==SCREEN_UPDATE:
           main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.next_direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.next_direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.next_direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.next_direction = Vector2(1, 0)
    screen.fill((210, 236, 255))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

