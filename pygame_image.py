import os
import sys
import pygame as pg

# 演習課題：作業ディレクトリの設定
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 演習1, 2: 背景画像の読み込みと表示
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) # 演習8: 反転画像を作成

    # 演習3, 4: こうかとん画像の読み込みと初期配置
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False) # 左右反転
    kk_rct = kk_img.get_rect() # 演習10: Rectの取得
    kk_rct.center = 300, 200 # 演習10: 初期座標の設定

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # 演習10: キー入力による移動
        key_lst = pg.key.get_pressed()
        move_x, move_y = 0, 0
        if key_lst[pg.K_UP]:    move_y = -1
        if key_lst[pg.K_DOWN]:  move_y = +1
        if key_lst[pg.K_LEFT]:  move_x = -1
        if key_lst[pg.K_RIGHT]: move_x = +1
        
        kk_rct.move_ip(move_x, move_y) # 演習10: move_ipによる移動

        # 演習5, 7, 8, 9: 背景のスクロール
        # xは0から3199をループするようにする
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])

        # 演習4, 10: こうかとんの描画
        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1
        clock.tick(200) # 演習6: FPSを200に変更

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()