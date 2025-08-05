#importing libraries
import pygame
import time
import random
# Initialize Pygame
pygame.init()

# Set up display
#width and height define dimensions
width, height = 800, 600
window = pygame.display.set_mode((width, height))#creates window with specified dimensions
pygame.display.set_caption('BabySnake Game') #setting title

# Colors
#using rgb colours here so yeee, the diff values can     diff colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 , 34)
green = (0, 255, 0)
blue = (50, 153, 213)
darkblue = (50, 100,100)
darkpurple =(102, 0, 204)


# Game variables
snake_block = 10
snake_speed = 20
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

#saving the highest score
def get_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except:
        return 0

def save_high_score(score):
    high_score = get_high_score()
    if score > high_score:
        with open("highscore.txt", "w") as file:
            file.write(str(score))

#drawing the snake, we can change the size and postions 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])

def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    window.blit(value, [0, 0])

def message(msg, color, position):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg,position )

def gameLoop():
    
    game_over = False
    game_close = False
    #postion of snake at start of game
    x1 = width / 2
    y1 = height / 2
    #variables to control the direction of the snakes head
    x1_change = 0
    y1_change = 0

    #size of snake at start
    snake_list = []
    length_of_snake = 1
    score = 0
    high_score = get_high_score()

    #positon of food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
  

    if game_close:
        save_high_score(score)


    border_thickness = 20 
    while not game_over:

        #handling the gameover
        while game_close == True:
            window.fill(darkpurple)# this is for colouring the screen
            #messages on screen
            message("You Lost! Press Q-Quit or P-Play Again", red, [width / 6, height / 3])
            message(f"Your Score: {score}", white, [width / 6, height / 2])
            message(f"High Score: {high_score}", white, [width / 6, height / 2 + 40])
            if score > high_score:
                message("You have the new High Score!", green, [width / 6, height / 2 + 80])
            pygame.display.update()


            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:#to quit the game
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_p:#to play the game
                            gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#closes the game if wndow is closed
                game_over = True
            if event.type == pygame.KEYDOWN:
                #the directions the snake moves in 
                if event.key == pygame.K_a and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        #ends the game if wall hit
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
            #updates the snakes position after dead
        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        show_score(score) 
       
        pygame.display.update()
        #handles the food consumption 
         
        if x1 == foodx and y1 == foody: #checks if the snakes head is on the food
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1 #this is to increase the length of the snake
            score += 10
             
       
        clock.tick(snake_speed)

    save_high_score(score)
    pygame.quit()
    quit()

gameLoop()
