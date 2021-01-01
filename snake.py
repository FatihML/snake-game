import pygame, sys, random
from pygame.math import Vector2

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, "red", fruit_rect)
    def randomize(self):
        self.x = int(random.randint(0,cell_number-1))
        self.y = int(random.randint(0,cell_number-1))
        self.pos = Vector2(self.x, self.y)
        
class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,5), Vector2(4,5), Vector2(3,5)]
        self.direction=Vector2(1,0)
        self.new_block = False
    def draw_snake(self):
        
        for block in self.body:
            x_pos= int(block.x*cell_size)
            y_pos= int(block.y*cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size, cell_size)
            pygame.draw.rect(screen,(150,100,50),block_rect)
    def move_snake(self):
        if self.new_block== True:
            copy_body=self.body[:]
            copy_body.insert(0,copy_body[0]+self.direction)
            self.body=copy_body
            self.new_block = False
        else:
            copy_body=self.body[:-1]
            copy_body.insert(0,copy_body[0]+self.direction)
            self.body=copy_body
    def add_block(self):
        self.new_block = True
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):

        if self.snake.body[0]==self.fruit.pos:
            self.snake.add_block()
            self.fruit.randomize()
SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
        
main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = (0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = (0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = (-1,0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = (1,0)
     
    screen.fill((250,200,20))
 
    main_game.draw_elements()
 
    pygame.display.update()
    clock.tick(60) 