import pygame
import pygame_textinput
from Game import Game

def draw_game():
        screen_info = pygame.display.Info()
        w, h = screen_info.current_w, screen_info.current_h
        if game.state == 0:
                game.textinput = pygame_textinput.TextInput()
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, w, h))

                pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(360, 280, 80, 40))
                screen.blit(myfont.render("MENU", 1, (255, 255, 255)), (381, 291))

        elif game.state == 0.5:
                map = game.world_map
                screen.fill((255, 255, 255))
                for x in range(map.width):
                        for y in range(map.height):
                                pygame.draw.rect(screen, map.tiles[x][y][1], pygame.Rect(x * map.tile_size, y * map.tile_size, map.tile_size, map.tile_size))
        
        elif game.state == 1:
                p_pos = game.player.pos
                map = game.world_map
                #Xscale = 
                ts = map.tile_size
                screen.fill((100, 100, 100))
                leftBound = 0
                rightBound = 0
                topBound = 0
                bottomBound = 0
                if int(p_pos.x) - map.game_Xsize//2 < 0:
                        leftBound = map.game_Xsize//2 - int(p_pos.x)
                if int(p_pos.x) + map.game_Xsize//2 > map.width:
                        rightBound = int(p_pos.x) + map.game_Xsize//2 - map.width
                if int(p_pos.y) - map.game_Ysize//2 < 0:
                        topBound = map.game_Ysize//2 - int(p_pos.y)
                if int(p_pos.y) + map.game_Ysize//2 > map.height:
                        bottomBound = int(p_pos.y) + map.game_Ysize//2 - map.height

                for x in range((int(p_pos.x) - map.game_Xsize//2 + leftBound)//ts, (int(p_pos.x) + map.game_Xsize//2 - rightBound)//ts):
                        for y in range((int(p_pos.y) - map.game_Ysize//2 + topBound)//ts, (int(p_pos.y) + map.game_Ysize//2 - bottomBound)//ts):
                                pygame.draw.rect(screen, map.tiles[x][y][1], pygame.Rect(x * ts, y * ts, ts, ts))


                pygame.draw.circle(screen, (255, 0, 0), (int(p_pos.x), int(p_pos.y)), game.world_map.tile_size, 0)
                """
                pygame.draw.polygon(screen, (255, 255, 255), game.Ship_pointlist(), 1)
                if game.thrust_counter > 9:
                        game.thrust_counter = 0
                if 0 <= game.thrust_counter <= 5 and game.thrust:
                        pygame.draw.polygon(screen, (255, 255, 255), game.Ship_thrust_pointlist(), 1)
                game.thrust_counter += 1
                """

                """
                if len(game.astr) > 0:
                        for i in range(len(game.astr)):
                                pygame.draw.circle(screen, (255, 255, 255), (int(game.astr[i].x), int(game.astr[i].y)), game.astr[i].size * 10, 2)
                if len(game.pjct) > 0:
                        for i in range(len(game.pjct)):
                                pygame.draw.circle(screen, (255, 255, 255), (int(game.pjct[i].x), int(game.pjct[i].y)), 2, 0)
                """
                """
                screen.blit(myfont.render("Points: {}".format(game.points), 1, (255, 255, 0)), (20, 20))
                screen.blit(myfont.render("Shield: {}".format(game.shield), 1, (255, 255, 0)), (20, 35))
                screen.blit(myfont.render("Stage: {}".format(game.stage), 1, (255, 255, 0)), (20, 50))
                """

        elif game.state == 2:
                pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(360, 280, 80, 40))
                screen.blit(myfont.render("PAUSE", 1, (255, 255, 255)), (377, 291))

        if game.state == 2 or game.state == 0:
                """
                pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(570, 10, 210, 40 + 15 * len(game.scores)))
                screen.blit(myfont.render("Highscores:", 1, (255, 255, 0)), (590, 20))
                for i, j in enumerate(game.scores):
                        screen.blit(myfont.render(str(j['Name']) + ': ' + str(j['Score']) + ' at ' + str(j['Stage']), 1, (255, 255, 0)), (590, 35 + i * 15))
                """
                """
                pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(260, 400, 300, 120))
                screen.blit(myfont.render("Controls:", 1, (255, 255, 255)), (270, 405))
                screen.blit(myfont.render("Thrust: Up Arrow", 1, (255, 255, 255)), (280, 420))
                screen.blit(myfont.render("Turn: Left and Right Arrows", 1, (255, 255, 255)), (280, 435))
                screen.blit(myfont.render("Shoot: Spacebar", 1, (255, 255, 255)), (280, 450))
                screen.blit(myfont.render("Pause: p", 1, (255, 255, 255)), (280, 465))
                screen.blit(myfont.render("Exit Game/New Game: ESC", 1, (255, 255, 255)), (280, 480))
                screen.blit(myfont.render("Sumbmit Score: Enter", 1, (255, 255, 255)), (280, 495))
                """
                """
                pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(570, 400, 210, 30 + 15 * len(game.localScores)))
                screen.blit(myfont.render("Local Highscores:", 1, (255, 255, 0)), (590, 405))
                for i, j in enumerate(game.localScores):
                        screen.blit(myfont.render(str(j['Name']) + ': ' + str(j['Score']) + ' at ' + str(j['Stage']), 1, (255, 255, 0)), (590, 420 + i * 15))
                """

        elif game.state == 3:
                """
                screen.fill((225, 225, 225))
                screen.blit(game.textinput.get_surface(), (10, 10))
                if game.textinput.update(events) and len(game.textinput.get_text()) > 0:
                        game.save_highscore(game.textinput.get_text())
                """

pygame.init()
"""
icon = "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAAAAAB5Gfe6AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAADsIAAA7CARUoSoAAAAAHdElNRQfiCxkKNRUP4pqmAAAKpUlEQVR42u2dbUxVRxrH4YLACgKFtfiGWaVY0S12Y6P0Q7G7oo2mmnazIZoobYyFZpOi+0Fhk93VD63YTbYtSTditq1es40x2WjsVo0v2YrbVE1ti0awtUpXqotYWEAui7zd04v3Pneeqxe4XM7MMzNnfh+NCXPmnvPM78yZ+U9MjMFgMBgMBoPBYDAYDAaDwWAQR6wP6jZQ4kpMSoh3cg+kzv1F3vQk6lbQ4crd+IffLn+Uuhl0159S+O4xd/kc6naQkZS99ljj59VPJzm1CqQvqvzq/y2HXsxKoG4JEdOKdzdafefKF6RSt4SG2LyK43cs69vq1VOpm0KCK7lw9xWPZbUc3ZLnyCKQlL3maFu/ZXXV7ypMdlG3hoD0xZUX+izL6ms9sibbiTI0o7im0Rqi78LWRenUrRFP7LzKoRI4xPWa4mnUzRGOrwTWNHT5O+DO8QrnlUFfCTzS2ufvAM+V3c4rg+mLtl4IXL/V33bUeWVwWnHNdQvou1C5OJ26RWJxza88cSfYAVZjTfEM6iYJJS5t6fvfeFgH3DleOc9RZXBizksnO/pZB3Q11DirDGYu2X5xgF2/82xwZom7ycI4zAZd+dtr20I6wFk2GJe6dO+17tAOcJQN+krgqc6B0A5wlA1mFG67OHj/sgfv9fQOeB1ng9kl7hv+3/1ey60fuvqdZoOu/G2nW/0d0P5F7Zf/6XaYDcalFe2BEtj097/s+7TVYTY4Meflkx3+EjhY98eSig9vOMwGhyzQXwIHOo6vW7Tq9cteZ9kgs8Duax/8csr80tOeQSfZILLA1tN/+nlCxsr9TT0OskFsgTfcJdkxcQvfPN8eKIMnKudrXwSQBQ5e3FaYERMzu+zArYANfvP+0rQ46hZyhlngQOepl3ImxsRMXr6zwV8G+ztO3v8XrWEW2H1t79JU3++dPLe0NlAGBy5uX5JJ3UK+IAtsq92eP/TEx2esCJbBJnfJTOomciXEAuFiJyysOtce2inagi2Q3e6zyg7cDH0stAVb4MmXoeBNXl5V7w0pjNqCLXBPEQx5KXmln9wNGRp1xfUEssBtwac9Pn2Z+zqWI10Z9kKH6RjtGP5WD/9oaMfwxS58cdSO4Ye78MOjbowgPGEFSTdGVN4wiqwd6KUnzG3+8EuSdrDX3nCF7uHXZO1gEx/hhrqHJ0p0YwKb+gonOw9NlenGhEw2+Rn2AkMmSzW0wZS8smAJvBT2FtfcBpkF9refKJkdpshpboM+C/wePoHtfnZSmN9XbxtEFjjcR1CtbRBbYGNN8fSw/ynUBp/QqgwiCxxhIQSywevuZenx1K22EfTxY4SlMMgG735SmpdC3WobQZ+/RlgMhWzQW1+1fDJ1q+0DWeBIy+GwDd48UDaLutn2XX9mhJ/AkQ22n6taOIG64XaBLHCURRDMBnua9q/I0KUMMgscbRkMs8FBT23p3GTqltsEtsCRF0IhG/Q27NSlDEZggQC2wVsHymZTN90WHrDAkRdD4kWU59/UowymzHv1zOgWCDAb9JXBlZk69EDW8299PboFAmghtae2TAsbzC0/3Dy6BQLa2WBsUsE7dZ2jWyCAbfB7HWwwIeuFg7d7I7BAQDcbTF1QfvaeNxILBDSzwSmr3r5qRWSBgGY2mLv5o+bILBDQygZjEwuqWQmMbEOEVjaYkPXiISiBEW+J0ckGU5/cdLYHSmDEm6I0ssEpq6sDJXAs2+I0ssE5m8ZigYA2NjhWCwS0scEhC2weiwUCutjg2C0Q0MQGx26BAAtYGPSceXWeqmVw7BYIoIgN79dvPZ9FfSVREY0FAjhkpflweS71tURFVBYIoJidzrp3CpRMHY3OAgEWtNR7++ALSqaORmeBAIva8t47q2bqaHQWCOCwtatvr5pCfTVjJloLBHDcXvNHm9Urg1FbIIACFzvrqgsSVSuD0VsgEIzc9JVBBcOXp66u/jY6CwQgdNVXBnvObnpSsTIYm7flaEt0FghA7O79Mli9Wq0y6Cthu+qDiaHRhaNA8LLfBjeplUGPB7Go43EC0dtK2iBKDB1HQBKywWbFbJA1fTwRWeraILp5u+p3PRNtOpCyNojL1+1//u7xaB9eZW3QtgFMVRsMVZjxPLuK2qB9zVbTBm28cZW0QTtLl5I2aOvgpaIN2qsvCtqgvU1WzwZtvmnxA6XEiUR2ly1cUpU4kcj2gQsNqkqcSGS/ujCtUiJ11H55ZV2qQuooh9cX/FBJnzrK4wUWl1XpM+i5TGGggVX6DHo+2mLPBJsQ+IirPVOsIuC0rMGWSXYRhC5sse/lNfRgNokz6PHpQbZOX2AblDmDni1us3sCSxEbZMsb7Z7CVMMG0QJXuyexlbBBvMTZ7s8YStggPj3I9g9ZKtgg2+bAY/JKARtkG114TF/Kb4NoqxOPCWzpbRBvduPxCcOORTdcQdsd+XzEsmHZFVfYhldenzHHv/COK/wsEBj/0kuecLRAYNyLb3nC0wKBkOXXsp1IxNUCg6AF+LKdSMTXAgG0BUO2E4n4WiCANuFIdiIRZwsE8DYsqVJHeVsggDfiSZVBz90Cg7CtmFJl0PO3QIBtxpUqg56/BQLIBiXKoEeH5PBe0IptUJoMenx60H8Plz/G829hG5Qmgx6dHuRt+POKR/n+NWaD0mTQs8TQQU8t973+zAalyaBnpweJCL1BNihJBj1KDBUReySdDeLEUBHBV9LZIMqNFxR9JpkNstx4UeF3ktkgy40XFXgjlw2i3HhRkUdS2SDOjRcVeiWVDaLceIGxZxLZYIgFCgu+k8gGWW68yOhDeWxQsAUC0tigaAsEHrBBuhOJxFsggGyQ8kQi8RYIIBukPJFIvAUCyAYJU0cJLBDANkh2IhGFBQLYBslSR2ksEGA2SJY6SmOBALNBsgx6GgsEkA0SZdATWSCAbZAkg57KAgFsgyQZ9Oj0IKJbkNkgSQY9Oz2IqggxGyTJoGenB1ENQ6Q2KIOI4AN8hGfQk/7xAKQ/ghwvI4SPIXEBCkBYiImHoABkQzG5hAQgkzFyDQWodJz+RQQgeiGT4FU0ANEruQSTEQFIJmVksECAZFoOT0iSH4NEMTErhwUCBFPzclgggD/OCDqRSA4LBPDnOSEnEsligQC2QSEnEkljgQCyQSGpo3hxwuWqZRKcBchsUMiJRHh5yqkNcyQ4FJfZoJDUUbxAaW9RmgQH4SEb5J9B/+ASNep1qkNgG+SeQS/VIsVgDzAb5J5BL9cyVYDZIPcMehZi0N9xYv2sn1Bfup/JRTsui9m2h2IsPFffWyJLjMXE3A3/6hKxcRMHmXR+9dfnZs7IloEZs/I3HPuhD2yQYwY9jrLpvLR/y7p1JTKwvmTjG2daegXYIAozsrq/++wfe/a63fvIcfsa8XHD/wIN45pBz+KsfB7Y3XbrRpMs3L7bF1AhnjaIAs1khpsN4kg7meFmg0nZa4OhhjLDzQYfKfj9Fwpc/5AN/noqjzI47Tc131FfXCR4e8+9lj+JQwfkBL/Gy86VHUU/5dABP9v4t3/XX6qTnkuXj1Q8y2MbzSOLi1+r3LpFerZWvPKrHB4zVYlZuQueemqhAsyfnspjpsqVmJyapgSTkuKlC5w0GAwGg8FgMBgMBoPBYDAYDAY5+BHPsF9iqP/X+gAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0xMS0yNVQxMDo1MzoyMS0wNTowMN1gZtEAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMTEtMjVUMTA6NTM6MjEtMDU6MDCsPd5tAAAAAElFTkSuQmCC"
icon = io.BytesIO(base64.b64decode(icon))
icon = pygame.image.load(icon)
pygame.display.set_icon(icon)
"""
pygame.display.set_caption('highwayman')
screen = pygame.display.set_mode((800, 600))
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

running = True

game = Game()

clock = pygame.time.Clock()

while running:
        events = pygame.event.get()
        for event in events:
                if event.type == pygame.QUIT:
                        running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        if game.state == 1 or game.state == 2:
                                game.toggle_pause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if game.state == 0.5:
                                pos = pygame.mouse.get_pos()
                                game.start_game(pos)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        if game.state != 0:
                                game.end_game()
                        else:
                                game.generate_game()

        pressed = pygame.key.get_pressed()

        game.tick(pygame, pressed)

        draw_game()
        pygame.display.flip()
        clock.tick(60)