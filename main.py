import pygame
from os import getcwd, chdir
import sys

from data.types.Player import Player, transform_image
from data.types.Shot import Shot
from data.types.Zombie import Zombie
from data.types.Monster import Monster
from data.types.Shooter import Shooter
from data.types.Item import Item

from random import random, randint


# Generate executable
dirpath = getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    chdir(sys._MEIPASS)

if __name__ == "__main__":
    def dead_menu():
        pass


    def info():
        pygame.init()
        display = pygame.display.set_mode([850, 600])

        # loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            pygame.display.update()


    def main_menu():
        # display
        pygame.init()
        display = pygame.display.set_mode([850, 600])

        font = font = pygame.font.Font("data/Main.ttf", 30)

        texts_blit = []

        buttons_coll = [
            # play game button
            {
                "rect": pygame.draw.rect(display, (0), pygame.Rect(5, 340, 300, 50)),
                "text": "Press here to play",
                "color": pygame.Color("Blue"),
                "func": game
            },

            # info button
            {
                "rect": pygame.draw.rect(display, (0), pygame.Rect(5, 500, 300, 50)),
                "text": "Press here",
                "color": pygame.Color("Blue"),
                "func": info
            }

        ]

        def background():
            for y in range(0, 12):
                pygame.draw.rect(display, (y * 10 + 70, y * 10 + 70, y * 10 + 70),
                                 pygame.Rect(0, y * 50, display.get_width(), 50))

        def texts_control():
            for text in texts_blit:
                # text for render
                txt_fr = font.render(text["text"], False, (0, 0, 0))

                display.blit(txt_fr, text["position"])

        def buttons_control():
            for bt in buttons_coll:
                if bt["rect"].collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    bt["color"] = (220, 220, 220)

                else:
                    bt["color"] = pygame.Color("White")

                surface = pygame.Surface([len(bt["text"]) * 20, bt["rect"].size[1]])
                surface.fill(bt["color"])

                texts_blit.append({
                    "text": bt["text"],
                    "position": (bt["rect"].x + 10, bt["rect"].y + 4)
                })

                display.blit(surface, bt["rect"])

        # loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons_coll:
                        if button["rect"].collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                            button["func"]()

            background()
            buttons_control()
            texts_control()

            pygame.display.update()


    def game():
        # display
        pygame.init()
        display = pygame.display.set_mode([850, 600])

        # groups
        player_group = pygame.sprite.Group()
        shot_group = pygame.sprite.Group()
        shot2_group = pygame.sprite.Group()
        zombie_group = pygame.sprite.Group()
        monster_group = pygame.sprite.Group()
        shooter_group = pygame.sprite.Group()
        bullet_group = pygame.sprite.Group()
        coin_group = pygame.sprite.Group()

        render_group = [player_group, shot_group,
                        shot2_group,
                        zombie_group,
                        monster_group,
                        shooter_group,
                        bullet_group,
                        coin_group]

        #  framerate
        framerate = pygame.time.Clock()

        #  common
        born_times = {
            "zombie": [0, 0.3],  # index, chance
            "monster": [0, 0.2],
            "shooter": [0, 0.3],
            "bullet": [0, 0.2],
            "coin": [0, 0.4],
        }

        font = pygame.font.Font("data/Main.ttf", 30)

        texts_blit = [
            # text life
            {
                "text": "Life: ",
                "position": (10, 10),
            },
            # text kills
            {
                "text": "Kills: ",
                "position": (10, 50),
            },
        ]

        # objects
        player = Player(player_group)

        background = {
            "image": transform_image(pygame.image.load("data/sprites/backgrounds/background_pampa.png").convert_alpha(),
                                     (850, 600), False, False),
            "rect": [0, 0],
            "mode": 0,
            "sprites": [
                transform_image(
                    pygame.image.load("data/sprites/backgrounds/background_pampa.png").convert_alpha(), (850, 600),
                    False, False),
                transform_image(
                    pygame.image.load("data/sprites/backgrounds/background_caatinga.png").convert_alpha(), (850, 600),
                    False, False),
                transform_image(
                    pygame.image.load("data/sprites/backgrounds/background_snow.png").convert_alpha(), (850, 600),
                    False, False),
                transform_image(
                    pygame.image.load("data/sprites/backgrounds/background_savanna.png").convert_alpha(), (850, 600),
                    False, False),
            ]
        }

        # functions
        def shoot():
            if player.bullets > 0:
                new_shot = Shot(shot_group)

                new_shot.rect.y = player.rect.y + 55
                new_shot.rect.x = player.rect.x
                player.bullets -= 1

            else:
                pass

        # noinspection PyGlobalUndefined
        def summon_control():
            global born_timers

            born_times["zombie"][0] += 0.5
            born_times["monster"][0] += 0.5
            born_times["shooter"][0] += 0.5
            born_times["bullet"][0] += 0.5
            born_times["coin"][0] += 0.5

            if born_times["zombie"][0] > 60:
                if random() < born_times["zombie"][1]:
                    Zombie(zombie_group)

                born_times["zombie"][0] = 0

            if born_times["monster"][0] > 70:
                if random() < born_times["monster"][1]:
                    Monster(monster_group)

                born_times["monster"][0] = 0

            if born_times["shooter"][0] > 70:
                if random() < born_times["shooter"][1]:
                    Shooter(shooter_group)

                born_times["shooter"][0] = 0

            if born_times["bullet"][0] > 40:
                if random() < born_times["bullet"][1]:
                    Item("data/sprites/icons/bullet.png", [25, 25], bullet_group)

                born_times["bullet"][0] = 0

            if born_times["coin"][0] > 50:
                if random() < born_times["coin"][1]:
                    Item("data/sprites/icons/coin.png", [25, 25], coin_group)

                born_times["coin"][0] = 0

        def difficulty_control():
            if player.kills > player.difficulty_index:
                born_times["zombie"][1] += 0.1
                born_times["monster"][1] += 0.1
                born_times["shooter"][1] += 0.1
                born_times["bullet"][1] += 0.1
                player.difficulty_index += randint(5, 10)

        def texts_control():
            for text in texts_blit:
                # text for render
                txt_fr = font.render(text["text"], False, (0, 0, 0))

                display.blit(txt_fr, text["position"])

        def interface_control():
            # bar life
            if player.hp > 50:
                bar_life = pygame.Color("Green")

            elif 50 >= player.hp > 30:
                bar_life = pygame.Color("Yellow")

            else:
                bar_life = pygame.Color("Red")

            pygame.draw.rect(display, bar_life, pygame.Rect(85, 10, player.hp, 30))
            pygame.draw.rect(display, 0, pygame.Rect(85, 10, 100, 30), 5)
            display.blit(pygame.font.Font("data/Main.ttf", 26).render(str(player.hp), False, (0, player.hp, 0)),
                         (115, 15))

            # kills text
            texts_blit[1]["text"] = "kills: " + str(player.kills)

            # selected gun

            # square of gun
            pygame.draw.rect(display, (0), pygame.Rect(10, 90, 50, 50), 5)

            # text selected gun

        def shooter_control():
            for shooter in shooter_group:
                if shooter.can_shoot:
                    shooter.shoot(Shot, shot2_group)

        def collisions():
            monster_coll = pygame.sprite.groupcollide(monster_group, shot_group, False, True,
                                                      pygame.sprite.collide_mask)

            # kill zombie
            if pygame.sprite.groupcollide(shot_group, zombie_group, True, True, pygame.sprite.collide_mask):
                player.kills += 1
                background["mode"] += 1

            # kill monster
            if monster_coll:
                for monster in monster_coll:
                    monster.hp -= 1

                    if monster.hp <= 0:
                        monster.kill()
                        player.kills += 1

            # kill shooter
            if pygame.sprite.groupcollide(shooter_group, shot_group, True, True):
                player.kills += 1

            # receive damage from shooter
            if pygame.sprite.groupcollide(shot2_group, player_group, True, False,
                                          pygame.sprite.collide_mask):
                player.hp -= 50

            # receive damage from monster
            if pygame.sprite.groupcollide(monster_group, player_group, True, False,
                                          pygame.sprite.collide_mask):
                player.hp -= 55

            # receive damage from zombie
            if pygame.sprite.groupcollide(zombie_group, player_group, True, False,
                                          pygame.sprite.collide_mask):
                player.hp -= 35

            # get bullet
            if pygame.sprite.groupcollide(bullet_group, player_group, True, False, pygame.sprite.collide_rect):
                player.bullets += 3

            # get coin
            elif pygame.sprite.groupcollide(coin_group, player_group, True, False, pygame.sprite.collide_rect):
                player.coins += 1

        def draw():
            for group in render_group:
                group.draw(display)
                group.update()

        # loop
        while True:
            framerate.tick(52)

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        shoot()

            # collisions
            collisions()

            # render
            display.blit(background["image"], background["rect"])

            draw()

            # update

            title = str(round(framerate.get_fps()))

            summon_control()
            difficulty_control()
            texts_control()

            shooter_control()

            interface_control()

            if player.hp <= 0:
                break

            pygame.display.set_caption(title)
            pygame.display.update()


    main_menu()
