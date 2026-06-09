import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("こうかとんゲーム練習")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 背景画像
    bg_img = pg.image.load("fig/pg_bg.jpg")

    # こうかとん画像（左右反転）
    kk_img = pg.transform.flip(
        pg.image.load("fig/3.png"),
        True,
        False
    )

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 背景描画
        screen.blit(bg_img, (0, 0))

        # こうかとん描画（x=300, y=200）
        screen.blit(kk_img, (300, 200))

        pg.display.update()
        tmr += 1
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()