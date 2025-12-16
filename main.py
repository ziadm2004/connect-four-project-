import pygame
import time
# imports kolaha
from gui import C4_UI
from logic import G_Core
from ai import El_Bot
from audio import Sfx_Handler

def Run_Game():
    pygame.init()
    
    try:
        icon = pygame.image.load("pictures/icon.png")
        pygame.display.set_icon(icon)
    except:
        print("Icon mesh mawgooda.")
        pass
        
    # init
    ui = C4_UI()
    core = G_Core()
    sfx = Sfx_Handler()
    
    # states: -1 intro, 0 start, 1 modes, 2 diff
    # 3 le3b, 4 win, 5 lose, 6 transition, 7 tie, 8 end menu
    state = -1
    running = True
    
    # variables
    game_mode = None 
    ai_lvl = None
    ai_bot = None
    last_b_state = None
    t_timer = 0 # transition timer
    ai_busy = False
    next_st = None

    while running:
        # 50 ms delay
        pygame.time.delay(50) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if state == -1: # intro
                    if ui.clicked('intro_clk', (x, y)):
                        sfx.Click_Snd()
                        state = 0

                elif state == 0: # start
                    if ui.clicked('start_clk', (x, y)):
                        sfx.Click_Snd()
                        state = 1
                
                # selection menu
                elif state == 1: 
                    if ui.clicked('vs_ai_btn', (x, y)):
                        sfx.Click_Snd()
                        game_mode = "vs_ai"
                        state = 2
                    elif ui.clicked('vs_p_btn', (x, y)):
                        sfx.Click_Snd()
                        game_mode = "vs_p"
                        ai_lvl = None
                        ai_bot = None
                        core.reset_game()
                        state = 3

                elif state == 2: # difficulty
                    diff_map = {'easy_b':1, 'medium_b':2, 'hard_b':3, 'expert_b':4}
                    
                    for k, v in diff_map.items():
                        if ui.clicked(k, (x, y)):
                            sfx.Click_Snd()
                            ai_lvl = v
                            break # خلاص اخترنا صعوبة

                    if ai_lvl is not None:
                        ai_bot = El_Bot(d=ai_lvl)
                        core.reset_game()
                        state = 3

                # el le3b
                elif state == 3 and not core.end and not ai_busy:
                    
                    is_human = (core.curr_p == 'R' or (game_mode == "vs_p" and core.curr_p == 'Y'))

                    if is_human:
                        c = ui.get_col(x)
                        
                        if 0 <= c < 7:
                            if core.drop_piece(c):
                                sfx.Play_Drop()

                                # render 3ashan el drop yeban 3ala tool
                                ui.draw_game_scr(core.b, core.curr_p, game_mode, ai_lvl)
                                ui.refresh()

                                if core.end:
                                    last_b_state = [row[:] for row in core.b]
                                    t_timer = time.time() # start timer
                                    
                                    if core.win:
                                        if game_mode == "vs_p" or core.win == 'R':
                                            sfx.Win_Snd()
                                            next_st = 4 # win
                                        else:
                                            sfx.Lose_Snd()
                                            next_st = 5 # lose
                                    else:
                                        next_st = 7 # tie
                                        
                                    state = 6 # transition
                            else:
                                sfx.Error_Snd() # column malyan 7awel tany

                elif state == 8: # end menu
                    if ui.clicked('again', (x, y)):
                        sfx.Click_Snd()
                        core.reset_game()
                        state = 3
                    elif ui.clicked('menu_out', (x, y)):
                        sfx.Click_Snd()
                        state = 1
                # 3ashan lw 3amalt click fe screen el natiiga t7awel 3ala el menu 3ala tool
                elif state in [4, 5, 7]:
                    state = 8


        # AI turn logic
        # lazem el state yeb2a 3 we mesh khalsan we el ai msh meshghoul
        if (
            state == 3 and 
            not core.end and 
            not ai_busy and
            game_mode == "vs_ai" and 
            core.curr_p == 'Y'
        ):
            ai_busy = True # set the flag
            # 7agat 3ashan el feel
            pygame.time.delay(330)

            m = ai_bot.get_ai_move(core)

            if m is not None:
                if core.drop_piece(m):
                    sfx.Play_Ai() # sot el 7arka
                    
                    if core.end:
                        last_b_state = [row[:] for row in core.b]
                        t_timer = time.time()

                        if core.win == 'Y':
                            sfx.Lose_Snd()
                            next_st = 5 # lose
                        elif core.win == 'R':
                            sfx.Win_Snd()
                            next_st = 4 # win
                        else:
                            next_st = 7 # tie
                        
                        state = 6
                # mesh lazm else hna 3ashan el ai mfrod ma yla3bsh 3'alat
            
            ai_busy = False # reset the flag

        # transition logic
        if state == 6 and time.time() - t_timer > 0.77: # changed 0.75 to 0.77
            state = next_st
        
        # from result screen to end menu
        if state in [4, 5, 7] and time.time() - t_timer > 2.5:
            state = 8
        
        # DRAWING
        if state == -1: ui.intro_scr()
        elif state == 0: ui.start_scr()
        elif state == 1: ui.mode_scr()
        elif state == 2: ui.diff_scr()
        elif state == 3: ui.draw_game_scr(core.b, core.curr_p, game_mode, ai_lvl)
        elif state == 4: ui.winner_scr()
        elif state == 5: ui.loser_scr()
        elif state == 6: ui.draw_game_scr(last_b_state, core.curr_p, game_mode, ai_lvl) # show last board
        elif state == 7: ui.draw_tie_scr()
        elif state == 8: ui.end_scr()
        
        ui.refresh()

    pygame.quit()

if __name__ == "__main__":
    Run_Game()