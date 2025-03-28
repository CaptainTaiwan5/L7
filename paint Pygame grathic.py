import pygame
import sys
import math

#隨堂測驗二
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GOLD  = (255, 216,   0)
SILVER= (192, 192, 192)
COPPER= (192, 112,  48)




def main():
    pygame.init()
    pygame.display.set_caption("繪製Pygame圖形")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        
        #隨堂測驗一

        #pygame.draw.line(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)
        pygame.draw.line(screen, BLACK, [0,0], [100,200], 10)
        
        #pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)
        pygame.draw.rect(screen, COPPER, [250,50,120,80])

        #pygame.draw.circle(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
        pygame.draw.circle(screen, GOLD, [600,100], 60)

        #pygame.draw.ellipse(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 線寬)
        pygame.draw.ellipse(screen, RED, (200, 250, 160, 100))
        pygame.draw.ellipse(screen, GREEN, (250, 300, 160, 100))
        pygame.draw.ellipse(screen, BLUE, (300, 350, 160, 100))
        
    
        

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
