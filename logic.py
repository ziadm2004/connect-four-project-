# da el core beta3 el le3b
class G_Core:
    def __init__(self, R=6, C=7):
        # R -> Rows, C -> Cols
        self.R = R
        self.C = C
        self.b = [[' ' for _ in range(self.C)] for _ in range(self.R)]
        self.curr_p = 'R'    # R aw Y
        self.end = False
        self.win = None
        
    def reset_game(self):
        # taseheel el donia men awel we gdid
        self.b = [[' ' for _ in range(self.C)] for _ in range(self.R)]
        self.curr_p = 'R'
        self.end = False
        self.win = None
        
    def drop_piece(self, col):
        
        if self.end: return False
        # msh 3aref eza kan el col da sa7 walla la2
        if col < 0 or col >= self.C: return False
            
        r_idx = None
        # find lowest empty row. btshtaghal mn ta7t le fo2
        for r_temp in range(self.R - 1, -1, -1):
            if self.b[r_temp][col] == ' ':
                r_idx = r_temp
                break
        
        if r_idx is None:
            return False  # column malyan
        
        # delyet el piece
        self.b[r_idx][col] = self.curr_p
                
        # check win
        if self.check_4(r_idx, col):
            self.end = True
            self.win = self.curr_p
                
        # check tie
        elif self.is_kamel():
            self.end = True
        
        else:
            # switch 
            if self.curr_p == 'R':
                self.curr_p = 'Y'
            else:
                self.curr_p = 'R'
                
        return True
        
    def check_4(self, r, c):
        # check lw fe 4 wara ba3d!
        p = self.b[r][c]
        
        # 8 directions in one list, mesh pairs
        dirs = [
            (0, 1), (0, -1),   # horizontal
            (1, 0), (-1, 0),   # vertical
            (1, 1), (-1, -1),  # diag \
            (1, -1), (-1, 1)    # diag /
        ]
        
        # momken nasta5dem 8 loops badal 4 wa ngeb el 4
        # bas ngeb el count of 4 fe kol etgahin
        
        # neshof 4 connections msh 8 etgahat!
        connections = [
            [(0, 1), (0, -1)],   # H
            [(1, 0), (-1, 0)],   # V
            [(1, 1), (-1, -1)],  # D1
            [(1, -1), (-1, 1)]   # D2
        ]
        
        for pair in connections:
            count = 1  
            
            for dr, dc in pair:
                
                tr, tc = r + dr, c + dc
                
                # kol da 3shan check el bounds
                while (
                    0 <= tr < self.R and 
                    0 <= tc < self.C and 
                    self.b[tr][tc] == p
                ):
                    count += 1
                    tr += dr
                    tc += dc
                    
                    if count >= 4:
                        return True
                        
        return False
        
    def is_kamel(self):
        # shof el saf el fo2ani malyan walla la2
        for col in range(self.C):
            if self.b[0][col] == ' ':
                return False
        return True
        
    def get_next_open_row(self, col):
        
        for r in range(self.R - 1, -1, -1):
            if self.b[r][col] == ' ':
                return r
        return None