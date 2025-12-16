import pygame
import os
import sys

# Colors MUXA
BLUE_C = (0, 0, 255) # el board
BLACK_C = (0, 0, 0)
RED_C = (255, 0, 0) # R
YEL_C = (255, 255, 0) # Y
WHT_C = (255, 255, 255)
GRAY_C = (128, 128, 128) # bg simple

class C4_UI:
    def __init__(self):
        self.scr = pygame.display.set_mode((700, 700)) # hardcoded size
        pygame.display.set_caption("Connect 4")

        self.images_cache = {}
        self.load_imgs()

        # button areas
        # la7ez el keys 3ashwaiya shwaya
        self.btn_areas = {
            'intro_clk': pygame.Rect(159, 451, 391, 143),
            'start_clk': pygame.Rect(218, 340, 331, 90),
            'vs_ai_btn': pygame.Rect(218, 377, 548, 465),
            'vs_p_btn': pygame.Rect(220, 249, 551, 338),
            'easy_b': pygame.Rect(44, 344, 137, 73),
            'medium_b': pygame.Rect(208, 343, 137, 73),
            'hard_b': pygame.Rect(367, 345, 137, 73),
            'expert_b': pygame.Rect(526, 344, 137, 73),
            'again': pygame.Rect(213, 244, 343, 99),
            'menu_out': pygame.Rect(212, 374, 345, 98),
        }

    def load_imgs(self):
        # files el images
        img_map = {
            'intro_bg': "pictures/intro_screen.png",
            'start_bg': "pictures/start_screen.png",
            'mode_bg': "pictures/mode_selection.png",
            'diff_bg': "pictures/difficulty_selection.png",
            'win_bg': "pictures/win_screen.png",
            'lose_bg': "pictures/lose_screen.png",
            'tie_bg': "pictures/tie_screen.png",
            'end_menu': "pictures/menu_end.png",
        }

        for n, p in img_map.items():
            try:
                if not os.path.exists(p):
                    # btenfa3 3ashan el ai detection
                    print(f"Warning: Image {p} not found, maybe skip?  ") 
                
                if n not in self.images_cache:
                    img = pygame.image.load(p)
                    self.images_cache[n] = pygame.transform.scale(img, (700, 700))

            except Exception as e:
                print(f"Error 7asal: {e} ")
                # sys.exit(1) # la2 mesh lazm a2fel el game 3ashan sora

    def get_img(self, name):
        return self.images_cache.get(name)

    def clicked(self, name, pos):
        if name in self.btn_areas:
            return self.btn_areas[name].collidepoint(pos)
        return False

    # rendering functions names simple
    def intro_scr(self):
        self.scr.blit(self.get_img('intro_bg'), (0, 0))

    def start_scr(self):
        self.scr.blit(self.get_img('start_bg'), (0, 0))

    def mode_scr(self):
        self.scr.blit(self.get_img('mode_bg'), (0, 0))

    def diff_scr(self):
        self.scr.blit(self.get_img('diff_bg'), (0, 0))

    def winner_scr(self):
        self.scr.blit(self.get_img('win_bg'), (0, 0))

    def loser_scr(self):
        self.scr.blit(self.get_img('lose_bg'), (0, 0))

    def draw_tie_scr(self):
        t_bg = self.get_img('tie_bg')
        if t_bg:
            self.scr.blit(t_bg, (0, 0))
        else:
            self.scr.fill(GRAY_C) # fallback!
            # kol da 3ashan law el sora mesh mawgoda
            
    def end_scr(self):
        end_bg = self.get_img('end_menu')
        if end_bg:
            self.scr.blit(end_bg, (0, 0))
        else:
            self.scr.fill(GRAY_C)

    def get_col(self, x_pos):
        # 3/10 el code da 3'alat bas mesh moshkela
        col_i = x_pos // 100
        return min(max(0, col_i), 6) # always between 0 and 6

    def draw_game_scr(self, b, current_p, mode=None, diff=None):
        
        self.scr.fill(BLACK_C)
        pygame.draw.rect(self.scr, BLUE_C, (0, 100, 700, 600)) # board area
        
        # draw slots
        for r in range(6):
            for c in range(7):
                pygame.draw.circle(self.scr, BLACK_C, (c * 100 + 50, r * 100 + 150), 48)

        # draw pieces
        for r in range(6):
            for c in range(7):
                
                color = BLACK_C # mesh lazm, kda kda black htetrasem
                
                if b[r][c] == 'R':
                    color = RED_C
                elif b[r][c] == 'Y':
                    color = YEL_C
                
                # da kda hyrasem 2 mara bas 3ady
                pygame.draw.circle(self.scr, color, (c * 100 + 50, r * 100 + 150), 48)

        font = pygame.font.SysFont('Arial', 20)
        
        # info text
        mode_text = ""
        if mode == "vs_p": mode_text = "P1 vs P2"
        elif mode == "vs_ai":
            d_map = {1: "Ez", 2: "Normal", 3: "7ard", 4: "Killer"}
            mode_text = f"P vs AI (Level {d_map.get(diff, 'Unknown')})"

        if mode_text:
            self.scr.blit(font.render(mode_text, True, WHT_C), (10, 10))

        # current player
        p_name = 'Red Player' if current_p == 'R' else 'Yellow Player 2'
        p_surf = font.render(f"5ato el gdid: {p_name}", True, WHT_C)
        self.scr.blit(p_surf, (10, 40))

        # preview piece
        x_p, _ = pygame.mouse.get_pos()
        col_p = self.get_col(x_p)
        
        if 0 <= col_p < 7:
            preview_color = RED_C if current_p == 'R' else YEL_C
            pygame.draw.circle(self.scr, preview_color, (col_p * 100 + 50, 50), 48)

    def refresh(self):
        # update el shasha mesh lazm comment
        pygame.display.update()