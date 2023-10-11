import pygame
import sys
from pygame.math import Vector2
import random

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grid()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.score += 1

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def draw_grid(self):
        for x in range(cell_number):
            for y in range(cell_number):
                if (x + y) % 2 == 0:
                    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, (0, 0, 0), rect)  

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (0, 255, 0), block_rect)  

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (255, 0, 0), fruit_rect)  

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

pygame.init()
cell_size = 40
cell_number = 15
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

game = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.snake.direction.y != 1:
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction.y != -1:
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.snake.direction.x != 1:
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.direction.x != -1:
                game.snake.direction = Vector2(1, 0)

    screen.fill((34, 34, 34)) 
    game.draw_elements()
    pygame.display.update()
    clock.tick(60)  

