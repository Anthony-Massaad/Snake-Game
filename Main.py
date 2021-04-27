import pygame
import Snake
import Food
# Could have made it look a lot nicer and all but at this point, my main project (which was snake in my implementation way) was done
# So I just left it to what it is

pygame.init()
gameWidth = 573
gameHeight = 573
CONST = 13
display = pygame.display.set_mode((gameWidth, gameHeight))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
snakeBody = Snake.Snake(display)
snakeFood = Food.Food(display)


def drawGrid():
    x = 0
    y = 0
    rows = 23
    trueGameWidth = gameWidth - CONST
    distance = trueGameWidth // rows
    for i in range(rows):
        x += distance
        y += distance
        pygame.draw.line(display, WHITE, (x, distance), (x, trueGameWidth - distance + 15))
        pygame.draw.line(display, WHITE, (distance, y), (trueGameWidth - distance + 15, y))


def draw():
    global score
    display.fill(BLACK)
    if snakeBody.lose is False:
        if snakeBody.reset:
            score = 0
            generateSnakeFood(display)
            snakeBody.reset = False
        display.blit(text, (20, 5))
        value = font.render(str(score), True, WHITE)
        display.blit(value, (85, 5))
        drawGrid()
        snakeFood.draw(display)
        snakeBody.draw(display)
    else:
        value = otherScreenFont.render(str(score), True, WHITE)
        display.blit(finalScoreText, (150, 150))
        display.blit(value, (340, 152))
        display.blit(restartText, (110, 230))
    pygame.display.update()


def generateSnakeFood(dsp):
    while True:
        snakeFood.generateFood(dsp)
        if (snakeFood.food[2][0], snakeFood.food[2][1]) not in snakeBody.coordinateSwitch:
            break


font = pygame.font.SysFont('Arial', 15)
otherScreenFont = pygame.font.SysFont('Arial', 35)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
score = 0
displayScore = "SCORE: "
restart = "Press 'R' to replay the game..."
text = font.render(displayScore, True, WHITE)
restartText = otherScreenFont.render(restart, True, WHITE)
finalScore = 'Final Score is '
finalScoreText = otherScreenFont.render(finalScore, True, WHITE)
run = True
while run:
    pygame.time.delay(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    headX, headY, headW, headH = snakeBody.snake[0][2]
    foodX, foodY, foodW, foodH = snakeFood.food[2]

    if headX < foodX + headW and headX + foodW > foodX and headY < foodY + headH and headH + headY > foodY:
        snakeBody.addBody(display)
        generateSnakeFood(display)
        score += 1

    snakeBody.snakeControls(display)
    draw()


pygame.quit()
