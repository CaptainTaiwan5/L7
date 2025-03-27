# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:02:42 2022

@author: CodingApe_User
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((,))  
pygame.display.set_caption("")    


loop = True
press = False

while loop: #任務一：python小畫家
    try:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  
                loop = False
    
        px, py =                                            #取得滑鼠XY位置
        if pygame. == (1,0,0):                              #按下滑鼠左鍵點擊
            pygame.draw.circle()                            #繪出白色的半徑10的圓圈
         
 
        if event.type == :              #如果滑鼠按鍵事件未被壓下
            press == False
        pygame.display.update()
      
    except Exception as e:
        print(e)
        pygame.quit()
        
pygame.quit()


