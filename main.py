import pygame #this is how we import the project
from snake import * # this will take the code from snake.py file and incorporate it into the main.py
from food import Food # takes the code from the food.py file and uses it in the main for the food the snake will collect during the game.


pygame.init()
bounds = (300,300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")
# this will make the display screen where the game is played.

block_size = 20
snake = Snake(block_size, bounds) # line 12 and 13 will set the size of the snake.
food = Food(block_size,bounds)
font = pygame.font.SysFont('comicsans',60, True)

run = True # this is the start of are loop which will allow the game to keep going unless someone types 'QUIT'.
while run:
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    snake.steer(Direction.LEFT)
  elif keys[pygame.K_RIGHT]:
    snake.steer(Direction.RIGHT)
  elif keys[pygame.K_UP]:
    snake.steer(Direction.UP)
  elif keys[pygame.K_DOWN]:
    snake.steer(Direction.DOWN)
    
  snake.move()
  snake.check_for_food(food)

  if snake.check_bounds() == True or snake.check_tail_collision() == True:
    text = font.render('Game Over', True, (255,255,255)) # when the snake losses it will say game over
    window.blit(text, (20,120))
    pygame.display.update()
    pygame.time.delay(1000)
    snake.respawn() # snake will come back if it loses and game will restart
    food.respawn() # food will keep appearing after it is ate

  window.fill((0,0,0))
  snake.draw(pygame, window) # takes the code and adds it to the window of the game from the snake.py file
  food.draw(pygame, window) # takes the code and adds it to the window of the game fro the food.py file
  pygame.display.update()
  # this is the end of our loop