import pygame
import random
from pygame.locals import *
from math import sin, cos, atan2, radians

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
FRAME = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
GRAY1 = (102, 102, 102)
GRAY2 = (153,153,153)
GRAY3 = (204, 204, 204)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Consolas", 30)

running = True

clock = pygame.time.Clock()

reg0 = [(0,0),(2.6,0),(3.0,2),(3.8,-2),(4.6,2),(5.4,-2),(6.2,2),(7.0,-2),(7.4,0),(10,0)]
reg0 = list(map(lambda x: (x[0], x[1]*0.3), reg0))

reg1 = [(0,0),(1, 5),(2.6,5),(3.0,7),(3.8,3),(4.6,7),(5.4,3),(6.2,7),(7.0,3),(7.4,5),(9,5), (10, 0)]
reg1 = list(map(lambda x: (x[0], x[1]*0.5), reg1))

reg2 = [(0,0),(1,-5),(2.6,-5),(3.0,-3),(3.8,-7),(4.6,-3),(5.4,-7),(6.2,-3),(7.0,-7),(7.4,-5),(9,-5),(10,0)]
reg2 = list(map(lambda x: (x[0], x[1]*0.5), reg2))

reg3 = [(0,0),(2,0),(2, 5),(2.6,5),(3.0,7),(3.8,3),(4.6,7),(5.4,3),(6.2,7),(7.0,3),(7.4,5),(8,5), (8,0),(10, 0)]
reg3 = list(map(lambda x: (x[0], x[1]*0.3), reg3))

reg4 = [(0,0),(2,0),(2,-5),(2.6,-5),(3.0,-3),(3.8,-7),(4.6,-3),(5.4,-7),(6.2,-3),(7.0,-7),(7.4,-5),(8,-5),(8,0),(10,0)]
reg4 = list(map(lambda x: (x[0], x[1]*0.3), reg4))

reg5 = [(0,0),(2,0),(2, 10),(2.6,10),(3.0,12),(3.8,8),(4.6,12),(5.4,8),(6.2,12),(7.0,8),(7.4,10),(8,10), (8,0),(10, 0)]
reg5 = list(map(lambda x: (x[0], x[1]*0.3), reg5))

reg6 = [(0,0),(2,0),(2,-10),(2.6,-10),(3.0,-8),(3.8,-12),(4.6,-8),(5.4,-12),(6.2,-8),(7.0,-12),(7.4,-10),(8,-10),(8,0),(10,0)]
reg6 = list(map(lambda x: (x[0], x[1]*0.3), reg6))

reg7 = [(0,0),(2,0),(2,-15),(2.6,-15),(3.0,-13),(3.8,-17),(4.6,-13),(5.4,-17),(6.2,-13),(7.0,-17),(7.4,-15),(8,-15),(8,0),(10,0)]
reg7 = list(map(lambda x: (x[0], x[1]*0.3), reg7))


def rotate(dot:tuple, angle:float)->tuple:
    return (dot[0]*cos(angle) - dot[1]*sin(angle), dot[0]*sin(angle)+dot[1]*cos(angle))

def draw_lines(dot_list:list):
    for i in range(len(dot_list)-1):
        pygame.draw.line(display, BLACK, dot_list[i], dot_list[i+1], 3)

i = 0
class Dot:
    def __init__(self, x, y, color = BLACK, type = 0):
        global i
        self.index = i
        i += 1
        self.x = x
        self.y = y
        self.size = 5
        self.color = color
        self.connected_dot = []
        self.movement = []
        self.type = type
        
    
    def update(self):
        display.blit(font.render(f"{self.index}", True, BLACK), (self.x+10, self.y+20))
        if self.movement:  
            self.x += self.movement[-1][0]
            self.y += self.movement[-1][1]
            self.movement.pop()
        pygame.draw.circle(display, self.color, (self.x, self.y), self.size)
        
    def move(self, target_pos, frame = 120):
        for i in range(frame):
            self.movement.append([(target_pos[0]-self.x)/frame, (target_pos[1]-self.y)/frame])

class Segment:
    def __init__(self, start_dot, end_dot, type = 0):
        self.start = start_dot
        self.end = end_dot
        self.type = type
    
    def update(self):
        dot1, dot2 = dots[self.start], dots[self.end]
        theta = atan2(dot2.y - dot1.y, dot2.x - dot1.x)
        distance = ((dot2.x-dot1.x)**2+(dot2.y-dot1.y)**2)**0.5
        reg = [reg0, reg1, reg2, reg3, reg4, reg5, reg6, reg7][self.type]
        drawing = list(map(rotate, reg, [theta]*len(reg)))
        drawing = list(map(lambda x: (x[0]*(distance/10) + dot1.x, x[1]*(distance/10) + dot1.y), drawing))
        draw_lines(drawing)


# dots = [Dot(500, 100), Dot(800, 100), Dot(300,300), Dot(600,300), Dot(500,400), Dot(800,400), Dot(300,600), Dot(600,600)]
# segments = [Segment(0, 1),Segment(0,2),Segment(1,3),Segment(2,3),Segment(0,4),Segment(1,5),
#             Segment(2,6),Segment(3,7),Segment(6,7),Segment(4,6),Segment(5,7),Segment(4,5)]

# dots = [Dot(500, 500), Dot(820, 620), Dot(900, 400), Dot(700, 200)]
# segments = [Segment(0,1), Segment(1,2), Segment(2,3), Segment(3,1), Segment(0,3), Segment(0,2)]

dots = [Dot(500,400), Dot(670, 370), Dot(900, 400), Dot(730, 430), Dot(700, 170), Dot(700, 610)]
segments = [Segment(0,1), Segment(1,2), Segment(2,3), Segment(3,0), 
            Segment(4,0), Segment(4,1), Segment(4,2), Segment(4,3), 
            Segment(5,0), Segment(5,1), Segment(5,2), Segment(5,3)]

lineb = False

while running:
    screen.fill((255,255,255))
    display.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_1:
                dots[0].move([300,100])
                dots[4].move([300,600])
                dots[5].move([800,600])
                dots[2].move([450,250])
                dots[3].move([650,250])
                dots[6].move([450,450])
                dots[7].move([650,450])

            if event.key == K_2:
                #dots[1].move([550,350])
                dots[3].move([550,350])
                #dots[4].move([550,350])
                dots[6].move([550,350])
            
            if event.key == K_3:
                for i in [3, 6]:
                    dots[i].color = pygame.Color("red")
                for i in [1, 4]:
                    dots[i].color = pygame.Color("Green")
                lineb = True
            
            if event.key == K_4:
                lineb = False
                segments[3].type = 2
                segments[6].type = 1
                #segments[0].type = 2
                #segments[4].type = 1
                segments[7].type = 2
                segments[8].type = 1
                #segments[5].type = 2
                #segments[11].type = 1
            
            if event.key == K_5:
                dots[0].move([300,200])
                dots[2].move([300,600])
                dots[5].move([1100, 200])
                dots[7].move([1100,600])
                dots[1].move([700,200])
                dots[4].move([700,200])
                dots[3].move([700,600])
                dots[6].move([700,600])

            if event.key == K_6:
                segments[0].type = 4
                segments[2].type = 3
                segments[3].type = 3
                segments[4].type = 3
                segments[5].type = 3
                segments[6].type = 4
                segments[7].type = 4
                segments[8].type = 3
                segments[9].type = 4
                segments[11].type = 4

            if event.key == K_7:
                del segments[9]
                del segments[2]

            if event.key == K_8:
                dots[0].move([300,200])
                dots[4].move([300,600])
                dots[3].move([1100, 200])
                dots[7].move([1100,600])
                dots[1].move([700,200])
                dots[2].move([700,200])
                dots[5].move([700,600])
                dots[6].move([700,600])

            if event.key == K_9:
                segments[0].type = 4
                segments[1].type = 3
                segments[2].type = 4
                segments[3].type = 3
                segments[5].type = 3
                segments[6].type = 4
                segments[8].type = 3
                segments[9].type = 3
                segments[10].type = 4
                segments[11].type = 4

            if event.key == K_q:
                dots[0].move([100, 400])
                [dots[i].move([500, 400]) for i in [1,2,4]]
                [dots[i].move([900, 400]) for i in [3,5,6]]
                dots[7].move([1300, 400])
            
            if event.key == K_w:
                segments[0].type = 3
                segments[4].type = 4

                segments[2].type = 7
                segments[3].type = 6
                segments[5].type = 5
                segments[6].type = 4
                segments[9].type = 3

                segments[8].type = 3
                segments[10].type = 4
            
            if event.key == K_e:
                dots[1].move([900,500])
                dots[2].move([700,154])
                dots[3].move([700,385])

            if event.key == K_r:
                del segments[2]
            
            if event.key == K_t:
                dots[0].move([400, 400])
                dots[2].move([1000,400])
                [dots[i].move([700,400]) for i in [1,3,4,5]]

            if event.key == K_y:
                segments[4].type = 5
                segments[0].type = 4
                segments[3].type = 4
                segments[8].type = 6
                segments[6].type = 6
                segments[1].type = 4
                segments[2].type = 4
                segments[10].type = 5

            
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 마우스를 클릭했을 때
            pass

        elif event.type == pygame.MOUSEBUTTONUP:  # 마우스를 땠을 때
            pass

        
        elif event.type == QUIT: # 종료
            running = False
    
    for seg in segments:
        seg.update()
    if lineb:
        pygame.draw.line(display, pygame.Color("blue"), (300, 100), (800, 600), 5)
    for dot in dots:
        dot.update()
    
    screen.blit(display, (0, 0))

    keys = pygame.key.get_pressed()  # 키보드 상태 얻기
    pygame.display.flip()
    clock.tick(FRAME)