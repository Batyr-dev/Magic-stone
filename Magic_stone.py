import pygame
import random
import os
import sys
#------------------------------------------------------------------------------------------------------------------#
#def is control to quit from game
def quit_escape():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
#------------------------------------------------------------------------------------------------------------------#
#def is intro game                
def intro():
    #initialization backgrounds, fonts, music and sounds
    intro_background1 = pygame.image.load('intro_background1.jpg').convert()
    intro_background1 = pygame.transform.scale(intro_background1, (MAX_X, MAX_Y))
        
    intro_background2 = pygame.image.load('intro_background2.jpeg').convert()
    intro_background2 = pygame.transform.scale(intro_background2, (MAX_X, MAX_Y))

    intro_background3 = pygame.image.load('intro_background3.jpeg').convert()
    intro_background3 = pygame.transform.scale(intro_background3, (MAX_X, MAX_Y))

    intro_backgrounds = [intro_background1, intro_background2, intro_background3]
           
    magic_stone_word = 'Magic stone'
    magic_stone_color = (206, 105, 13)
    intro_font_size = 100
    intro_font_name = pygame.font.Font('font/PAPYRUS.TTF', intro_font_size)
    intro_font_name.set_bold(True)
    intro_text_surface = intro_font_name.render(magic_stone_word, True, magic_stone_color)    
    intro_font_x = (MAX_X // 2 - intro_text_surface.get_width() // 2)

    anubis_gods_of_egypt = pygame.image.load('anubis_gods_of_egypt.png').convert()
    anubis_gods_of_egypt = pygame.transform.scale(anubis_gods_of_egypt, (18, 39))
    anubis_gods_of_egypt_rect = (MAX_X//2 + 395, MAX_Y // 2 + 80)
    anubis_gods_of_egypt_background_color = (129, 129, 129)
    anubis_god_color = [(0, 0, 0), (0, 0, 80), (0, 0, 110), (0, 0, 170), (0, 0, 225), (54, 54, 226), (90, 90, 226), (130, 130, 226), (160, 160, 226), (190, 190, 226), (220, 220, 226)]

    story_text0 = ['The wanderer wanted to become immortal and', 'sought the abode of the god of death - Anubis.']
    story_text1 = ['And the wanderer found a spell that summoned', 'souls from the death world of Anubis.']
    story_text2 = ['And he began to test his fate.']
    story_texts = [story_text0, story_text1, story_text2]
    story_texts_color = [(48, 180, 207), (127, 0, 0)]
    story_texts_color_change = story_texts_color[0]
    story_text_step1 = 0
    story_text_step2 = 0    
    story_text_font_size = 25
    story_text_font_name = pygame.font.Font('font/PAPYRUS.TTF', story_text_font_size)
    story_text_font_name.set_bold(True)
    story_text_surface = story_text_font_name.render(story_texts[story_text_step1][story_text_step2], True, (255, 255, 255))    
    story_text_font_x = 50
    story_text_font_y = 50
    story_text_bool = True
    story_text_alpha_bool = True
    story_image_step = 0
    
    pyramid_door_color = (252, 233, 174)
    pyramid_door_color1 = (241, 151, 65)
    pyramid_door_move = pygame.mixer.Sound('fx/pyramid_door_move.wav')
    anubis_appearance = pygame.mixer.Sound('fx/anubis_appearance.wav')
    anubis_disappear = pygame.mixer.Sound('fx/anubis_disappear.wav')
    anubis_disappear.set_volume(0.5)
    
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.load('music/intro_music.mp3')    
    pygame.mixer.music.play(1, 0.0)
    
    intro_main_bool = True

    episode_1_bool = True
    episode_1_change_image = 0
    episode_1_step = 0

    episode_2_bool = False
    episode_2_def_episode_1 = True
    def_episode_1_step = 0

    episode_3_bool = False
    episode_3_bool_step = 0
    episode_3_def_episode_1 = True
    episode_3_def_episode_2 = False
    episode_3_anubis_play_bool = True

    episode_4_bool = False
    episode_4_bool_step = 0
    episode_4_bool_anubis_disappear_play_bool = True

    episode_5_bool = False
    episode_5_magic_stone_word_bool = True
    episode_5_magic_stone_word_step = ''
    episode_5_bool_step = 0
    anubis_gods_of_egypt_big = pygame.image.load('anubis_gods_of_egypt.png').convert()
    anubis_gods_of_egypt_big = pygame.transform.scale(anubis_gods_of_egypt_big, (170, 376))
    anubis_gods_of_egypt_rect_big = (MAX_X//2 - 85, MAX_Y // 2 - 100)
    magic_stone_color_step = 0
    music_volume = 0.4

    episode_6_bool = False
    red_step = 0
    green_step = 0
    blue_step = 0
    color_plus = True
    color_minus = False
    magic_stone_color = (206, 105, 13)
    magic_stone_font_step = 0
    episode_6_magic_stone_word_step = ''
    yellow1 = (255, 255, 0)
    yellow2 = (238, 238, 0)
    yellow3 = (205, 205, 0)
    yellow4 = (139, 139, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
    push_game_color = (white, yellow1, yellow2, yellow3, yellow4, black)
    push_game_font_size = 20
    push_game_font_name = pygame.font.Font('font/georgia.ttf', push_game_font_size)
    push_game_font_name.set_bold(True)
    push_game_text_surface = push_game_font_name.render('press any key to start playing', True, push_game_color[0])
    push_game_font_x = 325 + ((250 - push_game_text_surface.get_width()) // 2)
    push_game_step = 0
    start_game_bool = True
    start_game_show_bool = False
    start_game_step = 0
    #start intro 
    while intro_main_bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:                
                vol = 0                                            
                for i in range(4):
                    quit_escape()
                    pygame.mixer.music.set_volume(0.4 - vol)
                    vol += 0.1
                    clock.tick(3)
                               
                intro_main_bool = False                                
        #episode_1 change images in intro
        if episode_1_bool:
            if story_text_alpha_bool:
                intro_backgrounds[episode_1_change_image].set_alpha(episode_1_step)
                screen.blit(intro_backgrounds[episode_1_change_image], (0, 0))            
                pygame.display.flip()                
                episode_1_step += 5
            if story_text_bool:
                if story_image_step > 15 and story_image_step < 130:
                    story_text_surface = story_text_font_name.render(story_texts[story_text_step1][story_text_step2], True, story_texts_color_change)
                    screen.blit(story_text_surface, (story_text_font_x, story_text_font_y))
                    pygame.display.flip()
                if story_image_step == 150:
                    if episode_1_change_image == 2:
                        pass
                    else:
                        story_text_font_y += 35
                        story_text_step2 += 1
                        story_text_alpha_bool = False
                if story_image_step == 155:
                    if episode_1_change_image == 2:
                        pass
                    else: 
                        story_text_surface = story_text_font_name.render(story_texts[story_text_step1][story_text_step2], True, story_texts_color_change)
                        screen.blit(story_text_surface, (story_text_font_x, story_text_font_y))
                        pygame.display.flip()
                if story_image_step == 255:
                    story_text_font_y = 50
                    story_text_step2 = 0
                    story_text_step1 += 1
            if story_image_step > 255:
                episode_1_step = 0
                episode_1_change_image += 1
                story_image_step = 0
                story_text_alpha_bool = True
                if episode_1_change_image == 2:
                    story_text_step2 = 0 
                    story_texts_color_change = story_texts_color[1]
                if episode_1_change_image == 3:                    
                    episode_1_bool = False
                    episode_2_bool = True
            story_image_step += 5
            clock.tick(10)
        #episode_2 opening the stone door
        if episode_2_bool:
            if episode_2_def_episode_1:
                pygame.draw.rect(screen, pyramid_door_color, (MAX_X//2 + 394, MAX_Y // 2 + 78, 20, 42))
                pygame.draw.rect(screen, pyramid_door_color1, (MAX_X//2 + 394, MAX_Y // 2 + 78, 20, 42), 2)
                pyramid_door_move.play()
                pyramid_door_step = 0
                episode_2_def_episode_1 = False
            else:
                pygame.draw.rect(screen, anubis_god_color[0], (MAX_X//2 + 394, MAX_Y // 2 + 78, 20, 2 + pyramid_door_step))
                pygame.draw.rect(screen, pyramid_door_color1, (MAX_X//2 + 394, MAX_Y // 2 + 78 + pyramid_door_step, 20, 42 - pyramid_door_step), 2)
                pygame.display.flip()
                clock.tick(5)
                pyramid_door_step += 4
                def_episode_1_step += 1
                if def_episode_1_step == 10:
                    episode_2_bool = False
                    episode_3_bool = True                
        #episode_3 effect change color into door
        if episode_3_bool:
            if episode_3_anubis_play_bool:
                anubis_appearance.play()
                episode_3_anubis_play_bool = False
                
            if episode_3_def_episode_1:
                pygame.draw.rect(screen, anubis_god_color[episode_3_bool_step], (MAX_X//2 + 394, MAX_Y // 2 + 78, 20, 42))
                pygame.display.flip()
                clock.tick(10)
                episode_3_bool_step += 1
                if episode_3_bool_step == 11:
                    episode_3_def_episode_1 = False
                    episode_3_def_episode_2 = True
                    episode_3_bool_step = 10
                    
            if episode_3_def_episode_2:
                pygame.draw.rect(screen, anubis_god_color[episode_3_bool_step], (MAX_X//2 + 394, MAX_Y // 2 + 78, 20, 42))
                pygame.display.flip()
                clock.tick(10)
                episode_3_bool_step -= 1
                if episode_3_bool_step == -1:
                    episode_3_bool = False
                    episode_4_bool = True
        #episode_4 anubis appearanced and disappeared
        if episode_4_bool:
            anubis_gods_of_egypt.set_colorkey(anubis_gods_of_egypt_background_color)
            anubis_gods_of_egypt.set_alpha(episode_4_bool_step)
            screen.blit(anubis_gods_of_egypt, anubis_gods_of_egypt_rect)
            pygame.display.flip()
            clock.tick(10)
            episode_4_bool_step += 5
            if episode_4_bool_step == 240:
                if episode_4_bool_anubis_disappear_play_bool:
                    anubis_disappear.play()
                    episode_4_bool_anubis_disappear_play_bool = False
                    
            if episode_4_bool_step == 255:
                pygame.draw.rect(screen, anubis_god_color[0], (MAX_X//2 + 394, MAX_Y // 2 + 78, 20, 42))
                episode_4_bool = False
                episode_5_bool = True        
        #episode_5 anubis appearanced in center screen
        if episode_5_bool:
            if episode_5_magic_stone_word_bool:
                pygame.mixer.music.set_volume(music_volume)
                music_volume += 0.1
                if music_volume == 1.0:
                    music_volume = 1.0
                episode_5_magic_stone_word_step += magic_stone_word[magic_stone_font_step]
                intro_text_surface = intro_font_name.render(episode_5_magic_stone_word_step, True, magic_stone_color)
                screen.blit(intro_text_surface, (intro_font_x, 100))
                
            anubis_gods_of_egypt_big.set_colorkey(anubis_gods_of_egypt_background_color)
            anubis_gods_of_egypt_big.set_alpha(episode_5_bool_step)        
            screen.blit(anubis_gods_of_egypt_big, anubis_gods_of_egypt_rect_big)                    
            pygame.display.flip()
            clock.tick(5)
            episode_5_bool_step += 10
            if episode_5_bool_step > 200:
                episode_5_bool = False
                episode_6_bool = True
                magic_stone_font_step = 10
                red_step = 206
                green_step = 105
                blue_step = 13

            magic_stone_font_step += 1
            if magic_stone_font_step == 11:                
                episode_5_magic_stone_word_bool = False                
                magic_stone_font_step = 0
        #episode_6 word the Magic stone changed color
        if episode_6_bool:
            episode_6_magic_stone_word_step += magic_stone_word[magic_stone_font_step]
            intro_text_surface = intro_font_name.render(episode_6_magic_stone_word_step, True, (red_step, green_step, blue_step))
            screen.blit(intro_text_surface, (intro_font_x, 100))            
            pygame.display.flip()
            clock.tick(60)
            magic_stone_font_step += 1
            if magic_stone_font_step == 11:
                episode_6_magic_stone_word_step = ''
                magic_stone_font_step = 0
                if start_game_bool:
                    start_game_step += 1
                    if start_game_step == 15:
                        start_game_show_bool = True
                        start_game_bool = False
                if start_game_show_bool:
                    push_game_text_surface = push_game_font_name.render('press any key to start playing', True, push_game_color[push_game_step])
                    screen.blit(push_game_text_surface, (push_game_font_x, 600))
                    pygame.display.flip()
                    push_game_step += 1
                    if push_game_step == 6:
                        push_game_step = 0  
                
            if color_plus:
                red_step += 5
                if red_step > 255:
                    red_step = 255
                    green_step += 5
                    if green_step > 255:
                        green_step = 255
                        blue_step += 5
                        if blue_step > 255:
                            blue_step = 255
                            color_plus = False
                            color_minus = True
                            
            if color_minus:
                blue_step -= 5
                if blue_step < -1:
                    blue_step = 0
                    green_step -= 5
                    if green_step < -1:
                        green_step = 0
                        red_step -= 5
                        if red_step < -1:
                            red_step = 0
                            color_plus = True
                            color_minus = False   
#------------------------------------------------------------------------------------------------------------------#    
#def for input name player
def player_name(game_main_music_step, random_trump_stones):
    #initialization backgrounds, fonts, music and sounds
    player_name_background = pygame.image.load('player_name_background.jpg').convert()
    player_name_background = pygame.transform.scale(player_name_background, (MAX_X, MAX_Y))

    anubis_gods_of_egypt_left = pygame.image.load('anubis_gods_of_egypt_left.png').convert()
    anubis_gods_of_egypt_left = pygame.transform.scale(anubis_gods_of_egypt_left, (170, 376))
    anubis_gods_of_egypt = pygame.image.load('anubis_gods_of_egypt.png').convert()
    anubis_gods_of_egypt = pygame.transform.scale(anubis_gods_of_egypt, (170, 376))
    anubis_gods_of_egypt_background_color = (129, 129, 129)
    
    input_box = pygame.image.load('input_box.jpg').convert()
    input_box = pygame.transform.scale(input_box, (320, 320))

    input_label = pygame.image.load('input_label.png').convert()
    input_label = pygame.transform.scale(input_label, (175, 40))
    
    screen_fill_black = pygame.image.load('screen_fill_black.png').convert()
    screen_fill_black = pygame.transform.scale(screen_fill_black, (MAX_X, MAX_Y))

    screen_fill_black_sound = pygame.mixer.Sound('fx/screen_fill_black_sound.wav')
    screen_fill_black_sound.set_volume(0.8)
    
    anubises_appearance_sound = pygame.mixer.Sound('fx/anubises_appearance_sound.wav')
    anubises_appearance_sound.set_volume(0.8)

    wrong_key_layout_text_clear = pygame.image.load('wrong_key_layout_text_clear.png').convert()
    wrong_key_layout_text_clear = pygame.transform.scale(wrong_key_layout_text_clear, (250, 20))
    wrong_sound = pygame.mixer.Sound('fx/aliens_voice4_sound.wav')
    
    input_name_sound0 = pygame.mixer.Sound('fx/input_name_sound0.wav')
    input_name_sound1 = pygame.mixer.Sound('fx/input_name_sound1.wav')
    input_name_sound2 = pygame.mixer.Sound('fx/input_name_sound2.wav')
    input_name_sound3 = pygame.mixer.Sound('fx/input_name_sound3.wav')
    input_name_sounds = [input_name_sound0, input_name_sound1, input_name_sound2, input_name_sound3]
    
    open_label_to_input_sound = pygame.mixer.Sound('fx/open_label_to_input_sound.wav')
    open_label_to_input_sound.set_volume(0.8)
    
    screen_fill_black_sound.play()    
    for j in range(0, 255, 25):
        quit_escape()
        screen_fill_black.set_alpha(j)
        screen.blit(screen_fill_black, (0,0))
        pygame.display.flip()
        clock.tick(10)
        
    pygame.mixer.music.load('music/player_name_music.wav')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1, 0.0)    
        
    for j in range(0, 255, 15):
        quit_escape()
        player_name_background.set_alpha(j)
        screen.blit(player_name_background, (0,0))        
        pygame.display.flip()
        clock.tick(10)

    anubises_appearance_sound.play()
    for j in range(0, 255, 10):
        quit_escape()
        anubis_gods_of_egypt.set_colorkey(anubis_gods_of_egypt_background_color)
        anubis_gods_of_egypt_left.set_colorkey(anubis_gods_of_egypt_background_color)
        anubis_gods_of_egypt.set_alpha(j)
        anubis_gods_of_egypt_left.set_alpha(j)
        input_box.set_alpha(j)
        screen.blit(anubis_gods_of_egypt_left, (100,200))
        screen.blit(anubis_gods_of_egypt, (630,200))
        screen.blit(input_box, (290,200))
        pygame.display.flip()
        clock.tick(10)

    input_word0 = 'Wanderer!'
    input_word1 = 'Welcome to my'
    input_word2 = 'AbodE!'
    input_word3 = 'Enter your name:'
    input_words = [input_word0, input_word1, input_word2, input_word3]
    input_color = (127, 0, 0)
    font_size = 25
    font_name = pygame.font.Font('font/PAPYRUS.TTF', font_size)
    font_name.set_bold(True)
    text_surface = font_name.render(input_words[0], True, input_color)    
    font_x = (MAX_X // 2 - text_surface.get_width() // 2)
    font_y = 235
    font_y_step = 0
    input_word_step = ''
    anubis_text_step = 0
    anubis_text_step_bool = True
    anubis_text_speed = 5
    anubis_button_speed_bool = False
    input_name_sounds_bool = True
    indicator_step = 0
    next_text_bool = False
    while anubis_text_step < 4:
        #reading events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()                    
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:                
                anubis_text_speed = 500                                      
                input_name_sounds_bool = False
                anubis_button_speed_bool = True
                input_name_sounds[anubis_text_step].stop()
                           
        if next_text_bool:
            font_y = 235 + font_y_step
            text_surface = font_name.render(input_words[anubis_text_step], True, input_color)
            font_x = (MAX_X // 2 - text_surface.get_width() // 2)
            input_word_step = ''
            next_text_bool = False
            
        if input_name_sounds_bool:
            if anubis_button_speed_bool:
                pass
            else:
                input_name_sounds[anubis_text_step].stop()
                input_name_sounds[anubis_text_step].play()
                input_name_sounds_bool = False
                
        if indicator_step < len(input_words[anubis_text_step]):            
            input_word_step += input_words[anubis_text_step][indicator_step]
            text_surface = font_name.render(input_word_step, True, input_color)
            screen.blit(text_surface, (font_x, font_y))  
            pygame.display.flip()
            clock.tick(anubis_text_speed)
            indicator_step += 1
        else:
            font_y_step += 40
            anubis_text_step += 1
            indicator_step = 0
            next_text_bool = True
            input_name_sounds_bool = True
            
        if anubis_text_step == 3:
            if anubis_text_step_bool:
                anubis_text_speed = 5                                      
                input_name_sounds_bool = True
                anubis_text_step_bool = False
                anubis_button_speed_bool = False

    input_name_sounds[3].stop()
    open_label_to_input_sound.play()
    input_label_rect = (360, 410)
    for j in range(0, 255, 15):
        quit_escape()
        input_label.set_alpha(j)
        screen.blit(input_label, input_label_rect)
        pygame.display.flip()
        clock.tick(15)
    #parametrs for procces input player name
    blue = (3, 2, 80)
    blue1 = (6, 3, 143)
    blue2 = (11, 5, 218)
    blue3 = (45, 39, 250)
    blue4 = (125, 122, 252)
    blue5 = (213, 211, 254)    
    input_name_font_color = [blue, blue1, blue2, blue3, blue4, blue5]
    white = (255, 255, 255)
    input_name_font_step = 0
    font_size = 18
    font_name = pygame.font.Font('font/PAPYRUS.TTF', font_size)
    font_name.set_bold(True)
    cursor_text = '|'
    cursor_bool = False
    name_player = ''
    name_player_surface = font_name.render(name_player, True, input_name_font_color[input_name_font_step])
    name_player_x = (input_label_rect[0] + 169 - text_surface.get_width() // 2) 
    press_down_stone_sound = pygame.mixer.Sound('fx/press_down_stone_sound.wav')
    press_down_stone_sound.set_volume(0.8)
    input_name_text_sound = pygame.mixer.Sound('fx/input_name_text_sound.wav')
    input_name_text_sound.set_volume(0.5)
    back_space_text_sound = pygame.mixer.Sound('fx/back_space_text_sound.wav')
    back_space_text_sound.set_volume(0.5)
    back_space_step = 0
    input_name_color_bool = False
    #when wrong key layout
    red = (255, 0, 0)
    wrong_key_layout_text = 'Change your keyboard layout to English'
    wrong_key_layout_text_font_size = 11
    wrong_key_layout_text_font_name = pygame.font.Font('font/PAPYRUS.TTF', wrong_key_layout_text_font_size)
    wrong_key_layout_text_font_name.set_bold(True)
    wrong_key_layout_surface = wrong_key_layout_text_font_name.render(wrong_key_layout_text, True, red)
    wrong_key_layout_x = input_label_rect[0] - 27
    wrong_key_layout_y = input_label_rect[1] + 43
    #process input name player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        
            if event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_RETURN:
                    if len(name_player) == 0:
                        continue                        
                    else:
                        cursor_bool = False
                        press_down_stone_sound.set_volume(0.4)
                        press_down_stone_sound.play()

                        player_name_none = ''
                        player_name_bool = True
                        for i in range(25):
                            if player_name_bool:
                                name_player_surface = font_name.render(name_player, True, red)
                                name_player_x = (input_label_rect[0] + 89 - name_player_surface.get_width() // 2)
                                screen.blit(name_player_surface, (name_player_x, input_label_rect[1] + 7))                                 
                                pygame.display.flip()
                                clock.tick(30)
                                player_name_bool = False
                            else:
                                pygame.draw.rect(screen, white, (input_label_rect[0] + 9, input_label_rect[1] + 9, 160, 22))
                                pygame.display.flip()
                                clock.tick(25)
                                player_name_bool = True
                                                                           
                        vol = 0                                            
                        for i in range(2):
                            quit_escape()
                            pygame.mixer.music.set_volume(0.4 - vol)
                            vol += 0.1
                            clock.tick(2)                        

                        game_center(name_player, game_main_music_step, random_trump_stones)
                                            
                elif event.key == pygame.K_SPACE or event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL or event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT or event.key == pygame.K_RALT or event.key == pygame.K_LALT or event.key == pygame.K_NUMLOCK:
                    continue
                elif event.key == pygame.K_BACKSPACE:
                    if len(name_player) == 0:
                        continue
                    else:
                        back_space_text_sound.play()
                        name_player = name_player[:-1]                
                elif event.unicode in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-+_':
                    screen.blit(wrong_key_layout_text_clear, (input_label_rect[0] - 35, input_label_rect[1] + 45))
                    pygame.display.flip()
                    if len(name_player) == 9:
                        name_player = name_player[:9]
                    else:
                        input_name_text_sound.play()
                        name_player += event.unicode.upper()                    
                else:
                    wrong_sound.set_volume(0.8)
                    wrong_sound.play()
                    wrong_key_layout_surface = wrong_key_layout_text_font_name.render(wrong_key_layout_text, True, red)
                    screen.blit(wrong_key_layout_surface, (wrong_key_layout_x, wrong_key_layout_y))  
                    pygame.display.flip()                    

        if len(name_player) == 0:
            pygame.draw.rect(screen, white, (input_label_rect[0] + 9, input_label_rect[1] + 9, 160, 22))
            pygame.display.flip()
            name_player_surface = font_name.render(cursor_text, True, input_name_font_color[input_name_font_step])
            name_player_x = (input_label_rect[0] + 85 - name_player_surface.get_width() // 2)
            screen.blit(name_player_surface, (name_player_x, input_label_rect[1] + 7))        
            pygame.display.flip()
            clock.tick(8)
        else:            
            pygame.draw.rect(screen, white, (input_label_rect[0] + 9, input_label_rect[1] + 9, 160, 22))
            pygame.display.flip()
            name_player_surface = font_name.render(name_player, True, input_name_font_color[input_name_font_step])
            name_player_x = (input_label_rect[0] + 89 - name_player_surface.get_width() // 2)
            screen.blit(name_player_surface, (name_player_x, input_label_rect[1] + 7))        
            pygame.display.flip()
            clock.tick(8)
        if input_name_color_bool == False:
            input_name_font_step += 1
            if input_name_font_step == 5:
                input_name_color_bool = True
        else:
            input_name_font_step -= 1
            if input_name_font_step == 0:
                input_name_color_bool = False    
#------------------------------------------------------------------------------------------------------------------#    
#def is credit game
def credit_game():
    #initialization finish game backgrounds and photo developer
    finish_game_background1 = pygame.image.load('finish_game_background1.jpg').convert()
    finish_game_background1 = pygame.transform.scale(finish_game_background1, (MAX_X, MAX_Y))

    finish_game_background2 = pygame.image.load('finish_game_background2.jpg').convert()
    finish_game_background2 = pygame.transform.scale(finish_game_background2, (MAX_X, MAX_Y))

    finish_game_background3 = pygame.image.load('finish_game_background3.jpg').convert()
    finish_game_background3 = pygame.transform.scale(finish_game_background3, (MAX_X, MAX_Y))
    finish_game_background4 = pygame.image.load('finish_game_background4.jpg').convert()
    finish_game_background4 = pygame.transform.scale(finish_game_background4, (MAX_X, MAX_Y))
    finish_game_backgrounds = [finish_game_background1, finish_game_background2, finish_game_background3, finish_game_background4]

    cool_developer = pygame.image.load('cool_dev.jpg').convert()
    cool_developer = pygame.transform.scale(cool_developer, (160, 160))
    cool_developer_rect = (MAX_X // 2 - 80, 50)

    pharaoh_left = pygame.image.load('pharaoh_left.jpg').convert()
    pharaoh_left = pygame.transform.scale(pharaoh_left, (180, 200))
    pharaoh_left_rect = (140, 30)
    pharaoh_right = pygame.image.load('pharaoh_right.jpg').convert()
    pharaoh_right = pygame.transform.scale(pharaoh_right, (180, 200))
    pharaoh_right_rect = (MAX_X - 320, 30)
    
    finish_game_info_box = pygame.image.load('finish_game_info_box.jpg').convert()
    finish_game_info_box = pygame.transform.scale(finish_game_info_box, (600, 400))
    finish_game_info_box_rect = (MAX_X // 2 - 300, 240)

    ok_press_button = pygame.image.load('buttons/ok_press_button.jpg').convert()
    ok_press_button = pygame.transform.scale(ok_press_button, (50, 50))
    ok_button = pygame.image.load('buttons/ok_button.jpg').convert()
    ok_button = pygame.transform.scale(ok_button, (50, 50))
    ok_button_rect = (MAX_X // 2 - 25, 585)
    select_ok_sound = pygame.mixer.Sound('fx/select_ok_sound.wav')       
    #screen_fill_black
    screen_fill_black = pygame.image.load('screen_fill_black.png').convert()
    screen_fill_black = pygame.transform.scale(screen_fill_black, (MAX_X, MAX_Y))
    screen_fill_black_sound = pygame.mixer.Sound('fx/screen_fill_black_sound.wav')
    screen_fill_black_sound.set_volume(0.8)
    
    screen_fill_black_sound.play()
    for j in range(0, 255, 10):
        quit_escape()
        screen_fill_black.set_alpha(j)
        screen.blit(screen_fill_black, (0,0))
        pygame.display.flip()
        clock.tick(10)
    #play finish music
    pygame.mixer.music.load('music/finish_game_music.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(1, 0.0)
    #color for draw rect
    rose1 = (64, 0, 35)
    rose2 = (113, 0, 62)
    rose3 = (166, 0, 91)
    rose4 = (230, 0, 126)
    rose5 = (255, 74, 174)
    white = (255, 255, 255)
    credit_color = [rose1, rose2, rose3, rose4, rose5, white]
    color_step = 0
    color_bool = False    
    #show background images
    for i in range(4):
        for j in range(0, 255, 5):
            quit_escape()
            finish_game_backgrounds[i].set_alpha(j)
            screen.blit(finish_game_backgrounds[i], (0,0))
            pygame.display.flip()
            clock.tick(10)
    #draw rect and show images 
    pygame.draw.rect(screen, credit_color[0], (cool_developer_rect[0] - 2, cool_developer_rect[1] - 2, 164, 164), 3)
    for j in range(0, 255, 5):
        quit_escape()
        cool_developer.set_alpha(j)
        pharaoh_left.set_alpha(j)
        pharaoh_right.set_alpha(j)
        screen.blit(cool_developer, cool_developer_rect)
        screen.blit(pharaoh_left, pharaoh_left_rect)
        screen.blit(pharaoh_right, pharaoh_right_rect)
        pygame.display.flip()
        clock.tick(20)
    #draw rect and show images 
    pygame.draw.rect(screen, credit_color[0], (finish_game_info_box_rect[0] - 2, finish_game_info_box_rect[1] - 2, 604, 404), 3)
    for j in range(0, 255, 15):
        quit_escape()
        finish_game_info_box.set_alpha(j)
        screen.blit(finish_game_info_box, finish_game_info_box_rect)
        pygame.display.flip()
        clock.tick(15)
    
    episode_font_size = 30
    episode1_text = ['Game Developer:', '   BaT&R']
    episode2_text = ['Programming language:', '   Python 3 (v 3.8.0)']
    episode3_text = ['Used libraries:', '   Pygame (v 1.9.6)']
    episode4_text = ['Music and sounds:', '   Stargate 1994, zvukipro.com']
    episode_texts = (episode1_text, episode2_text, episode3_text, episode4_text)
    episode_texts_index = 0

    blue = (139, 213, 228)
    yellow = (255, 255, 0)
    color_font = blue
    font_episodes_name = pygame.font.Font('font/PAPYRUS.TTF', episode_font_size)
    font_episodes_name.set_bold(True)      
    text_step = 0
    control_text = False
    text_index = 0    
    text_surface = font_episodes_name.render(episode_texts[episode_texts_index][text_index], True, color_font)
    font_x = 250 
    font_y = 250
       
    credit_episodes = True
    while credit_episodes:
        if text_index == 0:
            color_font = blue
            font_x = 250
        else:
            color_font = yellow
            
        quit_escape()        
        text_surface = font_episodes_name.render(episode_texts[episode_texts_index][text_index][:text_step], True, color_font)
        screen.blit(text_surface, (font_x, font_y))        
        pygame.display.flip()
        clock.tick(10)
        
        if control_text == False:
            text_step += 1
            if text_step == (len(episode_texts[episode_texts_index][text_index]) + 1):
                font_y += 35
                text_step = 0                
                text_index += 1
                if text_index == (len (episode_texts[episode_texts_index])):
                    text_index = 0                        
                    episode_texts_index += 1
                    font_y += 15
                    if episode_texts_index == 4:
                        credit_episodes = False

        pygame.draw.rect(screen, credit_color[color_step], (cool_developer_rect[0] - 2, cool_developer_rect[1] - 2, 164, 164), 3)
        pygame.draw.rect(screen, credit_color[color_step], (finish_game_info_box_rect[0] - 2, finish_game_info_box_rect[1] - 2, 604, 404), 3)
        if color_bool == False:
            color_step += 1
            if color_step == 5:
                color_bool = True
        else:
            color_step -= 1
            if color_step == 0:
                color_bool = False
    #show button ok
    for j in range(0, 255, 15):
        quit_escape()
        ok_button.set_alpha(j)
        ok_button.set_colorkey((255, 255, 255))
        screen.blit(ok_button, ok_button_rect)
        pygame.display.flip()
        clock.tick(20)
    #ok button font name and size
    black = (0, 0, 0)     
    ok_button_colors = ((3, 2, 80), (6, 3, 143), (11, 5, 218), (45, 39, 250), (125, 122, 252), (213, 211, 254))
    ok_button_font_size = 15
    ok_button_text = 'OK'
    ok_button_font_name = pygame.font.Font('font/PAPYRUS.TTF', ok_button_font_size)
    ok_button_font_name.set_bold(True)
    ok_button_surface = ok_button_font_name.render(ok_button_text, True, ok_button_colors[0])
    ok_button_font_x = (ok_button_rect[0] + 26 - ok_button_surface.get_width() // 2)
    ok_button_font_y = ok_button_rect[1] + 15
    screen.blit(ok_button_surface, (ok_button_font_x, ok_button_font_y))
    #process press button ok
    color_bool = True
    color_step = 0
    credit_ok_button_bool = True    
    while credit_ok_button_bool:
        #exit game when music is ending 
        if pygame.mixer.music.get_pos() == -1:
            for j in range(0, 255, 5):
                quit_escape()
                screen_fill_black.set_alpha(j)
                screen.blit(screen_fill_black, (0,0))
                pygame.display.flip()
                clock.tick(5)
                #exit system
                pygame.quit()
                sys.exit()      
        pygame.draw.rect(screen, credit_color[color_step], (cool_developer_rect[0] - 2, cool_developer_rect[1] - 2, 164, 164), 3)
        pygame.draw.rect(screen, credit_color[color_step], (finish_game_info_box_rect[0] - 2, finish_game_info_box_rect[1] - 2, 604, 404), 3)
        ok_button_surface = ok_button_font_name.render(ok_button_text, True, ok_button_colors[color_step])
        screen.blit(ok_button_surface, (ok_button_font_x, ok_button_font_y))
        pygame.display.flip()
        clock.tick(10)
        if color_bool:
            color_step += 1
            if color_step == 5:
                color_bool = False
        else:
            color_step -= 1
            if color_step == 0:
                color_bool = True                
        #read events        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()                
            #push ok button process
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (mouse_x >= ok_button_rect[0] and mouse_x <= ok_button_rect[0] + 49) and (mouse_y >= ok_button_rect[1] and mouse_y <= ok_button_rect[1] + 59):
                    pressed = pygame.mouse.get_pressed()
                    if pressed[0] == 1:
                        credit_ok_button_bool = True                        
                        ok_press_button.set_colorkey((255, 255, 255))
                        screen.blit(ok_press_button, ok_button_rect)
                        ok_button_surface = ok_button_font_name.render(ok_button_text, True, black)
                        screen.blit(ok_button_surface, (ok_button_font_x, ok_button_font_y))
                        select_ok_sound.set_volume(0.4)
                        select_ok_sound.play()
                        #screen fill black
                        screen_fill_black_sound.play()
                        for j in range(0, 255, 10):
                            quit_escape()
                            screen_fill_black.set_alpha(j)
                            screen.blit(screen_fill_black, (0,0))
                            pygame.display.flip()
                            clock.tick(10)

                        vol = 0                                            
                        for i in range(3):
                            quit_escape()
                            pygame.mixer.music.set_volume(0.4 - vol)
                            vol += 0.1
                            clock.tick(2)  
                        #exit system
                        pygame.quit()
                        sys.exit()        
#------------------------------------------------------------------------------------------------------------------#
#the main def game
def game_center(playerName, game_main_music_step, random_trump_stones):
    #def time for game
    def game_timer(milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left):
        #clear time indecators
        screen.blit(label_for_clear_time_and_turn, (label_for_clear_time_and_turn_rect[0], label_for_clear_time_and_turn_rect[1]))
        pygame.display.flip()
        if milliseconds > 1000:
            seconds_right += 1
            milliseconds -= 1000
            
        if seconds_right == 10:
            seconds_left += 1
            seconds_right = 0
            
        if seconds_left == 6:
            minutes_right += 1 
            seconds_left = 0
            
        if minutes_right == 10:
            minutes_left += 1
            minutes_right = 0
            
        if minutes_left == 6:
            hour_right += 1
            minutes_left = 0
            
        if hour_right == 10:
            hour_left += 1
            hour_right = 0
            
        if hour_left == 2 and hour_right == 4:
            hour_left = 0
            hour_right = 0
            minutes_right = 0
            minutes_left = 0
            seconds_right = 0
            seconds_left = 0
            show_players_best_score(game_main_music_step, False)
        #show time indecators    
        timer_min_sec_surface = timer_min_sec_font.render('{}{}:{}{}:{}{}'.format(hour_left, hour_right, minutes_left, minutes_right, seconds_left, seconds_right), True, time_show_color[1])   
        screen.blit(timer_min_sec_surface, (timer_min_sec_x, timer_min_sec_y))
        pygame.display.flip()
        clock.tick(350)
        return milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left
#------------------------------------------------------------------------------------------------------------------#
    #def of trump stones to style up to down 
    def up_to_down():
        trump_stone_background = pygame.image.load('stone/stone_background1.png').convert()
        trump_stone_background = pygame.transform.scale(stone_background, (88, 266))
        trump_stone_background_rect = [arena_for_stones_rect[0] + 75, arena_for_stones_rect[1] + 75]
        trump_stone_background_x = 0
        
        stones_move_sound = pygame.mixer.Sound('fx/stones_move_sound.wav')
        stones_move_sound.set_volume(0.5)
        stone_collision.set_volume(1.0)
        up_to_down_block = [[0, 12], [13, 1], [2, 14], [15, 3]]
        up_to_down_block_step = 0
            
        up_to_down_stone_count = 0
        up_to_down_stone_move_step = 0
        up_to_down_stone_move_step_first = 0
        up_to_down_stone_move_step_second = 0
        up_to_down_stone_move_step_second_bool = False        
        up_to_down_stone_move_step_third = 0
        up_to_down_stone_move_step_third_bool = False
        up_to_down_stone_move_count = 0
        max_count = 0
        
        for t1 in range(4):
            for t2 in range(3):
                max_count +=1
                stones_move_sound.play()
                if max_count == 16:
                    pass
                else:
                    screen.blit(stones[stone_random[up_to_down_stone_count + up_to_down_stone_move_count]], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]])
                    pygame.display.flip()

                if (up_to_down_block[up_to_down_block_step][0] - up_to_down_block[up_to_down_block_step][1]) > 0: 
                    up_to_down_stone_move_step = 0            
                    while up_to_down_stone_move_step < 88:
                        quit_escape()
                        screen.blit(stones[stone_random[up_to_down_stone_count]], (stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][0], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][1] - up_to_down_stone_move_step_first))
                        if up_to_down_stone_move_step_second_bool:
                            screen.blit(stones[stone_random[up_to_down_stone_count + 1]], (stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][0], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][1] - up_to_down_stone_move_step_second))
                        if up_to_down_stone_move_step_third_bool:
                            screen.blit(stones[stone_random[up_to_down_stone_count + 2]], (stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][0], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][1] - up_to_down_stone_move_step_third))
                        pygame.display.flip()
                        clock.tick(10)                
                        screen.blit(stone_background_mini_UpDown, (stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][0], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][1] + 77 - up_to_down_stone_move_step))
                        pygame.display.flip()
                        
                        up_to_down_stone_move_step += 11
                        up_to_down_stone_move_step_first += 11
                        if up_to_down_stone_move_step_second_bool:
                            up_to_down_stone_move_step_second += 11
                        if up_to_down_stone_move_step_third_bool:
                            up_to_down_stone_move_step_third += 11                                    

                    if up_to_down_stone_move_step_first > 77:
                        up_to_down_stone_move_step_second_bool = True
                    if up_to_down_stone_move_step_second > 77:
                        up_to_down_stone_move_step_third_bool = True

                    if up_to_down_stone_move_step_first > 253:
                        stones_move_sound.stop()
                        stone_collision.play()                

                    up_to_down_stone_move_count += 1    
                    if up_to_down_stone_move_count == 3:
                        screen.blit(trump_stone_background, (trump_stone_background_rect[0] + trump_stone_background_x, trump_stone_background_rect[1]))
                        pygame.display.flip()
                        if t1 == 3:
                            pass
                        else:
                            screen.blit(stones[stone_random[up_to_down_stone_count + 3]], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]])
                            pygame.display.flip()
                        for i in range(3):
                            quit_escape()
                            screen.blit(stones[stone_random[up_to_down_stone_count + i]], stone_cells_coords[up_to_down_block[up_to_down_block_step][1] + 4*i])
                            pygame.display.flip()
                            
                else:
                    up_to_down_stone_move_step = 0            
                    while up_to_down_stone_move_step < 88:
                        quit_escape()
                        screen.blit(stones[stone_random[up_to_down_stone_count]], (stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][0], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][1] + up_to_down_stone_move_step_first))
                        if up_to_down_stone_move_step_second_bool:
                            screen.blit(stones[stone_random[up_to_down_stone_count + 1]], (stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][0], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][1] + up_to_down_stone_move_step_second))
                        if up_to_down_stone_move_step_third_bool:
                            screen.blit(stones[stone_random[up_to_down_stone_count + 2]], (stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][0], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][1] + up_to_down_stone_move_step_third))
                        pygame.display.flip()
                        clock.tick(10)                
                        screen.blit(stone_background_mini_UpDown, (stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][0], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]][1] + up_to_down_stone_move_step))
                        pygame.display.flip()
                        
                        up_to_down_stone_move_step += 11
                        up_to_down_stone_move_step_first += 11
                        if up_to_down_stone_move_step_second_bool:
                            up_to_down_stone_move_step_second += 11
                        if up_to_down_stone_move_step_third_bool:
                            up_to_down_stone_move_step_third += 11                                    

                    if up_to_down_stone_move_step_first > 77:
                        up_to_down_stone_move_step_second_bool = True
                    if up_to_down_stone_move_step_second > 77:
                        up_to_down_stone_move_step_third_bool = True

                    if up_to_down_stone_move_step_first > 253:
                        stones_move_sound.stop()
                        stone_collision.play()                

                    up_to_down_stone_move_count += 1    
                    if up_to_down_stone_move_count == 3:                        
                        screen.blit(trump_stone_background, (trump_stone_background_rect[0] + trump_stone_background_x, trump_stone_background_rect[1] + 88))
                        pygame.display.flip()
                        screen.blit(stones[stone_random[up_to_down_stone_count + 3]], stone_cells_coords[up_to_down_block[up_to_down_block_step][0]])
                        pygame.display.flip()
                        for i in range(3):
                            quit_escape()
                            screen.blit(stones[stone_random[up_to_down_stone_count + i]], stone_cells_coords[up_to_down_block[up_to_down_block_step][1] - 4*i])
                            pygame.display.flip()

            if t1 == 3:
                up_to_down_stone_count += 3
            else:
                up_to_down_stone_count += 4
                
            up_to_down_stone_move_count = 0
            up_to_down_block_step += 1
            up_to_down_stone_move_step = 0
            up_to_down_stone_move_step_first = 0
            up_to_down_stone_move_step_second = 0
            up_to_down_stone_move_step_second_bool = False        
            up_to_down_stone_move_step_third = 0
            up_to_down_stone_move_step_third_bool = False
            up_to_down_stone_move_count = 0
            trump_stone_background_x += 88
#------------------------------------------------------------------------------------------------------------------#
    #def of trump stones to style right to left 
    def right_to_left():
        trump_stone_background = pygame.image.load('stone/stone_background1.png').convert()
        trump_stone_background = pygame.transform.scale(stone_background, (266, 88))
        trump_stone_background_rect = [arena_for_stones_rect[0] + 75, arena_for_stones_rect[1] + 75]
        trump_stone_background_y = 0
        
        stones_move_sound = pygame.mixer.Sound('fx/stones_move_sound.wav')
        stones_move_sound.set_volume(0.5)
        stone_collision.set_volume(1.0)
        right_to_left_block = [[3, 0], [4, 7], [11, 8], [12, 15]]
        right_to_left_block_step = 0
            
        right_to_left_stone_count = 0
        right_to_left_stone_move_step = 0
        right_to_left_stone_move_step_first = 0
        right_to_left_stone_move_step_second = 0
        right_to_left_stone_move_step_second_bool = False        
        right_to_left_stone_move_step_third = 0
        right_to_left_stone_move_step_third_bool = False
        right_to_left_stone_move_count = 0
        max_count = 0
        
        for t1 in range(4):
            for t2 in range(3):
                max_count +=1
                stones_move_sound.play()
                if max_count == 16:
                    pass
                else:
                    screen.blit(stones[stone_random[right_to_left_stone_count + right_to_left_stone_move_count]], stone_cells_coords[right_to_left_block[right_to_left_block_step][0]])
                    pygame.display.flip()

                if (right_to_left_block[right_to_left_block_step][0] - right_to_left_block[right_to_left_block_step][1]) > 0: 
                    right_to_left_stone_move_step = 0            
                    while right_to_left_stone_move_step < 88:
                        quit_escape()
                        screen.blit(stones[stone_random[right_to_left_stone_count]], (stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][0] - right_to_left_stone_move_step_first, stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][1]))
                        if right_to_left_stone_move_step_second_bool:
                            screen.blit(stones[stone_random[right_to_left_stone_count + 1]], (stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][0] - right_to_left_stone_move_step_second, stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][1]))
                        if right_to_left_stone_move_step_third_bool:
                            screen.blit(stones[stone_random[right_to_left_stone_count + 2]], (stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][0] - right_to_left_stone_move_step_third, stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][1]))
                        pygame.display.flip()
                        clock.tick(10)                
                        screen.blit(stone_background_mini_RightLeft, (stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][0] + 77 - right_to_left_stone_move_step, stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][1]))
                        pygame.display.flip()
                        
                        right_to_left_stone_move_step += 11
                        right_to_left_stone_move_step_first += 11
                        if right_to_left_stone_move_step_second_bool:
                            right_to_left_stone_move_step_second += 11
                        if right_to_left_stone_move_step_third_bool:
                            right_to_left_stone_move_step_third += 11                                    

                    if right_to_left_stone_move_step_first > 77:
                        right_to_left_stone_move_step_second_bool = True
                    if right_to_left_stone_move_step_second > 77:
                        right_to_left_stone_move_step_third_bool = True

                    if right_to_left_stone_move_step_first > 253:
                        stones_move_sound.stop()
                        stone_collision.play()                

                    right_to_left_stone_move_count += 1    
                    if right_to_left_stone_move_count == 3:
                        screen.blit(trump_stone_background, (trump_stone_background_rect[0], trump_stone_background_rect[1] + trump_stone_background_y))
                        pygame.display.flip()
                        screen.blit(stones[stone_random[right_to_left_stone_count + 3]], stone_cells_coords[right_to_left_block[right_to_left_block_step][0]])
                        for i in range(3):
                            quit_escape()
                            screen.blit(stones[stone_random[right_to_left_stone_count + i]], stone_cells_coords[right_to_left_stone_count + i])
                            pygame.display.flip()
                else:
                    right_to_left_stone_move_step = 0            
                    while right_to_left_stone_move_step < 88:
                        quit_escape()
                        screen.blit(stones[stone_random[right_to_left_stone_count]], (stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][0] + right_to_left_stone_move_step_first, stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][1]))
                        if right_to_left_stone_move_step_second_bool:
                            screen.blit(stones[stone_random[right_to_left_stone_count + 1]], (stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][0] + right_to_left_stone_move_step_second, stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][1]))
                        if right_to_left_stone_move_step_third_bool:
                            screen.blit(stones[stone_random[right_to_left_stone_count + 2]], (stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][0] + right_to_left_stone_move_step_third, stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][1]))
                        pygame.display.flip()
                        clock.tick(10)                
                        screen.blit(stone_background_mini_RightLeft, (stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][0] + right_to_left_stone_move_step, stone_cells_coords[right_to_left_block[right_to_left_block_step][0]][1]))
                        pygame.display.flip()
                        
                        right_to_left_stone_move_step += 11
                        right_to_left_stone_move_step_first += 11
                        if right_to_left_stone_move_step_second_bool:
                            right_to_left_stone_move_step_second += 11
                        if right_to_left_stone_move_step_third_bool:
                            right_to_left_stone_move_step_third += 11                                    

                    if right_to_left_stone_move_step_first > 77:
                        right_to_left_stone_move_step_second_bool = True
                    if right_to_left_stone_move_step_second > 77:
                        right_to_left_stone_move_step_third_bool = True

                    if right_to_left_stone_move_step_first > 253:
                        stones_move_sound.stop()
                        stone_collision.play()                

                    right_to_left_stone_move_count += 1    
                    if right_to_left_stone_move_count == 3:                        
                        screen.blit(trump_stone_background, (trump_stone_background_rect[0] + 88, trump_stone_background_rect[1] + trump_stone_background_y))
                        pygame.display.flip()
                        if t1 == 3:
                            pass
                        else:
                            screen.blit(stones[stone_random[right_to_left_stone_count + 3]], stone_cells_coords[right_to_left_block[right_to_left_block_step][0]])
                            pygame.display.flip()
                        for i in range(3):
                            quit_escape()
                            screen.blit(stones[stone_random[right_to_left_stone_count + i]], stone_cells_coords[right_to_left_stone_count + 3 - i])
                            pygame.display.flip()

            if t1 == 3:
                right_to_left_stone_count += 3
            else:
                right_to_left_stone_count += 4
                
            right_to_left_stone_move_count = 0
            right_to_left_block_step += 1
            right_to_left_stone_move_step = 0
            right_to_left_stone_move_step_first = 0
            right_to_left_stone_move_step_second = 0
            right_to_left_stone_move_step_second_bool = False        
            right_to_left_stone_move_step_third = 0
            right_to_left_stone_move_step_third_bool = False
            right_to_left_stone_move_count = 0
            trump_stone_background_y += 88   
#------------------------------------------------------------------------------------------------------------------#    
    #def of trump stones to style show all at the same time
    def show_all_stones_at_the_same_time():        
        for i in range(1, 255, 15):
            for stone_step in range(15):
                stones[stone_random[stone_step]].set_alpha(i)                
                screen.blit(stones[stone_random[stone_step]], stone_cells_coords[stone_step])
                pygame.display.flip()
                clock.tick(200)
#------------------------------------------------------------------------------------------------------------------#            
    #def of trump stones to style zigzag 
    def stone_zigzag_trump():
        push_down_stone_sound = pygame.mixer.Sound('fx/push_down_stone_sound.wav')
        push_down_stone_sound.set_volume(0.8)
        push_down_stone_sound_bool = True
        
        zigzag_alpha_step = 17
        zigzag_clock_fps = 30
        zigzag_bool = True
        zigzag_stone_count = 0                
        zigzag_block = [[0, 12], [1, 13], [2, 14], [3, 15], [3, 11], [2, 10], [1, 9], [0, 8], [0, 4], [1, 5], [2, 6], [3, 7], [3, 3], [2, 2], [1, 1]]
        
        while zigzag_bool:
            quit_escape()
            if zigzag_stone_count == 13 or zigzag_stone_count == 14:
                zigzag_alpha_step = 34
                zigziag_clock_fps = 10
                clock.tick(zigzag_clock_fps)
                push_down_stone_sound.play()
                stone_collision.play()
            
            for i in range(1, 255, zigzag_alpha_step):
                stones[stone_random[zigzag_stone_count]].set_alpha(i)
                screen.blit(stones[stone_random[zigzag_stone_count]], stone_cells_coords[zigzag_block[zigzag_stone_count][0]])
                pygame.display.flip()
                clock.tick(zigzag_clock_fps)                   
                
            zigzag_stone_move = 0    
            while ((stone_cells_coords[zigzag_block[zigzag_stone_count][0]][1] + zigzag_stone_move) < stone_cells_coords[zigzag_block[zigzag_stone_count][1]][1]):
                if push_down_stone_sound_bool and (zigzag_stone_count != 13 or zigzag_stone_count != 14):
                    push_down_stone_sound_bool = False
                    push_down_stone_sound.play()
                screen.blit(stone_background_mini_UpDown, (stone_cells_coords[zigzag_block[zigzag_stone_count][0]][0], stone_cells_coords[zigzag_block[zigzag_stone_count][0]][1] + zigzag_stone_move))
                zigzag_stone_move += 11
                screen.blit(stones[stone_random[zigzag_stone_count]], (stone_cells_coords[zigzag_block[zigzag_stone_count][0]][0], stone_cells_coords[zigzag_block[zigzag_stone_count][0]][1] + zigzag_stone_move))
                pygame.display.flip()
                clock.tick(60)
                if ((stone_cells_coords[zigzag_block[zigzag_stone_count][0]][1] + zigzag_stone_move + zigzag_stone_move) == stone_cells_coords[zigzag_block[zigzag_stone_count][1]][1]):
                    push_down_stone_sound.stop()
                    stone_collision.play()
                    push_down_stone_sound_bool = True
                    
            zigzag_stone_count += 1                         
            if zigzag_stone_count == 15:
                zigzag_bool = False
#------------------------------------------------------------------------------------------------------------------#    
    #def of trump stones to style square in the corners
    def square_of_corner():
        stone_of_corner_sound = pygame.mixer.Sound('fx/stone_of_corner_sound.wav')
        stone_of_corner_sound.set_volume(0.8)
        corner_stone_coords = [[2, 6, 3, 7], [8, 12, 9, 13], [0, 4, 1, 5], [10, 14, 11]]
        stone_random_step = 0
        for s in range(4):
            stone_of_corner_sound.stop()
            stone_of_corner_sound.play()
            for stone_step in range(len(corner_stone_coords[s])):
                for i in range(1, 255, 10):
                    stones[stone_random[stone_random_step]].set_alpha(i)
                    screen.blit(stones[stone_random[stone_random_step]], stone_cells_coords[corner_stone_coords[s][stone_step]])
                    pygame.display.flip()
                    clock.tick(150)
                stone_random_step += 1
#------------------------------------------------------------------------------------------------------------------#
    #def show players best score
    def show_players_best_score(game_main_music_step, score_file_bool):
        #initialization player_best_score_background
        player_best_score_background = pygame.image.load('player_best_score_background.jpg').convert()
        player_best_score_background = pygame.transform.scale(player_best_score_background, (460, 540))
        player_best_score_background_rect = (MAX_X//2 - 230, MAX_Y // 2 - 270)

        anubis_exit_image = pygame.image.load('anubis_exit_image.jpg').convert()
        anubis_exit_image = pygame.transform.scale(anubis_exit_image, (200, 300))
        anubis_exit_image_rect = (MAX_X//2 - 100, MAX_Y // 2 - 150)        
        #buttons parametrs
        button_font_size = 15
        button_font_name = pygame.font.Font('font/PAPYRUS.TTF', button_font_size)
        button_font_name.set_bold(True)
        #parametrs again button
        again_button_text = 'AGAIN'
        again_button_rect = (player_best_score_background_rect[0] + 50, 470)
        again_button_surface = button_font_name.render(again_button_text, True, player_colors[0])
        again_button_font_x = (again_button_rect[0] + 50 - again_button_surface.get_width() // 2)
        again_button_font_y = again_button_rect[1] + 15
        #parametrs exit button
        over_button_text = 'EXIT'
        over_button_rect = (player_best_score_background_rect[0] + 180, 470)
        over_button_surface = button_font_name.render(over_button_text, True, player_colors[0])
        over_button_font_x = (over_button_rect[0] + 50 - over_button_surface.get_width() // 2)
        over_button_font_y = over_button_rect[1] + 15
        #parametrs credit button 
        credit_button_text = 'CREDIT'
        credit_button_rect = (player_best_score_background_rect[0] + 310, 470)        
        credit_button_surface = button_font_name.render(credit_button_text, True, player_colors[0])
        credit_button_font_x = (credit_button_rect[0] + 50 - credit_button_surface.get_width() // 2)
        credit_button_font_y = credit_button_rect[1] + 15
        #winner player name color
        blue = (3, 2, 80)
        blue1 = (6, 3, 143)
        blue2 = (11, 5, 218)
        blue3 = (45, 39, 250)
        blue4 = (125, 122, 252)
        blue5 = (213, 211, 254)    
        win_player_name_font_color = [blue, blue1, blue2, blue3, blue4, blue5]
        win_player_name_font_color_step = 0
        #if the player won the game, then it is added to the file: win hi score - whs
        yes_win_player_in_top_score_bool = False
        win_player_time_fix = 0
        find_file_bool = True
        find_file_text = ['The file was not found', 'and will be created']
        find_file_x = player_best_score_background_rect[0] 
        find_file_y = player_best_score_background_rect[0] + 50
        file_not_found_sound = pygame.mixer.Sound('fx/file_not_found_sound.wav')
        file_not_found_sound.set_volume(0.8)
        if score_file_bool:
            try:
                with open('score/hiScore.txt', 'a') as whs:                
                    whs.write('\n'f'{playerName}:{str(hour_left)}{str(hour_right)}{str(minutes_left)}{str(minutes_right)}{str(seconds_left)}{str(seconds_right)}')
                win_player_time_fix = hour_left * 100000 + hour_right * 10000 + minutes_left * 1000 + minutes_right * 100 + seconds_left * 10 + seconds_right
                whs.close()
            except FileNotFoundError:
                pass
                
        buttons_color_step = 0
        #show player_best_score_background
        for bs in range(0, 255, 15):
            quit_escape()
            player_best_score_background.set_alpha(bs)
            screen.blit(player_best_score_background, player_best_score_background_rect)
            pygame.display.flip()
            clock.tick(15)
        #font to show best score
        best_score_font_size = 20
        best_score_font_name = pygame.font.Font('font/PAPYRUS.TTF', best_score_font_size)
        best_score_font_name.set_bold(True)
        best_score_font_color = (127, 0, 0)        
        best_score_x = (player_best_score_background_rect[0] + 60)
        best_score_y = (player_best_score_background_rect[1] + 120)
        #head best score
        head_best_score_text = '--- BEST  SCORE ---'        
        head_best_score_y = (player_best_score_background_rect[1] + 60)
        head_best_score_surface = best_score_font_name.render(head_best_score_text, True, finish_line_color[0])
        head_best_score_x = (player_best_score_background_rect[0] + 230 - head_best_score_surface.get_width() // 2)
        screen.blit(head_best_score_surface, (head_best_score_x, head_best_score_y))
        
        head_best_score_player_time_text = ['Players', 'h', 'm', 's']
        head_best_score_time_y = (player_best_score_background_rect[1] + 90)
        head_best_score_time_x = (player_best_score_background_rect[0] + 318)
        for t in range(4):
            if t == 0:
                head_best_score_time_surface = best_score_font_name.render(head_best_score_player_time_text[t], True, finish_line_color[0])
                screen.blit(head_best_score_time_surface, (head_best_score_time_x - 240, head_best_score_time_y))
            else:    
                head_best_score_time_surface = best_score_font_name.render(head_best_score_player_time_text[t], True, finish_line_color[0])
                screen.blit(head_best_score_time_surface, (head_best_score_time_x, head_best_score_time_y))
                pygame.display.flip()
                head_best_score_time_x += 31
        
        #open and read file
        try:
            f = open('score/hiScore.txt')
            f.close()
        except FileNotFoundError:
            find_file_bool = False
                
        if find_file_bool:
            with open ('score/hiScore.txt') as hs:
                values = hs.readlines()

            clean_values = []
            for content in values:
                clean_values.append(content.strip())
                
            list_for_sort_to_hs = []
            for i in range(len(clean_values)):
                list_for_sort_to_hs.append([clean_values[i][-6:], clean_values[i][:len(clean_values[i]) - 7]])

            list_for_sort_to_hs.sort()
            #show hi score players and fix position winner player       
            number_hi_score = 1
            fix_position_win_player = 0
            first_fix_position_win_player_bool = True
            yes_win_player_in_top_score_bool = False
            for i in range(len(list_for_sort_to_hs)):
                #fix position in best score winner player
                if score_file_bool:
                    if first_fix_position_win_player_bool:
                        if (playerName == list_for_sort_to_hs[i][1]) and (win_player_time_fix == int('{}{}{}'.format(list_for_sort_to_hs[i][0][:2], list_for_sort_to_hs[i][0][2:4], list_for_sort_to_hs[i][0][4:]))):
                            fix_position_win_player = i
                            first_fix_position_win_player_bool = False
                            yes_win_player_in_top_score_bool = True
                #show hi score players    
                best_score_surface = best_score_font_name.render('{}.{}'.format(number_hi_score, list_for_sort_to_hs[i][1]), True, best_score_font_color)
                screen.blit(best_score_surface, (best_score_x, best_score_y))        
                pygame.display.flip()
                best_score_x = (player_best_score_background_rect[0] + 310)
                best_score_surface = best_score_font_name.render('{}:{}:{}'.format(list_for_sort_to_hs[i][0][:2], list_for_sort_to_hs[i][0][2:4], list_for_sort_to_hs[i][0][4:]), True, best_score_font_color)
                screen.blit(best_score_surface, (best_score_x, best_score_y))        
                pygame.display.flip()
                clock.tick(5)
                best_score_y += 40
                best_score_x = (player_best_score_background_rect[0] + 60)
                number_hi_score += 1
                if number_hi_score == 8:
                    break
        else:
            file_not_found_sound.play()
            find_file_surface = best_score_font_name.render(find_file_text[0], True, (127, 0, 0))
            find_file_x = player_best_score_background_rect[0] + 230 - find_file_surface.get_width() // 2
            screen.blit(find_file_surface, (find_file_x, find_file_y))
            pygame.display.flip()
            find_file_y += 30
            find_file_surface = best_score_font_name.render(find_file_text[1], True, (127, 0, 0))
            find_file_x = player_best_score_background_rect[0] + 230 - find_file_surface.get_width() // 2
            screen.blit(find_file_surface, (find_file_x, find_file_y))
            pygame.display.flip()
            f = open('score/hiScore.txt', 'w')
            f.close()
        #show buttons
        for i in range(0, 255, 15):
            quit_escape()
            push_stop_button.set_colorkey((255, 255, 255))
            push_stop_button.set_alpha(i)
            screen.blit(push_stop_button, again_button_rect)
            screen.blit(push_stop_button, over_button_rect)
            screen.blit(push_stop_button, credit_button_rect)
            pygame.display.flip()
            clock.tick(30)            
        #select game: a new game, game over, credit     
        select_game_bool = True
        push_button_surface_color_bool = True
        player_color_bool = True
        while select_game_bool:
            #get ending music track 
            if pygame.mixer.music.get_pos() == -1:
                game_main_music_step += 1 
                if game_main_music_step > 4:
                    game_main_music_step = 0
                pygame.mixer.music.load(game_main_musics[game_main_music_step])
                pygame.mixer.music.play(1, 0.0)                
            #reading events                               
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()                
                #push game process
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    #if press button again
                    if (mouse_x >= again_button_rect[0] and mouse_x <= again_button_rect[0] + 99) and (mouse_y >= again_button_rect[1] and mouse_y <= again_button_rect[1] + 79):                    
                        pressed = pygame.mouse.get_pressed()
                        if pressed[0] == 1:
                            press_down_stone_sound.set_volume(0.4)
                            press_down_stone_sound.play()
                            again_button_surface = button_font_name.render(again_button_text, True, black)
                            over_button_surface = button_font_name.render(over_button_text, True, player_colors[0])
                            credit_button_surface = button_font_name.render(over_button_text, True, player_colors[0])
                            again_button_font_x = (again_button_rect[0] + 50 - again_button_surface.get_width() // 2)
                            press_button.set_colorkey((255, 255, 255))
                            screen.blit(press_button, again_button_rect)
                            screen.blit(again_button_surface, (again_button_font_x, again_button_font_y))                        
                            pygame.display.flip()
                            select_game_bool = False
                            push_button_surface_color_bool = False
                            vol = 0                                            
                            for i in range(4):
                                quit_escape()
                                pygame.mixer.music.set_volume(0.4 - vol)
                                vol += 0.1
                                clock.tick(3)
                            #get def of player_name()
                            game_main_music_step += 1 
                            if game_main_music_step > 4:
                                game_main_music_step = 0
                            player_name(game_main_music_step, random_trump_stones)
                    #if press button exit
                    elif (mouse_x >= over_button_rect[0] and mouse_x <= over_button_rect[0] + 99) and (mouse_y >= over_button_rect[1] and mouse_y <= over_button_rect[1] + 79):                    
                        pressed = pygame.mouse.get_pressed()
                        if pressed[0] == 1:
                            press_down_stone_sound.set_volume(0.4)
                            press_down_stone_sound.play()
                            over_button_surface = button_font_name.render(over_button_text, True, black)
                            again_button_surface = button_font_name.render(again_button_text, True, player_colors[0])
                            credit_button_surface = button_font_name.render(credit_button_text, True, player_colors[0])
                            over_button_font_x = (over_button_rect[0] + 50 - over_button_surface.get_width() // 2)
                            press_button.set_colorkey((255, 255, 255))
                            screen.blit(press_button, over_button_rect)
                            screen.blit(over_button_surface, (over_button_font_x, over_button_font_y))                        
                            pygame.display.flip()
                            select_game_bool = False
                            push_button_surface_color_bool = False
                            #screen fill black                            
                            for j in range(0, 255, 10):
                                quit_escape()                                
                                screen_fill_black.set_alpha(j)
                                screen.blit(screen_fill_black, (0,0))
                                pygame.display.flip()
                                clock.tick(15)
                            #show anubis_image_image
                            for j in range(0, 120, 5):
                                quit_escape()                                
                                anubis_exit_image.set_alpha(j)
                                screen.blit(anubis_exit_image, anubis_exit_image_rect)
                                pygame.display.flip()
                                clock.tick(8)
                                
                            anubis_word = 'See you soon, Wanderer!'
                            anubis_word_color = (232, 8, 0)
                            anubis_word_font_size = 30
                            anubis_word_font_name = pygame.font.Font('font/PAPYRUS.TTF', anubis_word_font_size)
                            anubis_word_font_name.set_bold(True)
                            anubis_word_surface = anubis_word_font_name.render(anubis_word, True, anubis_word_color)    
                            anubis_word_font_x = (MAX_X // 2 - anubis_word_surface.get_width() // 2)
                            anubis_word_font_y = anubis_exit_image_rect[1] + 320

                            anubis_word_step = ''
                            for i in range(23):
                                quit_escape()
                                anubis_word_step += anubis_word[i]
                                anubis_word_surface = anubis_word_font_name.render(anubis_word_step, True, anubis_word_color)    
                                screen.blit(anubis_word_surface, (anubis_word_font_x, anubis_word_font_y))            
                                pygame.display.flip()
                                clock.tick(10)
                                                                        
                            vol = 0                                            
                            for i in range(4):
                                quit_escape()
                                pygame.mixer.music.set_volume(0.4 - vol)
                                vol += 0.1
                                clock.tick(3)
                            #exit game
                            pygame.quit()
                            sys.exit()
                    #if press button credit
                    elif (mouse_x >= credit_button_rect[0] and mouse_x <= credit_button_rect[0] + 99) and (mouse_y >= credit_button_rect[1] and mouse_y <= credit_button_rect[1] + 79):                    
                        pressed = pygame.mouse.get_pressed()
                        if pressed[0] == 1:
                            press_down_stone_sound.set_volume(0.4)
                            press_down_stone_sound.play()
                            credit_button_surface = button_font_name.render(credit_button_text, True, black)
                            again_button_surface = button_font_name.render(again_button_text, True, player_colors[0])
                            over_button_surface = button_font_name.render(over_button_text, True, player_colors[0])
                            credit_button_font_x = (credit_button_rect[0] + 50 - credit_button_surface.get_width() // 2)
                            press_button.set_colorkey((255, 255, 255))
                            screen.blit(press_button, credit_button_rect)
                            screen.blit(credit_button_surface, (credit_button_font_x, credit_button_font_y))                        
                            pygame.display.flip()
                            select_game_bool = False
                            push_button_surface_color_bool = False
                            vol = 0                                            
                            for i in range(4):
                                quit_escape()
                                pygame.mixer.music.set_volume(0.4 - vol)
                                vol += 0.1
                                clock.tick(3)
                            #get def of credit_game()
                            credit_game()
                            
            if push_button_surface_color_bool:
                again_button_surface = button_font_name.render(again_button_text, True, player_colors[buttons_color_step])
                again_button_font_x = (again_button_rect[0] + 50 - again_button_surface.get_width() // 2)
                screen.blit(again_button_surface, (again_button_font_x, again_button_font_y))
                over_button_surface = button_font_name.render(over_button_text, True, player_colors[buttons_color_step])
                over_button_font_x = (over_button_rect[0] + 50 - over_button_surface.get_width() // 2)
                screen.blit(over_button_surface, (over_button_font_x, over_button_font_y))
                credit_button_surface = button_font_name.render(credit_button_text, True, player_colors[buttons_color_step])
                credit_button_font_x = (credit_button_rect[0] + 50 - credit_button_surface.get_width() // 2)
                screen.blit(credit_button_surface, (credit_button_font_x, credit_button_font_y))
                pygame.display.flip()
                clock.tick(30)
                if player_color_bool:
                    buttons_color_step += 1
                    if buttons_color_step == 5:
                        player_color_bool = False
                else:
                    buttons_color_step -= 1
                    if buttons_color_step == 0:
                        player_color_bool = True
            #change color winner player's name and time parametrs
            if yes_win_player_in_top_score_bool:
                best_score_x = (player_best_score_background_rect[0] + 60)
                best_score_y = (player_best_score_background_rect[1] + 120)
                best_score_surface = best_score_font_name.render('{}.{}'.format(fix_position_win_player + 1, list_for_sort_to_hs[fix_position_win_player][1]), True, win_player_name_font_color[win_player_name_font_color_step])
                screen.blit(best_score_surface, (best_score_x, best_score_y + 40*fix_position_win_player))        
                pygame.display.flip()
                best_score_x = (player_best_score_background_rect[0] + 310)
                best_score_surface = best_score_font_name.render('{}:{}:{}'.format(list_for_sort_to_hs[fix_position_win_player][0][:2], list_for_sort_to_hs[fix_position_win_player][0][2:4], list_for_sort_to_hs[fix_position_win_player][0][4:]), True, win_player_name_font_color[win_player_name_font_color_step])
                screen.blit(best_score_surface, (best_score_x, best_score_y + 40*fix_position_win_player))        
                pygame.display.flip()
                clock.tick(30)
                win_player_name_font_color_step += 1
                if win_player_name_font_color_step == 6:
                    win_player_name_font_color_step = 0                
#------------------------------------------------------------------------------------------------------------------#                    
    #def of verify cells is empty or not
    def notNoneCell(i):
        for j in range(len(stone_move_cells[i])):
            if (game_stone_register[stone_move_cells[i][j]] == -1):
                return False
        return True
#------------------------------------------------------------------------------------------------------------------#
    #def of identify cells is empty and direction
    #direction position parametrs: 1 - left, 2 - right, 3 - up, 4 - down 
    def identifyDirection (i):
        fix_position_cells = 0
        for j in range(len(stone_move_cells[i])):
            if (game_stone_register[stone_move_cells[i][j]] == -1):
                fix_position_cells = stone_move_cells[i][j]                
                break
        if (fix_position_cells - i) == -1:
            return True, False, False, False, fix_position_cells
        elif (fix_position_cells - i) == 1:
            return False, True, False, False, fix_position_cells
        elif (fix_position_cells - i) == -4:
            return False, False, True, False, fix_position_cells
        elif (fix_position_cells - i) == 4:
            return False, False, False, True, fix_position_cells
#------------------------------------------------------------------------------------------------------------------#
    #def is move stone specified parameters
    def stone_move_to_directions(move_left, move_right, move_up, move_down, will_move_cell, not_stone, milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left):
        stone_move.set_volume(0.8)
        stone_collision.set_volume(0.8)
        if move_left:
            stone_move_step = 0
            stone_move.play()
            while ((stone_cells_coords[will_move_cell][0] - stone_move_step) > stone_cells_coords[not_stone][0]):
                screen.blit(stone_background_mini_RightLeft, (stone_cells_coords[will_move_cell][0] + 75 - stone_move_step, stone_cells_coords[will_move_cell][1]))
                stone_move_step += 11
                milliseconds += clock.tick_busy_loop(60)
                milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left = game_timer(milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left)        
                screen.blit(stones[game_stone_register[will_move_cell]], (stone_cells_coords[will_move_cell][0] - stone_move_step, stone_cells_coords[will_move_cell][1]))
                pygame.display.flip()
                clock.tick(60)
                if ((stone_cells_coords[will_move_cell][0] - stone_move_step - 11) == stone_cells_coords[not_stone][0]):
                    stone_move.stop()
                    stone_collision.play()            
        elif move_right:
            stone_move_step = 0
            stone_move.play()
            while ((stone_cells_coords[will_move_cell][0] + stone_move_step) < stone_cells_coords[not_stone][0]):
                screen.blit(stone_background_mini_RightLeft, (stone_cells_coords[will_move_cell][0] + stone_move_step, stone_cells_coords[will_move_cell][1]))
                stone_move_step += 11
                milliseconds += clock.tick_busy_loop(60)
                milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left = game_timer(milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left)
                screen.blit(stones[game_stone_register[will_move_cell]], (stone_cells_coords[will_move_cell][0] + stone_move_step, stone_cells_coords[will_move_cell][1]))
                pygame.display.flip()
                clock.tick(60)
                if ((stone_cells_coords[will_move_cell][0] + stone_move_step + 11) == stone_cells_coords[not_stone][0]):
                    stone_move.stop()
                    stone_collision.play()
        elif move_up:
            stone_move_step = 0
            stone_move.play()
            while ((stone_cells_coords[will_move_cell][1] - stone_move_step) > stone_cells_coords[not_stone][1]):
                screen.blit(stone_background_mini_UpDown, (stone_cells_coords[will_move_cell][0], stone_cells_coords[will_move_cell][1] + 75 - stone_move_step))
                stone_move_step += 11
                milliseconds += clock.tick_busy_loop(60)
                milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left = game_timer(milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left)        
                screen.blit(stones[game_stone_register[will_move_cell]], (stone_cells_coords[will_move_cell][0], stone_cells_coords[will_move_cell][1] - stone_move_step))
                pygame.display.flip()
                clock.tick(60)
                if ((stone_cells_coords[will_move_cell][1] - stone_move_step - 11) == stone_cells_coords[not_stone][1]):
                    stone_move.stop()
                    stone_collision.play()
        elif move_down:
            stone_move_step = 0
            stone_move.play()
            while ((stone_cells_coords[will_move_cell][1] + stone_move_step) < stone_cells_coords[not_stone][1]):
                screen.blit(stone_background_mini_UpDown, (stone_cells_coords[will_move_cell][0], stone_cells_coords[will_move_cell][1] + stone_move_step))
                stone_move_step += 11
                milliseconds += clock.tick_busy_loop(60)
                milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left = game_timer(milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left)
                screen.blit(stones[game_stone_register[will_move_cell]], (stone_cells_coords[will_move_cell][0], stone_cells_coords[will_move_cell][1] + stone_move_step))
                pygame.display.flip()
                clock.tick(60)
                if ((stone_cells_coords[will_move_cell][1] + stone_move_step + 11) == stone_cells_coords[not_stone][1]):
                    stone_move.stop()
                    stone_collision.play()          
        return milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left
#------------------------------------------------ MAIN GAME CENTER ------------------------------------------------#
    #game initialization
    #game_center_image
    game_center_image = pygame.image.load('game_center_image.png').convert()
    game_center_image = pygame.transform.scale(game_center_image, (MAX_X, MAX_Y))
    
    #arena and panel
    arena_for_stones = pygame.image.load('arena_for_stones.png').convert()
    arena_for_stones = pygame.transform.scale(arena_for_stones, (500, 500))
    arena_for_stones_rect = (MAX_X//2 - 440, MAX_Y // 2 - 250)

    panel_for_indicator = pygame.image.load('panel_for_indicator.png').convert()
    panel_for_indicator = pygame.transform.scale(panel_for_indicator, (375, 500))
    panel_for_indicator_rect = (MAX_X//2 + 65, MAX_Y // 2 - 250)
    
    #stones
    stone1 = pygame.image.load('stone/stone1.png').convert()
    stone1 = pygame.transform.scale(stone1, (86, 86))
    
    stone2 = pygame.image.load('stone/stone2.png').convert()
    stone2 = pygame.transform.scale(stone2, (86, 86))
    
    stone3 = pygame.image.load('stone/stone3.png').convert()
    stone3 = pygame.transform.scale(stone3, (86, 86))
    
    stone4 = pygame.image.load('stone/stone4.png').convert()
    stone4 = pygame.transform.scale(stone4, (86, 86))
    
    stone5 = pygame.image.load('stone/stone5.png').convert()
    stone5 = pygame.transform.scale(stone5, (86, 86))
    
    stone6 = pygame.image.load('stone/stone6.png').convert()
    stone6 = pygame.transform.scale(stone6, (86, 86))
    
    stone7 = pygame.image.load('stone/stone7.png').convert()
    stone7 = pygame.transform.scale(stone7, (86, 86))
    
    stone8 = pygame.image.load('stone/stone8.png').convert()
    stone8 = pygame.transform.scale(stone8, (86, 86))
    
    stone9 = pygame.image.load('stone/stone9.png').convert()
    stone9 = pygame.transform.scale(stone9, (86, 86))
    
    stone10 = pygame.image.load('stone/stone10.png').convert()
    stone10 = pygame.transform.scale(stone10, (86, 86))
    
    stone11 = pygame.image.load('stone/stone11.png').convert()
    stone11 = pygame.transform.scale(stone11, (86, 86))
    
    stone12 = pygame.image.load('stone/stone12.png').convert()
    stone12 = pygame.transform.scale(stone12, (86, 86))
    
    stone13 = pygame.image.load('stone/stone13.png').convert()
    stone13 = pygame.transform.scale(stone13, (86, 86))
    
    stone14 = pygame.image.load('stone/stone14.png').convert()
    stone14 = pygame.transform.scale(stone14, (86, 86))
    
    stone15 = pygame.image.load('stone/stone15.png').convert()
    stone15 = pygame.transform.scale(stone15, (86, 86))
    #main rect stones
    stone_rect = (arena_for_stones_rect[0] + 76, arena_for_stones_rect[1] + 76)
    
    #stone list 
    stones = [stone1, stone2, stone3, stone4, stone5, stone6, stone7, stone8, stone9, stone10, stone11, stone12, stone13, stone14, stone15]
    
    #stone cells coords
    stone_cells_coords = {0:(stone_rect[0], stone_rect[1]), 1:(stone_rect[0] + 88, stone_rect[1]), 2:(stone_rect[0] + 88*2, stone_rect[1]), 3:(stone_rect[0] + 88*3, stone_rect[1]), 4:(stone_rect[0], stone_rect[1] + 88), 5:(stone_rect[0] + 88, stone_rect[1] + 88), 6:(stone_rect[0] + 88*2, stone_rect[1] + 88), 7:(stone_rect[0] + 88*3, stone_rect[1] + 88), 8:(stone_rect[0], stone_rect[1] + 88*2), 9:(stone_rect[0] + 88, stone_rect[1] + 88*2), 10:(stone_rect[0] + 88*2, stone_rect[1] + 88*2), 11:(stone_rect[0] + 88*3, stone_rect[1] + 88*2), 12:(stone_rect[0], stone_rect[1] + 88*3), 13:(stone_rect[0] + 88, stone_rect[1] + 88*3), 14:(stone_rect[0] + 88*2, stone_rect[1] + 88*3), 15:(stone_rect[0] + 88*3, stone_rect[1] + 88*3)}
    
    #stone can move cells
    stone_move_cells = {0:(1, 4), 1:(0, 2, 5), 2:(1, 3, 6), 3:(2, 7), 4:(0, 5, 8), 5:(1, 4, 6, 9), 6:(2, 5, 7, 10), 7:(3, 6, 11), 8:(4, 9, 12), 9:(5, 8, 10, 13), 10:(6, 9, 11, 14), 11:(7, 10, 15), 12:(8, 13), 13:(9, 12, 14), 14:(10, 13, 15), 15:(11, 14)}
    
    #creat stone and shuffle
    stone_random = list(range(15))
    random.shuffle(stone_random)
    
    #stone background
    stone_background = pygame.image.load('stone/stone_background1.png').convert()
    stone_background = pygame.transform.scale(stone_background, (88, 88))
    stone_background_rect = (arena_for_stones_rect[0] + 75, arena_for_stones_rect[1] + 75)

    stone_background_mini_RightLeft = pygame.image.load('stone/stone_background1.png').convert()
    stone_background_mini_RightLeft = pygame.transform.scale(stone_background_mini_RightLeft, (11, 88))
    
    stone_background_mini_UpDown = pygame.image.load('stone/stone_background1.png').convert()
    stone_background_mini_UpDown = pygame.transform.scale(stone_background_mini_UpDown, (88, 11))
    
    #panel player name
    panel_name_player = pygame.image.load('panel_name_player.png').convert()
    panel_name_player = pygame.transform.scale(panel_name_player, (320, 80))
    panel_name_player_rect = (panel_for_indicator_rect[0] + 375 // 2 - 160, panel_for_indicator_rect[1] + 30)
    
    #label_for_time_and_turn and clear it
    label_for_time_and_turn = pygame.image.load('label_for_time_and_turn.png').convert()
    label_for_time_and_turn = pygame.transform.scale(label_for_time_and_turn, (160, 80))
    label_for_time_and_turn_rect = (panel_name_player_rect[0], panel_name_player_rect[1] + 120)

    label_for_show_time_and_turn = pygame.image.load('label_for_show_time_and_turn.png').convert()
    label_for_show_time_and_turn = pygame.transform.scale(label_for_show_time_and_turn, (160, 80))
    label_for_show_time_and_turn_rect = (panel_name_player_rect[0] + 160, panel_name_player_rect[1] + 120)

    label_for_clear_time_and_turn = pygame.image.load('label_for_clear_time_and_turn.png').convert()
    label_for_clear_time_and_turn = pygame.transform.scale(label_for_clear_time_and_turn, (120, 45))
    label_for_clear_time_and_turn_rect = (panel_name_player_rect[0] + 180, panel_name_player_rect[1] + 135)

    #initialization progress bar image, font and messages
    progress_bar_image = pygame.image.load('progress_bar_image.jpg').convert()
    progress_bar_image = pygame.transform.scale(progress_bar_image, (320, 50))
    progress_bar_image_rect = (panel_for_indicator_rect[0] + 27, panel_for_indicator_rect[1] + 418)

    progress_bar_clear = pygame.image.load('progress_bar_clear.jpg').convert()
    progress_bar_clear = pygame.transform.scale(progress_bar_clear, (260, 35))
    progress_bar_clear_rect =(progress_bar_image_rect[0] + 30, progress_bar_image_rect[1] + 7) 
    
    progress_bar_image_texts = ('press push button', 'wait, trump process', 'start play', 'wrong turn!', 'you win!')
    progress_bar_image_font_size = 20
    progress_bar_image_font_name = pygame.font.Font('font/PAPYRUS.TTF', progress_bar_image_font_size)
    progress_bar_image_font_name.set_bold(True)
    progress_bar_image_font_y = progress_bar_image_rect[1] + 10
    progress_bar_image_surface = progress_bar_image_font_name.render(progress_bar_image_texts[0], True, (52, 120, 43))
    progress_bar_image_font_x = (progress_bar_image_rect[0] + 160 - progress_bar_image_surface.get_width() // 2)
        
    #push and stop buttons
    push_button_text = 'PUSH'
    stop_button_text = 'STOP'
    press_button = pygame.image.load('buttons/press_button.png').convert()
    press_button = pygame.transform.scale(press_button, (100, 50))
    push_press_button_rect = (panel_for_indicator_rect[0] + 50, 430)
    stop_press_button_rect = (panel_for_indicator_rect[0] + 220, 430)
    push_stop_button = pygame.image.load('buttons/push_stop_button.png').convert()
    push_stop_button = pygame.transform.scale(push_stop_button, (100, 50))
    press_down_stone_sound = pygame.mixer.Sound('fx/press_down_stone_sound.wav')       
    #game center music    
    game_main_musics = ['music/game_main_music1.mp3', 'music/game_main_music2.mp3', 'music/game_main_music3.mp3', 'music/game_main_music4.mp3', 'music/game_main_music5.mp3']
    pygame.mixer.music.load(game_main_musics[game_main_music_step])        
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(1, 0.0)            
    #sounds for stone
    stone_move = pygame.mixer.Sound('fx/stone_move2.wav')
    stone_collision = pygame.mixer.Sound('fx/stone_collision.wav')
    #sounds alince voice
    aliens_voice1_sound = pygame.mixer.Sound('fx/aliens_voice1_sound.wav')
    aliens_voice2_sound = pygame.mixer.Sound('fx/aliens_voice2_sound.wav')
    aliens_voice3_sound = pygame.mixer.Sound('fx/aliens_voice3_sound.wav')
    aliens_voices = [aliens_voice1_sound, aliens_voice2_sound, aliens_voice3_sound]
    
    #screen_fill_black
    screen_fill_black = pygame.image.load('screen_fill_black.png').convert()
    screen_fill_black = pygame.transform.scale(screen_fill_black, (MAX_X, MAX_Y))
    screen_fill_black_sound = pygame.mixer.Sound('fx/screen_fill_black_sound.wav')
    screen_fill_black_sound.set_volume(0.8)
    
    screen_fill_black_sound.play()
    for j in range(0, 255, 10):
        quit_escape()
        screen_fill_black.set_alpha(j)
        screen.blit(screen_fill_black, (0,0))
        pygame.display.flip()
        clock.tick(10)
        
    #show game center image
    for j in range(0, 200, 15):
        quit_escape()
        game_center_image.set_alpha(j)
        screen.blit(game_center_image, (0,0))
        pygame.display.flip()
        clock.tick(10)
        
    #draw arena without stones and panel indicators
    for j in range(0, 255, 15):
        quit_escape()
        arena_for_stones.set_alpha(j)
        panel_for_indicator.set_alpha(j)        
        screen.blit(arena_for_stones, arena_for_stones_rect)
        screen.blit(panel_for_indicator, panel_for_indicator_rect)         
        pygame.display.flip()
        clock.tick(10)
        
    #show buttons and label indicators 
    for j in range(0, 255, 15):
        quit_escape()
        panel_name_player.set_alpha(j)
        label_for_time_and_turn.set_alpha(j)
        label_for_show_time_and_turn.set_alpha(j)        
        push_stop_button.set_colorkey((255, 255, 255))
        press_button.set_colorkey((255, 255, 255))
        push_stop_button.set_alpha(j)
        press_button.set_alpha(j)
        screen.blit(panel_name_player, panel_name_player_rect)
        screen.blit(label_for_time_and_turn, label_for_time_and_turn_rect)
        screen.blit(label_for_time_and_turn, (label_for_time_and_turn_rect[0], label_for_time_and_turn_rect[1] + 90))
        screen.blit(label_for_show_time_and_turn, label_for_show_time_and_turn_rect)
        screen.blit(label_for_show_time_and_turn, (label_for_show_time_and_turn_rect[0], label_for_show_time_and_turn_rect[1] + 90))
        screen.blit(push_stop_button, push_press_button_rect)
        screen.blit(press_button, stop_press_button_rect)
        screen.blit(progress_bar_image, progress_bar_image_rect)
        pygame.display.flip()
        clock.tick(30)
        
    #initialization parametrs for show player name
    player_color1 = (255, 0, 151)
    player_color2 = (213, 0, 151)
    player_color3 = (150, 0, 151)
    player_color4 = (90, 0, 151)
    player_color5 = (58, 0, 151)
    black = (0, 0, 0)    
    player_colors = (player_color1, player_color2, player_color3, player_color4, player_color5, black)
    player_color_step = 0
    player_color_bool = True
    player_font_size = 25
    player_font_name = pygame.font.Font('font/PAPYRUS.TTF', player_font_size)
    player_font_name.set_bold(True)
    player_font_y = panel_name_player_rect[1] + 20
    player_name_surface = player_font_name.render(playerName, True, player_colors[0])
    player_font_x = (panel_name_player_rect[0] + 160 - player_name_surface.get_width() // 2)
    screen.blit(player_name_surface, (player_font_x, player_font_y))
    
    #initialization parametrs push and stop buttons
    push_button_font_size = 20
    push_button_font_name = pygame.font.Font('font/PAPYRUS.TTF', push_button_font_size)
    push_button_font_name.set_bold(True)
    push_button_font_y = push_press_button_rect[1] + 10
    push_button_surface = push_button_font_name.render(push_button_text, True, (27, 15, 255))
    push_button_font_x = (push_press_button_rect[0] + 50 - push_button_surface.get_width() // 2)
    screen.blit(push_button_surface, (push_button_font_x, push_button_font_y))

    stop_button_font_size = 20
    stop_button_font_name = pygame.font.Font('font/PAPYRUS.TTF', push_button_font_size)
    stop_button_font_name.set_bold(True)
    stop_button_font_y = stop_press_button_rect[1] + 10
    stop_button_surface = stop_button_font_name.render(stop_button_text, True, black)
    stop_button_font_x = (stop_press_button_rect[0] + 50 - stop_button_surface.get_width() // 2)
    screen.blit(stop_button_surface, (stop_button_font_x, stop_button_font_y))
    
    #initialization parametrs for show timer and its indicators
    timer_text = 'Time'
    timer_font_size = 30
    timer_font_name = pygame.font.Font('font/PAPYRUS.TTF', timer_font_size)
    timer_font_name.set_bold(True)
    timer_font_y = label_for_time_and_turn_rect[1] + 15
    timer_name_surface = timer_font_name.render(timer_text, True, (27, 15, 255))
    timer_font_x = (label_for_time_and_turn_rect[0] + 80 - timer_name_surface.get_width() // 2)
    screen.blit(timer_name_surface, (timer_font_x, timer_font_y))        
    #timer with seconds and minutes
    time_show_color = [(27, 15, 255), (255, 0, 0)]    
    hour_left = 0
    hour_right = 0    
    minutes_left = 0
    minutes_right = 0
    seconds_left = 0
    seconds_right = 0
    milliseconds = 0
    timer_min_sec_size = 30
    timer_min_sec_font = pygame.font.Font('font/arial.ttf', timer_min_sec_size)    
    timer_min_sec_surface = timer_min_sec_font.render('{}{}:{}{}:{}{}'.format(hour_left, hour_right, minutes_left, minutes_right, seconds_left, seconds_right), True, time_show_color[0])
    timer_min_sec_y = label_for_show_time_and_turn_rect[1] + 23
    timer_min_sec_x = (label_for_show_time_and_turn_rect[0] + 80 - timer_min_sec_surface.get_width() // 2)
    screen.blit(timer_min_sec_surface, (timer_min_sec_x, timer_min_sec_y))
    #initialization parametrs for show turn and its indicators
    turn_text = 'Turns'
    turn_font_y = label_for_time_and_turn_rect[1] + 105
    turn_name_surface = timer_font_name.render(turn_text, True, (27, 15, 255))
    turn_font_x = (label_for_time_and_turn_rect[0] + 80 - turn_name_surface.get_width() // 2)
    screen.blit(turn_name_surface, (turn_font_x, turn_font_y))
    turn_step = 0
    turn_indicator_size = 30
    turn_indicator_font = pygame.font.Font('font/arial.ttf', turn_indicator_size)    
    turn_indicator_surface = turn_indicator_font.render('{}'.format(turn_step), True, time_show_color[0])
    turn_indicator_y = label_for_show_time_and_turn_rect[1] + 113
    turn_indicator_x = (label_for_show_time_and_turn_rect[0] + 80 - turn_indicator_surface.get_width() // 2)
    screen.blit(turn_indicator_surface, (turn_indicator_x, turn_indicator_y))     
    pygame.display.flip()
    
    #mouse setting
    pygame.mouse.set_visible(True)
    pressed = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #message progess bar
    screen.blit(progress_bar_image_surface, (progress_bar_image_font_x, progress_bar_image_font_y))
    #push game     
    push_game_bool = True
    push_button_surface_color_bool = True
    while push_game_bool:
        #get ending music track 
        if pygame.mixer.music.get_pos() == -1:
            game_main_music_step += 1 
            if game_main_music_step > 4:
                game_main_music_step = 0
            pygame.mixer.music.load(game_main_musics[game_main_music_step])
            pygame.mixer.music.play(1, 0.0)            
        #reading events                               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()            
            #push game process
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (mouse_x >= push_press_button_rect[0] and mouse_x <= push_press_button_rect[0] + 99) and (mouse_y >= push_press_button_rect[1] and mouse_y <= push_press_button_rect[1] + 79):                    
                    pressed = pygame.mouse.get_pressed()
                    if pressed[0] == 1:
                        #change the message progess bar
                        screen.blit(progress_bar_clear, progress_bar_clear_rect)
                        pygame.display.flip()
                        progress_bar_image_surface = progress_bar_image_font_name.render(progress_bar_image_texts[1], True, (232, 8, 0))
                        progress_bar_image_font_x = (progress_bar_image_rect[0] + 160 - progress_bar_image_surface.get_width() // 2)
                        screen.blit(progress_bar_image_surface, (progress_bar_image_font_x, progress_bar_image_font_y))
                        #play sound and change push button text
                        press_down_stone_sound.set_volume(0.4)
                        press_down_stone_sound.play()
                        push_button_surface = push_button_font_name.render(push_button_text, True, black)
                        push_button_font_x = (push_press_button_rect[0] + 50 - push_button_surface.get_width() // 2)
                        press_button.set_colorkey((255, 255, 255))
                        screen.blit(press_button, push_press_button_rect)
                        screen.blit(push_button_surface, (push_button_font_x, push_button_font_y))                        
                        pygame.display.flip()
                        push_game_bool = False
                        push_button_surface_color_bool = False

        if push_button_surface_color_bool:
            push_button_surface = push_button_font_name.render(push_button_text, True, player_colors[player_color_step])
            push_button_font_x = (push_press_button_rect[0] + 50 - push_button_surface.get_width() // 2)
            screen.blit(push_button_surface, (push_button_font_x, push_button_font_y))
            pygame.display.flip()
            clock.tick(30)
            if player_color_bool:
                player_color_step += 1
                if player_color_step == 5:
                    player_color_bool = False
            else:
                player_color_step -= 1
                if player_color_step == 0:
                    player_color_bool = True                
    #trump stones    
    if random_trump_stones == 0:
        #zigzag trump stones
        stone_zigzag_trump()
        #register stones position in cells
        game_stone_register = [-1, stone_random[14], stone_random[13], stone_random[12], stone_random[8], stone_random[9], stone_random[10], stone_random[11], stone_random[7], stone_random[6], stone_random[5], stone_random[4], stone_random[0], stone_random[1], stone_random[2], stone_random[3]]
    elif random_trump_stones == 1:
        #trump show all stones at the same time
        show_all_stones_at_the_same_time()
        #register stones position in cells
        game_stone_register = [stone_random[0], stone_random[1], stone_random[2], stone_random[3], stone_random[4], stone_random[5], stone_random[6], stone_random[7], stone_random[8], stone_random[9], stone_random[10], stone_random[11], stone_random[12], stone_random[13], stone_random[14], -1]
    elif random_trump_stones == 2:
        #right_to_left trump stones
        right_to_left()
        #register stones position in cells
        game_stone_register = [stone_random[0], stone_random[1], stone_random[2], stone_random[3], stone_random[7], stone_random[6], stone_random[5], stone_random[4], stone_random[8], stone_random[9], stone_random[10], stone_random[11], -1, stone_random[14], stone_random[13], stone_random[12]]
    elif random_trump_stones == 3:
        #square_of_corner
        square_of_corner()
        #register stones position in cells        
        game_stone_register = [stone_random[8], stone_random[10], stone_random[0], stone_random[2], stone_random[9], stone_random[11], stone_random[1], stone_random[3], stone_random[4], stone_random[6], stone_random[12], stone_random[14], stone_random[5], stone_random[7], stone_random[13], -1]    
    else:
        #up_to_down trump stones
        up_to_down()
        #register stones position in cells
        game_stone_register = [stone_random[3], stone_random[4], stone_random[11], stone_random[12], stone_random[2], stone_random[5], stone_random[10], stone_random[13], stone_random[1], stone_random[6], stone_random[9], stone_random[14], stone_random[0], stone_random[7], stone_random[8], -1]
    random_trump_stones += 1
    if random_trump_stones == 5:
        random_trump_stones = 0
    #change the message progess bar
    screen.blit(progress_bar_clear, progress_bar_clear_rect)
    pygame.display.flip()
    progress_bar_image_surface = progress_bar_image_font_name.render(progress_bar_image_texts[2], True, (52, 120, 43))
    progress_bar_image_font_x = (progress_bar_image_rect[0] + 160 - progress_bar_image_surface.get_width() // 2)
    screen.blit(progress_bar_image_surface, (progress_bar_image_font_x, progress_bar_image_font_y))    
    #initialization directions
    direct_left = False
    direct_right = False
    direct_up = False
    direct_down = False
    empty_cell = 0
    #player name color
    color_plus = True
    color_minus = False
    red_step = 0
    blue_step = 0
    green_step = 0
    #initialization mouse
    pressed = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #finish game effects
    finish_line_color = [(14, 52, 61), (21, 79, 91), (35, 130, 150), (48, 180, 207), (139, 213, 228), (255, 255, 255), (48, 59, 79)]    
    finish_line_color_step = 0
    finish_line_color_bool = True
    finish_sound = pygame.mixer.Sound('fx/finish_sound.wav')
    finish_sound.set_volume(0.8)
    finish_voice_of_victory_sound = pygame.mixer.Sound('fx/finish_voice_of_victory_sound.wav')
    finish_voice_of_victory_sound.set_volume(1.0)
    #stop_button after push game
    stop_button_surface = stop_button_font_name.render(stop_button_text, True, (27, 15, 255))
    stop_button_font_x = (stop_press_button_rect[0] + 50 - stop_button_surface.get_width() // 2)
    screen.blit(stop_button_surface, (stop_button_font_x, stop_button_font_y))
    push_stop_button.set_colorkey((255, 255, 255))
    screen.blit(push_stop_button, stop_press_button_rect)
    player_color_bool = True
    player_color_step = 0
    #main game loop
    game_loop = True
    while game_loop:
        if color_plus:
            red_step += 5
            if red_step > 255:
                red_step = 255
                green_step += 5
                if green_step > 255:
                    green_step = 255
                    blue_step += 5
                    if blue_step > 255:
                        blue_step = 255
                        color_plus = False
                        color_minus = True                            
        if color_minus:
            blue_step -= 5
            if blue_step < -1:
                blue_step = 0
                green_step -= 5
                if green_step < -1:
                    green_step = 0
                    red_step -= 5
                    if red_step < -1:
                        red_step = 0
                        color_plus = True
                        color_minus = False                        
        #get ending music track 
        if pygame.mixer.music.get_pos() == -1:
            game_main_music_step += 1 
            if game_main_music_step > 4:
                game_main_music_step = 0
            pygame.mixer.music.load(game_main_musics[game_main_music_step])
            pygame.mixer.music.play(1, 0.0)
        #reading events                               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()            
            #turn stone process
            if event.type == pygame.MOUSEBUTTONDOWN:
                if color_plus:
                    red_step += 5
                    if red_step > 255:
                        red_step = 255
                        green_step += 5
                        if green_step > 255:
                            green_step = 255
                            blue_step += 5
                            if blue_step > 255:
                                blue_step = 255
                                color_plus = False
                                color_minus = True                                    
                if color_minus:
                    blue_step -= 5
                    if blue_step < -1:
                        blue_step = 0
                        green_step -= 5
                        if green_step < -1:
                            green_step = 0
                            red_step -= 5
                            if red_step < -1:
                                red_step = 0
                                color_plus = True
                                color_minus = False
                #fix mouse coords 
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for index_cell in range(16):
                    if (mouse_x >= stone_cells_coords[index_cell][0] and mouse_x <= stone_cells_coords[index_cell][0] + 86) and (mouse_y >= stone_cells_coords[index_cell][1] and mouse_y <= stone_cells_coords[index_cell][1] + 86):
                        pressed = pygame.mouse.get_pressed()
                        if pressed[0] == 1:
                            #if walking is not correct
                            if game_stone_register[index_cell] == -1 or notNoneCell(index_cell):
                                #change the message progess bar
                                screen.blit(progress_bar_clear, progress_bar_clear_rect)
                                pygame.display.flip()
                                progress_bar_image_surface = progress_bar_image_font_name.render(progress_bar_image_texts[3], True, (232, 8, 0))
                                progress_bar_image_font_x = (progress_bar_image_rect[0] + 160 - progress_bar_image_surface.get_width() // 2)
                                screen.blit(progress_bar_image_surface, (progress_bar_image_font_x, progress_bar_image_font_y))
                                #play wrong turn sound
                                aliens_voices_random = random.randint(0,2)
                                aliens_voices[aliens_voices_random].stop()
                                aliens_voices[aliens_voices_random].set_volume(0.8)
                                aliens_voices[aliens_voices_random].play()                                
                            else:
                                #change the message progess bar
                                screen.blit(progress_bar_clear, progress_bar_clear_rect)
                                pygame.display.flip()
                                progress_bar_image_surface = progress_bar_image_font_name.render(progress_bar_image_texts[2], True, (52, 120, 43))
                                progress_bar_image_font_x = (progress_bar_image_rect[0] + 160 - progress_bar_image_surface.get_width() // 2)
                                screen.blit(progress_bar_image_surface, (progress_bar_image_font_x, progress_bar_image_font_y))
                                #clear and show turn indecators
                                screen.blit(label_for_clear_time_and_turn, (label_for_clear_time_and_turn_rect[0], label_for_clear_time_and_turn_rect[1] + 90))
                                pygame.display.flip()                                
                                turn_step += 1                                
                                turn_indicator_surface = turn_indicator_font.render('{}'.format(turn_step), True, time_show_color[1])
                                turn_indicator_x = (label_for_show_time_and_turn_rect[0] + 80 - turn_indicator_surface.get_width() // 2)
                                screen.blit(turn_indicator_surface, (turn_indicator_x, turn_indicator_y))
                                pygame.display.flip()
                                #identify direction and time fix                                
                                direct_left, direct_right, direct_up, direct_down, empty_cell = identifyDirection(index_cell)
                                milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left = stone_move_to_directions(direct_left, direct_right, direct_up, direct_down, index_cell, empty_cell, milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left)
                                game_stone_register[index_cell], game_stone_register[empty_cell] = game_stone_register[empty_cell], game_stone_register[index_cell]
                                #checking for ordering
                                finish_step = 0
                                for finish in range(15):
                                    if game_stone_register[finish] == finish:
                                        finish_step += 1
                                if finish_step == 15:
                                    #change the message progess bar
                                    screen.blit(progress_bar_clear, progress_bar_clear_rect)
                                    pygame.display.flip()
                                    progress_bar_image_surface = progress_bar_image_font_name.render(progress_bar_image_texts[4], True, (52, 120, 43))
                                    progress_bar_image_font_x = (progress_bar_image_rect[0] + 160 - progress_bar_image_surface.get_width() // 2)
                                    screen.blit(progress_bar_image_surface, (progress_bar_image_font_x, progress_bar_image_font_y))
                                    #play finish sound
                                    finish_sound.play()
                                    #show finish lines for win game
                                    for i in range(7):
                                            pygame.draw.line(screen, finish_line_color[i], (stone_cells_coords[0][0] + 87, stone_cells_coords[0][1]), (stone_cells_coords[12][0] + 87, stone_cells_coords[12][1] + 87), 2)
                                            pygame.draw.line(screen, finish_line_color[i], (stone_cells_coords[1][0] + 87, stone_cells_coords[1][1]), (stone_cells_coords[13][0] + 87, stone_cells_coords[13][1] + 87), 2)
                                            pygame.draw.line(screen, finish_line_color[i], (stone_cells_coords[2][0] + 87, stone_cells_coords[2][1]), (stone_cells_coords[14][0] + 87, stone_cells_coords[14][1] + 87), 2)
                                            pygame.draw.line(screen, finish_line_color[i], (stone_cells_coords[0][0], stone_cells_coords[0][1] + 87), (stone_cells_coords[3][0] + 87, stone_cells_coords[3][1] + 87), 2)
                                            pygame.draw.line(screen, finish_line_color[i], (stone_cells_coords[4][0], stone_cells_coords[4][1] + 87), (stone_cells_coords[7][0] + 87, stone_cells_coords[7][1] + 87), 2)
                                            pygame.draw.line(screen, finish_line_color[i], (stone_cells_coords[8][0], stone_cells_coords[8][1] + 87), (stone_cells_coords[11][0] + 87, stone_cells_coords[11][1] + 87), 2)
                                            pygame.draw.rect(screen, finish_line_color[i], (stone_cells_coords[15][0] - 1, stone_cells_coords[15][1] - 1, 87, 87))
                                            pygame.display.flip()
                                            clock.tick(10)                                           
                                    #play finish voice of victory
                                    finish_voice_of_victory_sound.play()
                                    #blink the message of win in the progress bar
                                    blink_bool = True
                                    for i in range(20):
                                        if blink_bool:
                                            screen.blit(progress_bar_clear, progress_bar_clear_rect)
                                            pygame.display.flip()
                                            clock.tick(10)
                                            blink_bool = False
                                        else:
                                            progress_bar_image_surface = progress_bar_image_font_name.render(progress_bar_image_texts[4], True, (52, 120, 43))
                                            progress_bar_image_font_x = (progress_bar_image_rect[0] + 160 - progress_bar_image_surface.get_width() // 2)
                                            screen.blit(progress_bar_image_surface, (progress_bar_image_font_x, progress_bar_image_font_y))
                                            pygame.display.flip()
                                            clock.tick(10)
                                            blink_bool = True
                                    #finish_game
                                    show_players_best_score(game_main_music_step, True)

                                break
                #verify press stop button
                if (mouse_x >= stop_press_button_rect[0] and mouse_x <= stop_press_button_rect[0] + 99) and (mouse_y >= stop_press_button_rect[1] and mouse_y <= stop_press_button_rect[1] + 79):                    
                    pressed = pygame.mouse.get_pressed()
                    if pressed[0] == 1:
                        press_down_stone_sound.set_volume(0.4)
                        press_down_stone_sound.play()
                        stop_button_surface = stop_button_font_name.render(stop_button_text, True, black)
                        stop_button_font_x = (stop_press_button_rect[0] + 50 - stop_button_surface.get_width() // 2)
                        press_button.set_colorkey((255, 255, 255))
                        screen.blit(press_button, stop_press_button_rect)
                        screen.blit(stop_button_surface, (stop_button_font_x, stop_button_font_y))                        
                        pygame.display.flip()
                        #get def show_players_best_score()
                        show_players_best_score(game_main_music_step, False)
                #change color player name
                player_name_surface = player_font_name.render(playerName, True, (red_step, blue_step, green_step))
                player_font_x = (panel_name_player_rect[0] + 160 - player_name_surface.get_width() // 2)
                screen.blit(player_name_surface, (player_font_x, player_font_y))
                pygame.display.flip()                
                #change color stop button name
                stop_button_surface = stop_button_font_name.render(stop_button_text, True, player_colors[player_color_step])
                stop_button_font_x = (stop_press_button_rect[0] + 50 - stop_button_surface.get_width() // 2)
                screen.blit(stop_button_surface, (stop_button_font_x, stop_button_font_y))
                pygame.display.flip()
                if player_color_bool:
                    player_color_step += 1
                    if player_color_step == 5:
                        player_color_bool = False
                else:
                    player_color_step -= 1
                    if player_color_step == 0:
                        player_color_bool = True                        
        #get milliseconds for time        
        clock.tick(60)
        milliseconds += clock.tick_busy_loop(60)
        milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left = game_timer(milliseconds, seconds_right, seconds_left, minutes_right, minutes_left, hour_right, hour_left)
        #change color player name
        player_name_surface = player_font_name.render(playerName, True, (red_step, blue_step, green_step))
        player_font_x = (panel_name_player_rect[0] + 160 - player_name_surface.get_width() // 2)
        screen.blit(player_name_surface, (player_font_x, player_font_y))
        pygame.display.flip()
        #change color stop button name
        stop_button_surface = stop_button_font_name.render(stop_button_text, True, player_colors[player_color_step])
        stop_button_font_x = (stop_press_button_rect[0] + 50 - stop_button_surface.get_width() // 2)
        screen.blit(stop_button_surface, (stop_button_font_x, stop_button_font_y))
        pygame.display.flip()
        if player_color_bool:
            player_color_step += 1
            if player_color_step == 5:
                player_color_bool = False
        else:
            player_color_step -= 1
            if player_color_step == 0:
                player_color_bool = True            
#********************************************************************************************************************************************************************#                          
#main screen size
MAX_X = 900
MAX_Y = 650
#initialization pygame  
pygame.init()
#initialization clock
clock = pygame.time.Clock()
#screen top center display 
os.environ['SDL_VIDEO_CENTERED'] = '1'
#set screen
screen = pygame.display.set_mode((MAX_X, MAX_Y))
#set caption
pygame.display.set_caption('Magic stone')
#set icon
icon = pygame.image.load('magic stone.png')
pygame.display.set_icon(icon)
#set mouse visible = True
pygame.mouse.set_visible(True)
#get def of intro()
intro()
#get def of player_name()
random_trump_stones = 0
game_main_music_step = 0
player_name(game_main_music_step, random_trump_stones)
