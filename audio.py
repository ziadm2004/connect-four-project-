import pygame
import os
import sys # 3ashan low 7asal 7aga

# de el class bta3t el sot
class Sfx_Handler:
    def __init__(self):
        pygame.mixer.init()
        self.snds = {}
        self.load_all()
    
    def load_all(self):
        # sound files
        files_list = {
            'drop': 'sounds/drop.wav',
            'ai_move': 'sounds/ai_move.wav',
            'win': 'sounds/win.wav',
            'lose': 'sounds/lose.wav',
            'error_snd': 'sounds/error.wav', # changed name
            'button': 'sounds/button.wav'
        }
        
        for name, path in files_list.items():
            try:
                if not os.path.exists(path):
                    # msh lazm a2fel el program 3ashan sound
                    print(f"Sound {path} is missing. No sound for {name}")
                    continue # roo7 lel ba3do
                
                self.snds[name] = pygame.mixer.Sound(path)
            
            except Exception as e:
                # 7asalt moshkela we ana ba load el sound
                print(f"Ehhhh el 7asal: {e} with {path}")
                # kda kda el program mesh haywa2af
                pass
    
    def play(self, n):
        # function 3adi
        if n in self.snds:
            self.snds[n].play()
    
    # helper functions for playing
    def Play_Drop(self):
        self.play('drop')
    
    def Play_Ai(self):
        self.play('ai_move')
    
    def Win_Snd(self):
        self.play('win')
    
    def Lose_Snd(self):
        self.play('lose')
    
    def Error_Snd(self):
        self.play('error_snd')
    
    def Click_Snd(self):
        # el button click
        self.play('button')