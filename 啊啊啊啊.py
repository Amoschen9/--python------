# -*- coding: utf-8 -*
import pygame
import sys
import random
import numpy as np
import sys
import traceback
import copy
from pygame.locals import *
import pygame.gfxdraw


pygame.init()
g_map = []
g_map = [[0 for y in range(15)] for x in range(15)]  # 当前的棋盘

# 控制结束
running = True
# 控制顺序
turn = True


# 判断是否结束
def game_result():
    """判断游戏的结局。0为游戏进行中，1为黑子获胜，2为白子获胜，3为平局"""
    # 1. 判断是否横向连续五子
    global g_map
    for x in range(11):
        for y in range(15):
            if g_map[x][y] == 1 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 1 and g_map[x + 3][y] == 1 and \
                    g_map[x + 4][y] == 1:
                return 1
            if g_map[x][y] == 2 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 2 and g_map[x + 3][y] == 2 and \
                    g_map[x + 4][y] == 2:
                return 2

    # 2. 判断是否纵向连续五子
    for x in range(15):
        for y in range(11):
            if g_map[x][y] == 1 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][y + 3] == 1 and g_map[x][
                y + 4] == 1:
                return 1
            if g_map[x][y] == 2 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][y + 3] == 2 and g_map[x][
                y + 4] == 2:
                return 2

    # 3. 判断是否有左上-右下的连续五子
    for x in range(11):
        for y in range(11):
            if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                y + 3] == 1 and g_map[x + 4][y + 4] == 1:
                return 1
            if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                y + 3] == 2 and g_map[x + 4][y + 4] == 2:
                return 2

    # 4. 判断是否有右上-左下的连续五子
    for x in range(11):
        for y in range(11):
            if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 1][
                y + 3] == 1 and g_map[x][y + 4] == 1:
                return 1
            if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 1][
                y + 3] == 2 and g_map[x][y + 4] == 2:
                return 2

    # 5. 判断是否结束
    for x in range(15):
        for y in range(15):
            if g_map[x][y] == 0:  # 棋盘中还有剩余的格子，不能判断为平局
                return 0

    # 6.判断是否平局
    for x in range(15):
        for y in range(15):
            if g_map[x][y] != 0:
                return 3


# 绘制棋盘
def Draw_chessboard(screen):
    screen.fill([201, 202, 187])
    for i in range(15):
        pygame.draw.line(screen, (0, 0, 0), (40 * (i + 1), 40), (40 * (i + 1), 600), 2)  # 画横线
    for i in range(15):
        pygame.draw.line(screen, (0, 0, 0), (40, 40 * (i + 1)), (600, 40 * (i + 1)), 2)  # 画竖线
    pygame.draw.circle(screen, (0, 0, 0), [320, 320], 5)
    pygame.draw.circle(screen, (0, 0, 0), [200, 200], 5)
    pygame.draw.circle(screen, (0, 0, 0), [440, 440], 5)
    pygame.draw.circle(screen, (0, 0, 0), [200, 440], 5)
    pygame.draw.circle(screen, (0, 0, 0), [440, 200], 5)


# 绘制棋子
def Draw_chess(screen, x, y, cur_step):
    if cur_step == 1:
        col = (0, 0, 0)
        pygame.gfxdraw.aacircle(screen, 40 * (x + 1), 40 * (y + 1), 15, col)
        pygame.gfxdraw.filled_circle(screen, 40 * (x + 1), 40 * (y + 1), 15, col)
        # 落黑子
    if cur_step == 2:
        col = (255, 255, 255)
        pygame.gfxdraw.aacircle(screen, 40 * (x + 1), 40 * (y + 1), 15, col)
        pygame.gfxdraw.filled_circle(screen, 40 * (x + 1), 40 * (y + 1), 15, col)  # 落白子
    pygame.display.update()


# 显示结果
def text(s, screen):
    s_font = pygame.font.SysFont('SimHei', 40)
    s_text = s_font.render(s, True, (0, 0, 255))
    screen.blit(s_text, (100, 100))
    # 是不断刷新的，每点一次白子和黑子交替显示
    pygame.display.flip()

def button0(screen):
    x_font = pygame.font.Font("aaaaa.TTF", 25)
    text1 = x_font.render("欢迎来到我们的游戏！", True, (0, 0, 0))
    screen.blit(text1, (600, 450))
    text2 = x_font.render("游戏可实现AI训练！", True, (0, 0, 0))
    screen.blit(text2, (600, 480))
    text2 = x_font.render("单击棋盘即可开始！", True, (0, 0, 0))
    screen.blit(text2, (600, 510))
    text3 = x_font.render("伴随音乐~", True, (0, 0, 0))
    screen.blit(text3, (600, 540))
    text2 = x_font.render("祝你成功哦~", True, (0, 0, 0))
    screen.blit(text2, (600, 570))



t = True
def AI_analysis():
    global g_map
    value = [[0 for y in range(15)] for x in range(15)]  # 计算每个落点价值
    for i in range(15):
        for j in range(15):
            if g_map[i][j] == 0:
                g_map[i][j] = 1  # 假设电脑落子

                # 五子
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 1 and g_map[x + 3][
                            y] == 1 and g_map[x + 4][y] == 1:
                            value[i][j] = 1000000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1:
                            value[i][j] = 1000000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1:
                            value[i][j] = 1000000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and \
                                g_map[x + 1][y + 3] == 1 and g_map[x][y + 4] == 1:
                            value[i][j] = 1000000

                # 活四
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 200000
                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 1 and g_map[x + 3][y] == 1 and g_map[x + 2][
                            y] == 1 and g_map[x + 1][y] == 1 and g_map[x][y] == 0:
                            value[i][j] += 200000
                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 200000
                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 200000

                # 冲四
                # （1）
                for x in range(10):
                    for y in range(15):
                        if g_map[x][y] == 0 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 1 and g_map[x + 3][
                            y] == 1 and g_map[x + 4][y] == 1 and g_map[x + 5][y] == 2:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 1 and g_map[x + 3][
                            y] == 1 and g_map[x + 4][y] == 1 and g_map[x + 5][y] == 0:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 2:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 40000

                # （2）
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 1 and g_map[x + 3][
                            y] == 1 and g_map[x + 4][y] == 1:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and \
                                g_map[x + 1][y + 3] == 1 and g_map[x][y + 4] == 1:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 1 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 1:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 1:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and \
                                g_map[x + 1][y + 3] == 0 and g_map[x][y + 4] == 1:
                            value[i][j] += 40000

                # （3）
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 1 and g_map[x + 4][y] == 1:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 1 and g_map[x][y + 4] == 1:
                            value[i][j] += 40000

                # 活三
                # (1)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 0 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 1 and g_map[x + 3][
                            y] == 1 and g_map[x + 4][y] == 0:
                            value[i][j] += 20000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 0:
                            value[i][j] += 20000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 0:
                            value[i][j] += 20000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 0 and g_map[x + 3][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and \
                                g_map[x + 1][y + 3] == 1 and g_map[x][y + 4] == 0:
                            value[i][j] += 20000

                # (2)
                for x in range(12):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 1 and g_map[x + 3][y] == 1:
                            value[i][j] += 20000

                for x in range(15):
                    for y in range(12):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 1 and g_map[x][y + 3] == 1:
                            value[i][j] += 20000

                for x in range(12):
                    for y in range(12):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1:
                            value[i][j] += 20000

                for x in range(11):
                    for y in range(12):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and \
                                g_map[x + 1][y + 3] == 1:
                            value[i][j] += 20000

                for x in range(12):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 0 and g_map[x + 3][y] == 1:
                            value[i][j] += 20000

                for x in range(15):
                    for y in range(12):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 0 and g_map[x][y + 3] == 1:
                            value[i][j] += 20000

                for x in range(12):
                    for y in range(12):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 1:
                            value[i][j] += 20000

                for x in range(11):
                    for y in range(12):
                        if g_map[x + 4][y] == 0 and g_map[x + 3][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 1:
                            value[i][j] += 20000

                # 眠三
                # (1)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 0 and g_map[x + 3][y] == 1 and g_map[x + 2][
                            y] == 1 and g_map[x + 1][y] == 1 and g_map[x][y] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y] == 1 and g_map[x + 3][y] == 1 and g_map[x + 2][
                            y] == 1 and g_map[x + 1][y] == 0 and g_map[x][y] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                # (2)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(15):
                        if g_map[x][y] == 0 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 1 and g_map[x + 4][y] == 1 and g_map[x + 5][y] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][y + 3] == 0 and \
                                g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 1 and g_map[x][y] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 1 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 1 and g_map[x + 5][y] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                # (3)
                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                # (4)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 1 and g_map[x + 4][y] == 1:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 1 and g_map[x][y + 4] == 1:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 1:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 1:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 0 and g_map[x][y + 4] == 1:
                            value[i][j] += 8000

                # (5)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 1 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 1:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 1:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and \
                                g_map[x + 1][y + 3] == 0 and g_map[x][y + 4] == 1:
                            value[i][j] += 8000

                # (6)
                for x in range(9):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 1 and g_map[x + 3][y] == 1 \
                                and g_map[x + 4][y] == 1 and g_map[x + 5][y] == 0 and g_map[x + 6][y] == 2:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(9):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 1 and g_map[x][y + 3] == 1 \
                                and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 0 and g_map[x][y + 6] == 2:
                            value[i][j] += 8000

                for x in range(9):
                    for y in range(9):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 \
                                and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 0 and g_map[x + 6][y + 6] == 2:
                            value[i][j] += 8000

                for x in range(9):
                    for y in range(9):
                        if g_map[x + 6][y] == 2 and g_map[x + 5][y + 1] == 0 and g_map[x + 4][y + 2] == 1 and \
                                g_map[x + 3][y + 3] == 1 \
                                and g_map[x + 2][y + 4] == 1 and g_map[x + 1][y + 5] == 0 and g_map[x][y + 6] == 2:
                            value[i][j] += 8000

                # 活二
                # (1)
                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5600
                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5600
                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5600
                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5600
                # (2)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 0 and g_map[x + 1][y] == 1 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 1 and g_map[x + 4][y] == 0:
                            value[i][j] += 5600

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 0:
                            value[i][j] += 5600

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 0:
                            value[i][j] += 5600

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 0 and g_map[x + 3][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 1 and g_map[x][y + 4] == 0:
                            value[i][j] += 5600
                # (3)
                for x in range(12):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 0 and g_map[x + 3][y] == 1:
                            value[i][j] += 5600

                for x in range(15):
                    for y in range(12):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 0 and g_map[x][y + 3] == 1:
                            value[i][j] += 5600

                for x in range(12):
                    for y in range(12):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 1:
                            value[i][j] += 5600

                for x in range(11):
                    for y in range(12):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 1:
                            value[i][j] += 5600

                # 眠二
                # (1)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 5000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 0 and g_map[x + 3][y] == 0 and g_map[x + 2][
                            y] == 1 and g_map[x + 1][y] == 1 and g_map[x][y] == 2:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y] == 1 and g_map[x + 3][y] == 1 and g_map[x + 2][
                            y] == 0 and g_map[x + 1][y] == 0 and g_map[x][y] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 2:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                # (2)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 1 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 5000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 1 and g_map[x][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 0 and g_map[x + 3][y] == 1 and g_map[x + 2][
                            y] == 0 and g_map[x + 1][y] == 1 and g_map[x][y] == 2:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y] == 1 and g_map[x + 3][y] == 0 and g_map[x + 2][
                            y] == 1 and g_map[x + 1][y] == 0 and g_map[x][y] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 1 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 2:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 1 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 1 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 1 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                # (3)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 5000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 1 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 1 and g_map[x + 3][y] == 0 and g_map[x + 2][
                            y] == 0 and g_map[x + 1][y] == 1 and g_map[x][y] == 2:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y] == 1 and g_map[x + 3][y] == 0 and g_map[x + 2][
                            y] == 0 and g_map[x + 1][y] == 1 and g_map[x][y] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 2:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 1 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 2:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 2 and g_map[x + 4][y + 1] == 1 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 1 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000
                # (4)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 1:
                            value[i][j] += 5000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 1:
                            value[i][j] += 5000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 1:
                            value[i][j] += 5000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 1 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 0 and g_map[x][y + 4] == 1:
                            value[i][j] += 5000

                g_map[i][j] = 0  # 撤销假设

                g_map[i][j] = 2  # 假设玩家落子

                # 五子
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 2 and g_map[x + 3][
                            y] == 2 and g_map[x + 4][y] == 2:
                            value[i][j] = 1000000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2:
                            value[i][j] = 1000000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2:
                            value[i][j] = 1000000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and \
                                g_map[x + 1][y + 3] == 2 and g_map[x][y + 4] == 2:
                            value[i][j] = 1000000

                # 活四
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 200000
                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 2 and g_map[x + 3][y] == 2 and g_map[x + 2][
                            y] == 2 and g_map[x + 1][y] == 2 and g_map[x][y] == 0:
                            value[i][j] += 200000
                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 200000
                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 200000

                # 冲四
                # （1）
                for x in range(10):
                    for y in range(15):
                        if g_map[x][y] == 0 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 2 and g_map[x + 3][
                            y] == 2 and g_map[x + 4][y] == 2 and g_map[x + 5][y] == 1:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 2 and g_map[x + 3][
                            y] == 2 and g_map[x + 4][y] == 2 and g_map[x + 5][y] == 0:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 1:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 40000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 40000

                # （2）
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 2 and g_map[x + 3][
                            y] == 2 and g_map[x + 4][y] == 2:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and \
                                g_map[x + 1][y + 3] == 2 and g_map[x][y + 4] == 2:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 2 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 2:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 2:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and \
                                g_map[x + 1][y + 3] == 0 and g_map[x][y + 4] == 2:
                            value[i][j] += 40000

                # （3）
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 2 and g_map[x + 4][y] == 2:
                            value[i][j] += 40000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2:
                            value[i][j] += 40000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 2 and g_map[x][y + 4] == 2:
                            value[i][j] += 40000

                # 活三
                # (1)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 0 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 2 and g_map[x + 3][
                            y] == 2 and g_map[x + 4][y] == 0:
                            value[i][j] += 20000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 0:
                            value[i][j] += 20000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 0:
                            value[i][j] += 20000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 0 and g_map[x + 3][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and \
                                g_map[x + 1][y + 3] == 2 and g_map[x][y + 4] == 0:
                            value[i][j] += 20000

                # (2)
                for x in range(12):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 2 and g_map[x + 3][y] == 2:
                            value[i][j] += 20000

                for x in range(15):
                    for y in range(12):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 2 and g_map[x][y + 3] == 2:
                            value[i][j] += 20000

                for x in range(12):
                    for y in range(12):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2:
                            value[i][j] += 20000

                for x in range(11):
                    for y in range(12):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and \
                                g_map[x + 1][y + 3] == 2:
                            value[i][j] += 20000

                for x in range(12):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 0 and g_map[x + 3][y] == 2:
                            value[i][j] += 20000

                for x in range(15):
                    for y in range(12):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 0 and g_map[x][y + 3] == 2:
                            value[i][j] += 20000

                for x in range(12):
                    for y in range(12):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 2:
                            value[i][j] += 20000

                for x in range(11):
                    for y in range(12):
                        if g_map[x + 4][y] == 0 and g_map[x + 3][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 2:
                            value[i][j] += 20000

                # 眠三
                # (1)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 0 and g_map[x + 3][y] == 2 and g_map[x + 2][
                            y] == 2 and g_map[x + 1][y] == 2 and g_map[x][y] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y] == 2 and g_map[x + 3][y] == 2 and g_map[x + 2][
                            y] == 2 and g_map[x + 1][y] == 0 and g_map[x][y] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                # (2)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(15):
                        if g_map[x][y] == 0 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 2 and g_map[x + 4][y] == 2 and g_map[x + 5][y] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][y + 3] == 0 and \
                                g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 2 and g_map[x][y] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 2 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 2 and g_map[x + 5][y] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                # (3)
                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 8000

                # (4)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 2 and g_map[x + 4][y] == 2:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 2 and g_map[x][y + 4] == 2:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 2:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 2:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 0 and g_map[x][y + 4] == 2:
                            value[i][j] += 8000

                # (5)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 2 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 2:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 2:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2:
                            value[i][j] += 8000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and \
                                g_map[x + 1][y + 3] == 0 and g_map[x][y + 4] == 2:
                            value[i][j] += 8000

                # (6)
                for x in range(9):
                    for y in range(15):
                        if g_map[x][y] == 1 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 2 and g_map[x + 3][y] == 2 \
                                and g_map[x + 4][y] == 2 and g_map[x + 5][y] == 0 and g_map[x + 6][y] == 1:
                            value[i][j] += 8000

                for x in range(15):
                    for y in range(9):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 2 and g_map[x][y + 3] == 2 \
                                and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 0 and g_map[x][y + 6] == 1:
                            value[i][j] += 8000

                for x in range(9):
                    for y in range(9):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 \
                                and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 0 and g_map[x + 6][y + 6] == 1:
                            value[i][j] += 8000

                for x in range(9):
                    for y in range(9):
                        if g_map[x + 6][y] == 1 and g_map[x + 5][y + 1] == 0 and g_map[x + 4][y + 2] == 2 and \
                                g_map[x + 3][y + 3] == 2 \
                                and g_map[x + 2][y + 4] == 2 and g_map[x + 1][y + 5] == 0 and g_map[x][y + 6] == 1:
                            value[i][j] += 8000

                # 活二
                # (1)
                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5600
                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5600
                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5600
                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5600
                # (2)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 0 and g_map[x + 1][y] == 2 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 2 and g_map[x + 4][y] == 0:
                            value[i][j] += 5600

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 0:
                            value[i][j] += 5600

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 0:
                            value[i][j] += 5600

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 0 and g_map[x + 3][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 2 and g_map[x][y + 4] == 0:
                            value[i][j] += 5600
                # (3)
                for x in range(12):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 0 and g_map[x + 3][y] == 2:
                            value[i][j] += 5600

                for x in range(15):
                    for y in range(12):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 0 and g_map[x][y + 3] == 2:
                            value[i][j] += 5600

                for x in range(12):
                    for y in range(12):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 2:
                            value[i][j] += 5600

                for x in range(11):
                    for y in range(12):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 2:
                            value[i][j] += 5600

                # 眠二
                # (1)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 5000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 0 and g_map[x + 3][y] == 0 and g_map[x + 2][
                            y] == 2 and g_map[x + 1][y] == 2 and g_map[x][y] == 1:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y] == 2 and g_map[x + 3][y] == 2 and g_map[x + 2][
                            y] == 0 and g_map[x + 1][y] == 0 and g_map[x][y] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 1:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                # (2)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 2 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 5000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 2 and g_map[x][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 0 and g_map[x + 3][y] == 2 and g_map[x + 2][
                            y] == 0 and g_map[x + 1][y] == 2 and g_map[x][y] == 1:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y] == 2 and g_map[x + 3][y] == 0 and g_map[x + 2][
                            y] == 2 and g_map[x + 1][y] == 0 and g_map[x][y] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 2 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 1:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 2 and g_map[x + 4][y + 4] == 0 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 0 and g_map[x + 3][y + 2] == 2 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 2 and g_map[x + 1][y + 4] == 0 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                # (3)
                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 5000

                for x in range(15):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x][y + 1] == 2 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y] == 2 and g_map[x + 3][y] == 0 and g_map[x + 2][
                            y] == 0 and g_map[x + 1][y] == 2 and g_map[x][y] == 1:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(15):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y] == 2 and g_map[x + 3][y] == 0 and g_map[x + 2][
                            y] == 0 and g_map[x + 1][y] == 2 and g_map[x][y] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 0 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 1:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x][y] == 1 and g_map[x + 1][y + 1] == 2 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2 and g_map[x + 5][y + 5] == 0:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 0 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 1:
                            value[i][j] += 5000

                for x in range(10):
                    for y in range(10):
                        if g_map[x + 5][y] == 1 and g_map[x + 4][y + 1] == 2 and g_map[x + 3][y + 2] == 0 and \
                                g_map[x + 2][y + 3] == 0 and g_map[x + 1][y + 4] == 2 and g_map[x][y + 5] == 0:
                            value[i][j] += 5000
                # (4)
                for x in range(11):
                    for y in range(15):
                        if g_map[x][y] == 2 and g_map[x + 1][y] == 0 and g_map[x + 2][y] == 0 and g_map[x + 3][
                            y] == 0 and g_map[x + 4][y] == 2:
                            value[i][j] += 5000

                for x in range(15):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x][y + 1] == 0 and g_map[x][y + 2] == 0 and g_map[x][
                            y + 3] == 0 and g_map[x][y + 4] == 2:
                            value[i][j] += 5000

                for x in range(11):
                    for y in range(11):
                        if g_map[x][y] == 2 and g_map[x + 1][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and g_map[x + 3][
                            y + 3] == 0 and g_map[x + 4][y + 4] == 2:
                            value[i][j] += 5000

                for x in range(11):
                    for y in range(11):
                        if g_map[x + 4][y] == 2 and g_map[x + 3][y + 1] == 0 and g_map[x + 2][y + 2] == 0 and \
                                g_map[x + 1][y + 3] == 0 and g_map[x][y + 4] == 2:
                            value[i][j] += 5000
                g_map[i][j] = 0  # 撤销假设

    temp, m, n = 0, 0, 0
    for i in range(15):
        for j in range(15):
            if value[i][j] >= temp:
                temp = value[i][j]
                m, n = i, j
    if temp == 0:
        p, q = random.randint(0, 14), random.randint(0, 14)
        while g_map[p][q] != 0:
            p, q = random.randint(0, 14), random.randint(0, 14)
            m, n = p, q
    return m, n


def main():
    pygame.mixer.music.load("beijing.wav")  # 载入音乐
    pygame.mixer.music.set_volume(0.2)  # 设置音量为 0.2
    pygame.mixer.music.play()  # 播放音乐
    global running, turn, g_map
    screen = pygame.display.set_mode([850, 650])
    # 定义窗口名字
    pygame.display.set_caption("五子棋小游戏")
    # 在窗口画出棋盘
    Draw_chessboard(screen)
    pygame.display.flip()
    clock = pygame.time.Clock()
    button0(screen)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
            if running:
                if turn:

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # 按下的是鼠标左键
                            x, y = event.pos[0], event.pos[1]
                            # 点击棋盘相应位置
                            if (25 <= x <= 615 and 25 <= y <= 615) and (x % 40 <= 15 or x % 40 >= 25) and (y % 40 <= 15 or y % 40 >= 25) and running:
                                # 在棋盘相应位置落相应颜色棋子
                                x = int((x + 15) // 40) - 1
                                y = int((y + 15) // 40) - 1
                                cur_step = 2
                                Draw_chess(screen, x, y, cur_step)

                                g_map[x][y] = cur_step
                                turn = not turn

                else:
                    cur_step = 1
                    m, n = AI_analysis()
                    Draw_chess(screen, m, n, cur_step)
                    g_map[m][n] = cur_step
                    turn = not turn

                res = game_result()

                if res == 1:
                    text("黑胜", screen)
                    running = False
                elif res == 2:
                    text("白胜", screen)
                    running = False
                elif res == 3:
                    text("平局", screen)
                    running = False

                pygame.display.flip()


        clock.tick(60)


if __name__ == "__main__":
    main()


