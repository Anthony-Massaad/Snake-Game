import pygame

class Snake:
    def __init__(self, display):
        self.velocity = 24
        self.color = (255, 0, 0)
        self.snake = [(display, self.color, [25, 25, 23, 23])]
        self.headDirections = [True, False, False, False]# <- Down, up, left, right
        self.coordinateSwitch = [(25, 25)]
        self.lose = False
        self.reset = True

    def draw(self, display):
        self.coordinateSwitch[0] = (self.snake[0][2][0], self.snake[0][2][1])

        if self.headDirections[0] and self.snake[0][2][1] < 520:
            self.snake[0][2][1] += self.velocity
        elif self.headDirections[1] and self.snake[0][2][1] > 40:
            self.snake[0][2][1] -= self.velocity
        elif self.headDirections[2] and self.snake[0][2][0] > 40:
            self.snake[0][2][0] -= self.velocity
        elif self.headDirections[3] and self.snake[0][2][0] < 520:
            self.snake[0][2][0] += self.velocity
        else:
            self.velocity = 0
            self.lose = True

        pygame.draw.rect(self.snake[0][0], self.snake[0][1], self.snake[0][2])
        if self.velocity != 0:
            for i in range(1, len(self.snake)):
                self.coordinateSwitch[i] = (self.snake[i][2][0], self.snake[i][2][1])
                self.snake[i][2][0] = self.coordinateSwitch[i - 1][0]
                self.snake[i][2][1] = self.coordinateSwitch[i - 1][1]
                pygame.draw.rect(self.snake[i][0], self.snake[i][1], self.snake[i][2])
        else:
            for i in range(1, len(self.snake)):
                self.coordinateSwitch[i] = (self.snake[i][2][0], self.snake[i][2][1])
                self.snake[i][2][0] = self.coordinateSwitch[i][0]
                self.snake[i][2][1] = self.coordinateSwitch[i][1]
                pygame.draw.rect(self.snake[i][0], self.snake[i][1], self.snake[i][2])

        if self.coordinateSwitch[0] in self.coordinateSwitch[1:]:
            self.velocity = 0
            self.lose = True

    def snakeControls(self, display):
        keys = pygame.key.get_pressed()
        if len(self.snake) > 1:
            self.headAndBody(keys)
        else:
            self.justHead(keys)

        if self.lose is True:
            if keys[pygame.K_r]:
                self.velocity = 24
                self.snake = [(display, self.color, [25, 25, 23, 23])]
                self.headDirections = [True, False, False, False]  # <- Down, up, left, right
                self.coordinateSwitch = [(25, 25)]
                self.lose = False
                self.reset = True

    def addBody(self, display):
        self.coordinateSwitch.append((self.snake[-1][2][0], self.snake[-1][2][1]))
        self.snake.append((display, self.color, [self.coordinateSwitch[-2][0], self.coordinateSwitch[-2][1], 23, 23]))

    def justHead(self, keys):
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not self.headDirections[0]:
            for i in range(len(self.headDirections)):
                self.headDirections[i] = False
            self.headDirections[0] = True
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and not self.headDirections[1]:
            for i in range(len(self.headDirections)):
                self.headDirections[i] = False
            self.headDirections[1] = True
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not self.headDirections[2]:
            for i in range(len(self.headDirections)):
                self.headDirections[i] = False
            self.headDirections[2] = True
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not self.headDirections[3]:
            for i in range(len(self.headDirections)):
                self.headDirections[i] = False
            self.headDirections[3] = True

    def headAndBody(self, keys):
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not self.headDirections[0] and not self.headDirections[1]:
            for i in range(len(self.headDirections)):
                self.headDirections[i] = False
            self.headDirections[0] = True
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and not self.headDirections[1] and not self.headDirections[0]:
            for i in range(len(self.headDirections)):
                self.headDirections[i] = False
            self.headDirections[1] = True
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not self.headDirections[2] and not self.headDirections[3]:
            for i in range(len(self.headDirections)):
                self.headDirections[i] = False
            self.headDirections[2] = True
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not self.headDirections[3] and not self.headDirections[2]:
            for i in range(len(self.headDirections)):
                self.headDirections[i] = False
            self.headDirections[3] = True
