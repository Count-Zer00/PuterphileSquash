import pygame

# coordinates for width and height
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 1
FPS = 300


# creating a class for ball
class Ball:
    RADIUS = 20

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, colour):
        global screen
        pygame.draw.circle(screen,
                           colour,
                           (self.x, self.y),
                           self.RADIUS)

    def update(self):
        global bgColor, fgColor

        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER + self.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER + self.RADIUS or newy > HEIGHT-BORDER-self.RADIUS:
            self.vy = -self.vy
        else:
            self.show(bgColor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(fgColor)


class Paddle:
    global bgColor, fgColor

    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, colour):
        global screen
        pygame.draw.rect(screen,
                         colour,
                         pygame.Rect(WIDTH - self.WIDTH,
                                     self.y - self.HEIGHT//2,
                                     self.WIDTH, self.HEIGHT))

    def update(self):
        self.show(pygame.Color("black"))
        self.y = pygame.mouse.get_pos()[1]
        self.show(pygame.Color("white"))


# Drawing main screen
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bgColor = pygame.Color("Black")
fgColor = pygame.Color("white")

pygame.draw.rect(screen,
                 fgColor,
                 pygame.Rect((0, 0), (WIDTH, BORDER)))

pygame.draw.rect(screen,
                 fgColor,
                 pygame.Rect(0, 0, BORDER, HEIGHT))

pygame.draw.rect(screen,
                 fgColor,
                 pygame.Rect(0, HEIGHT - BORDER, WIDTH, BORDER))

ball = Ball(WIDTH - Ball.RADIUS, HEIGHT//2, -VELOCITY, -VELOCITY)
ball.show(fgColor)

paddle = Paddle(HEIGHT//2)
paddle.show(fgColor)

clock = pygame.time.Clock()
# forever loop while keeping window open with the border drawings
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    clock.tick(FPS)

    pygame.display.flip()

    paddle.update()
    ball.update()


pygame.quit()

'''
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not run
            pygame.quit()
'''

