#! /bin/env python

import sys
from sudoku import SudokuSolver


class Tester(object):
    def __init__(self):
        self.tested = 0
        self.passed = 0

    def checkList(self, l, msg):
        if len(l) != 9:
            print('ERROR: Wrong result format %s!' % (msg,))
            return False
        s = sorted(list(set(l)))
        if len(s) !=9:
            print('ERROR: Duplicate number %s!' % (msg,))
            return False
        if s != range(1,10):
            print('ERROR: Wrong numbers %s!' % (msg,))
            return False
        return True

    def checkInput(self, i, s):
        for r in xrange(9):
            for c in xrange(9):
                if i[r][c] != 0:
                    if i[r][c] != s[r][c]:
                        print('ERROR: does not match input at %d,%d!' % (r,c))
                        return False
        return True

    def checkGood(self, i, s):
        if not self.checkInput(i, s):
            return False
        for row,r in zip(s,xrange(9)):
            if not self.checkList(row, 'in row %d: %s' % (r,repr(row))):
                return False
        for c in xrange(9):
            col = [ row[c] for row in s ]
            if not self.checkList(col, 'in col %d: %s' % (c,repr(col))):
                return False
        for sr in xrange(3):
            for sc in xrange(3):
                a = sc*3
                b = sc*3 + 3
                l = s[sr*3][a:b] + s[sr*3+1][a:b] + s[sr*3+2][a:b]
                if not self.checkList(l, 'in square %d,%d: %s' % (sr,sc,repr(l))):
                    return False
        return True

    def checkBad(self, s):
        for r in s:
            for c in r:
                if c:
                    print('ERROR: Nonzero in bad sudoku!')
                    return False
        return True

    def check(self, i, good, s):
        if good:
            return self.checkGood(i, s)
        else:
            return self.checkBad(s)


    def test(self, i, good, s):
        self.tested += 1
        sys.stdout.write('Case %d:  ' % (self.tested,))
        if self.check(i, good, s):
            self.passed += 1
            print('PASSED')
        else:
            print('')
            print('{:^20}    {:^20}'.format('INPUT', 'OUTPUT'))
            for ri,rs in zip(i,s):
                print('{:<20}    {:<20}'.format(
                    ' '.join([str(x) for x in ri]),
                    ' '.join([str(x) for x in rs]),
                ))
            print('')

    def status(self):
        print("TESTED %d" % (self.tested,))
        print("PASSED %d" % (self.passed,))
        if self.tested == self.passed:
            print("OK")
        else:
            print("ERROR")


t = Tester()

i = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
t.test(i, True, SudokuSolver().solve(i))

i = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
t.test(i, True, SudokuSolver().solve(i))

i = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
t.test(i, False, SudokuSolver().solve(i))

i = [
    [0, 9, 5, 0, 0, 3, 6, 0, 0],
    [0, 6, 0, 0, 5, 1, 0, 3, 8],
    [1, 8, 0, 0, 4, 6, 7, 0, 9],
    [5, 0, 4, 0, 2, 0, 0, 0, 6],
    [6, 1, 0, 4, 8, 0, 0, 2, 0],
    [8, 3, 0, 0, 0, 0, 0, 7, 0],
    [9, 5, 0, 7, 3, 4, 0, 6, 0],
    [0, 0, 6, 0, 0, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 2, 5, 9, 3],
]
t.test(i, True, SudokuSolver().solve(i))

t.status()

# vim: set sw=4 ts=4 sts=4 et :
