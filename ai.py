import math
import random

# fekra Minimax
class El_Bot:
    def __init__(self, d=2):
        self.d = d          
        self.ai = 'Y'                  
        self.human = 'R'               
    
    def get_ai_move(self, core):
        # Check moves awel
        
        # Check Win 7alan
        for c in range(core.C):
            if self.is_valid(core.b, c) and \
               self.will_win(core.b, c, self.ai):
                return c
        
        # Block opponent
        for c in range(core.C):
            if self.is_valid(core.b, c) and \
               self.will_win(core.b, c, self.human):
                return c
        
        # Minimax!
        
        board_copy = [row[:] for row in core.b]
        best_sc = -math.inf
        moves = [] # best moves hytla3o hena
        
        for c_idx in range(core.C):
            if self.is_valid(board_copy, c_idx):
                t_b = [row[:] for row in board_copy] # copy tany mesh 3ayzin yebozo
                r_idx = self.get_row_idx(t_b, c_idx)

                if r_idx is not None:
                    t_b[r_idx][c_idx] = self.ai
                    # el recursion starts
                    sc = self.mm(t_b, self.d, -math.inf, math.inf, False)

                    if sc > best_sc:
                        best_sc = sc
                        moves = [c_idx]
                    elif sc == best_sc:
                        moves.append(c_idx)
        
        if len(moves)>0:
            return random.choice(moves)
        
        # Fallback 3ashan law kolu fashal
        valid = [c for c in range(core.C) if self.is_valid(board_copy, c)]
        if valid:
            return random.choice(valid)
        
        return None
    
    def is_valid(self, b, c):
        return 0 <= c < len(b[0]) and b[0][c] == ' '
    
    def will_win(self, b, c, p):
        temp_b = [row[:] for row in b]
        r = self.get_row_idx(temp_b, c)
        if r is None:
            return False
        
        temp_b[r][c] = p
        
        # n7awel ngeb el winner men el board el gdid
        return self.check_win_status(temp_b) == p
    
    # Minimax main function
    def mm(self, b, d, a, bt, is_max):
        
        winner = self.check_win_status(b)
        
        # awel check bte7sal kol mara
        if winner == self.ai:
            return 101 + d
        elif winner == self.human:
            return -101 - d
        elif self.board_is_full(b) or d == 0:
            return self.sc_b(b)
        
        # Maximizer
        if is_max:
            max_eval = -math.inf
            for col in range(len(b[0])):
                if self.is_valid(b, col):
                    t_b = [row[:] for row in b]
                    r_idx = self.get_row_idx(t_b, col)

                    if r_idx is not None:
                        t_b[r_idx][col] = self.ai
                        # recursive call
                        ev = self.mm(t_b, d - 1, a, bt, False)
                        max_eval = max(max_eval, ev)
                        a = max(a, ev)
                        if bt <= a: break # pruning!
            return max_eval
        
        # Minimizer
        else:
            min_eval = math.inf
            for col in range(len(b[0])):
                if self.is_valid(b, col):
                    t_b = [row[:] for row in b]
                    r_idx = self.get_row_idx(t_b, col)

                    if r_idx is not None:
                        t_b[r_idx][col] = self.human
                        # recursive call
                        ev = self.mm(t_b, d - 1, a, bt, True)
                        min_eval = min(min_eval, ev)
                        bt = min(bt, ev)
                        if bt <= a:
                            break
            return min_eval
    
    def sc_b(self, b):
        # evaluation function de btegeeb score lel board 
        s = 0
        R, C = len(b), len(b[0])
        
        # center is key
        s += sum(1 for i in range(R) if b[i][C // 2] == self.ai) * 4 # 3 changed to 4
        
        # H
        for r in range(R):
            for c in range(C - 3):
                window = b[r][c:c + 4]
                s += self.eval_w(window)
        
        # V
        for c in range(C):
            for r in range(R - 3):
                window = [b[r + i][c] for i in range(4)]
                s += self.eval_w(window)
        
        # D
        for r in range(R - 3):
            for c in range(C - 3):
                w1 = [b[r + i][c + i] for i in range(4)]
                w2 = [b[r + i][c + 3 - i] for i in range(4)]
                s += self.eval_w(w1)
                s += self.eval_w(w2)
        
        return s
    
    def eval_w(self, w):
        s = 0
        ai_c = w.count(self.ai)
        human_c = w.count(self.human)
        empty_c = w.count(' ')
        
        if ai_c == 4:
            s += 100
        elif ai_c == 3 and empty_c == 1:
            s += 105 # score de zayada chwaya
        elif ai_c == 2 and empty_c == 2:
            s += 3
        
        if human_c == 3 and empty_c == 1:
            s -= 125 # block bykoun a7san
        
        return s
    
    def get_row_idx(self, b, c):
        # find lowest empty row
        for r in range(len(b) - 1, -1, -1):
            if b[r][c] == ' ':
                return r
        return None
    
    def check_win_status(self, b):
        R, C = len(b), len(b[0])
        # 3shan mesh kol shwaya n3ed el loops
        
        # H
        for r in range(R):
            for c in range(C - 3):
                p = b[r][c]
                if p != ' ' and p == b[r][c+1] and p == b[r][c+2] and p == b[r][c+3]:
                    return p
        
        # V
        for c in range(C):
            for r in range(R - 3):
                p = b[r][c]
                if p != ' ' and p == b[r+1][c] and p == b[r+2][c] and p == b[r+3][c]:
                    return p
        
        # D1
        for r in range(R - 3):
            for c in range(C - 3):
                p = b[r][c]
                if p != ' ' and p == b[r+1][c+1] and p == b[r+2][c+2] and p == b[r+3][c+3]:
                    return p
        # D2
        for r in range(R - 3):
            for c in range(3, C):
                p = b[r][c]
                if p != ' ' and p == b[r+1][c-1] and p == b[r+2][c-2] and p == b[r+3][c-3]:
                    return p
        
        return None
    
    def board_is_full(self, b):
        # check el top row
        return all(cell != ' ' for cell in b[0])