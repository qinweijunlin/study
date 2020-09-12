#!/usr/bin/env python3

# 屏蔽 Pygame 的欢迎信息
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'ivan'

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化 Pygame, 设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
