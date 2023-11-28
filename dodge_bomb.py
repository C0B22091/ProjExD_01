import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900

delta = {pg.K_UP:(0, -5), pg.K_DOWN:(0, +5), 
         pg.K_LEFT:(-5, 0), pg.K_RIGHT:(+5, 0)}


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    kk_rct = kk_img.get_rect()  # 練習3
    kk_rct.center = 900, 400  # 練習3 こうかとんの初期座標
    bb_img = pg.Surface((20, 20))  # 練習1 透明のSurface
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 練習1 赤い半径10の円を描画
    bb_img.set_colorkey((0, 0, 0))  # 練習1 黒を透過
    img_rct = bb_img.get_rect()  # 練習1
    img_rct.centerx = random.randint(0, WIDTH)  # 練習1
    img_rct.centery = random.randint(0, HEIGHT)  # 練習1
    vx = +5  # 練習2
    vy = +5  # 練習2
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        key_lst = pg.key.get_pressed() # 練習3 こうかとんの総移動距離
        sum_mv = [0, 0]
        for k, tpl in delta.items():
            if key_lst[k]:  # キーが押されたら
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]
        kk_rct.move_ip(sum_mv)

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        img_rct.move_ip((vx, vy))  # 練習2
        screen.blit(bb_img, img_rct)
    
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()