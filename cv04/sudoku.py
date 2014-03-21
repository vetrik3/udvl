import os.path
import sys
sys.path[0:0] = [os.path.join(sys.path[0], '../examples/sat')]

import sat

class SudokuSolver(object):
    def __init__(self):
        self.N = 0

    def s(self, x, y, j):
        return x*9*9 + y*9 + (j-1) + 1

    def solve(self, i):
        solver = sat.SatSolver()
        w = sat.DimacsWriter('sudoku_cnf_in.txt')
		
		# na polickach aspon jedno cislo
        for x in range(9):
            for j in range(9):
                for n in range(1,10):
                    w.writeLiteral(self.s(x,j,n))
                w.finishClause()
                
        for x in range(9):
            for j in range(9):
                for y1 in range(1,10):
                    for y2 in range(1,10):
                        if y1 != y2:
                            w.writeImpl(self.s(x,j,y1),-self.s(x,j,y2))

        # zakodujeme si vstup
        for x in range(9):
            for j in range(9):
                if i[x][j] != 0:
                    w.writeClause([self.s(x,j, i[x][j])])

        # osetrime aby sa nachadzal v kazdom riadnu prave jeden
        for x in range(9):
            for y1 in range(9):
                for y2 in range(9):
                    if y1 != y2:
                        for j in range(1,10):
                            w.writeImpl(self.s(x,y1,j),-self.s(x,y2,j))

        # osetrime aby sa nachadzal v kazdom stlpci prave jeden
        for x1 in range(9):
            for x2 in range(9):
                for y in range(9):
                    if x1 != x2:
                        for j in range(1,10):
                            w.writeImpl(self.s(x1,y,j),-self.s(x2,y,j))

        # osetrime aby sa nachadzal v kazdom stlpci prave jedno cislo
        for x1 in range(9):
            for x2 in range(9):
                for y1 in range(9):
                    for y2 in range(9):
                        if x1 != x2:
                            if y1 != y2:
                                if x1 // 3 == x2 // 3 and y1 // 3 == y2 // 3:
                                    for j in range(1,10): 
                                        w.writeImpl(self.s(x1,y1,j),-self.s(x2,y2,j))
        
        w.close()
		
        OK, solve = solver.solve(w, 'sudoku_cnf_out.txt')

        ret = []
        for j in range(9):
            ret.append([0]*9) # [0]*9 pole deviatich nul
            
        if OK:
            for x in solve:
                if x > 0:
                    x = x - 1
                    y = (x % 9) + 1
                    x = x //9
                    y1 = x % 9
                    x = x //9
                    y2 = x
                    ret[y2][y1] = y
        return ret
