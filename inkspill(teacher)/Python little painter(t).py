# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:02:42 2022

@author: CodingApe_User
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))   #設定600*400視窗
pygame.display.set_caption("Python Draw")     #設定視窗標題


loop = True
press = False

while loop: #任務一：python小畫家
    try:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  
                loop = False
    
        px, py = pygame.mouse.get_pos()                     #取得滑鼠位置
        if pygame.mouse.get_pressed() == (1,0,0):           #按下滑鼠左鍵
            pygame.draw.circle(screen,(255,255,255),(px,py),10)    #繪出白色的半徑10的圓圈
            
        if pygame.mouse.get_pressed() == (0,0,1):           #按下滑鼠右鍵 
            pygame.draw.rect(screen, (0,0,0),(px,py,20,20))        #繪出黑色的寬度20*20的矩形(當橡皮擦)
 
        if event.type == pygame.MOUSEBUTTONUP:              #滑鼠按鍵的事件未被壓下
            press == False
        pygame.display.update()
      
    except Exception as e:
        print(e)
        pygame.quit()
        
pygame.quit()


