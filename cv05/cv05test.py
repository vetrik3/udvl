#!/bin/env python3

import io
import itertools
import traceback

"""
    Testovaci program pre kniznicu cnf.py
"""

from cnf import VariableMap, Cnf, CnfClause, CnfLit

def ignoreException(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print('ERROR: %s: Exception raised:\n%s\n%s\n%s' % (
                func.__name__,
                '-'*20,
                traceback.format_exc(),
                '-'*20)
            )
    return wrapper

class Tester(object):
    def __init__(self):
        self.tested = 0
        self.passed = 0

    def compare(self, result, expected, msg):
        self.tested += 1
        if result == expected:
            self.passed += 1
            return True
        else:
            print("Failed: %s:" %  msg)
            print("    got %s  expected %s" % (repr(result), repr(expected)))
            print("")
            return False

    def status(self):
        print("TESTED %d" % (self.tested,))
        print("PASSED %d" % (self.passed,))
        if self.tested == self.passed:
            print("OK")
        else:
            print("ERROR")

    def check(self, b):
        self.state = self.state and b

    @ignoreException
    def testCnfWrite(self, cnf, varMap, dimacs):
        oF = io.StringIO()
        cnf.writeToFile(oF, varMap)
        oD = [int(x) for x in oF.getvalue().split()]
        self.compare(oD, dimacs, 'Cnf.writeToFile %s' % cnf.toString())

    @ignoreException
    def testCnfRead(self, dimacs, varMap, ecnf):
        iF = io.StringIO(dimacs)
        cnf = Cnf.readFromFile(iF, varMap)
        self.compare(cnf.toString(), ecnf.toString(), 'Cnf.readFromFile %s' % ecnf.toString())

    @ignoreException
    def testCnfClauseWrite(self, cnf, varMap, dimacs):
        oF = io.StringIO()
        cnf.writeToFile(oF, varMap)
        oD = [int(x) for x in oF.getvalue().split()]
        self.compare(oD, dimacs, 'CnfClause.writeToFile %s' % cnf.toString())

    @ignoreException
    def testCnfLitWrite(self, cnf, varMap, dimacs):
        oF = io.StringIO()
        cnf.writeToFile(oF, varMap)
        oD = [int(x) for x in oF.getvalue().split()]
        self.compare(oD, dimacs, 'CnfLit.writeToFile %s' % cnf.toString())

    @ignoreException
    def testCnfClauseRead(self, dimacs, varMap, ecnf):
        iF = io.StringIO(dimacs)
        cnf = CnfClause.readFromFile(iF, varMap)
        self.compare(cnf.toString(), ecnf.toString(), 'CnfClause.readFromFile %s' % ecnf.toString())

    @ignoreException
    def testVarMap(self, namesPre, namesAdd):
        varMap = VariableMap(namesPre)
        for name in namesAdd:
            varMap.addVar(name)
        self.compare(sorted(varMap.keys()), sorted(list(set(namesPre+namesAdd))),
                'VariableMap: wrong variables %s' % varMap.toString())

        self.compare(
                sorted([varMap[k] for k in varMap.keys()]),
                list(range(1, len(sorted(list(set(namesPre+namesAdd)))) + 1)),
                'VariableMap: wrong variable numbers %s' % varMap.toString())

        rev = varMap.reverse()
        self.compare(
                sorted([ (k,varMap[k]) for k in varMap.keys()]),
                sorted([ (rev[k],k) for k in rev]),
                'VariableMap: reverse() %s' % varMap.toString())

        oF = io.StringIO()
        varMap.writeToFile(oF)
        iF = io.StringIO(oF.getvalue())
        vm = VariableMap.readFromFile(iF)
        self.compare(
                sorted([ (k,vm[k]) for k in vm.keys()]),
                sorted([ (k,varMap[k]) for k in varMap.keys()]),
                'VariableMap read/write %s (%s)' % (varMap.toString(), repr(oF.getvalue())))

    @ignoreException
    def testExtendVarMap(self, cnf, names):
        for pre in range(len(names)):
            varMap = VariableMap()
            for name in names[:pre]:
                varMap.addVar(name)  # fixed numbers (1,2..pre) for the first 'pre' variables
            cnf.extendVarMap(varMap)
            keys = sorted(varMap.keys())
            values = sorted([ varMap[v] for v in varMap.keys() ])
            self.compare(keys, sorted(names), 'extendVarMap wrong var names %s %s' % (names, cnf.toString()))
            self.compare(values, list(range(1, len(names)+1)), 'extendVarMap wrong numbers %s %s' % (names, cnf.toString()))
            for k,v in [ (v,varMap[v]) for v in names[:pre]]:
                self.compare(varMap[k], v, 'extendVarMap fixed mismatch %s %s' % (names, cnf.toString()))

    @ignoreException
    def testCnf(self, cnf, string, cases):
        self.compare(cnf.toString(), string, 'toString')

        for interpretation, result in cases:
            self.compare(cnf.eval(interpretation), result, 'eval(%s)\n%s' % (repr(interpretation), string))


t = Tester()

try:
    #
    # Jednoduche testy literalov
    #
    t.compare( CnfLit('a').name, 'a', 'CnfLit.name' )
    t.compare( CnfLit('a').neg, False, 'CnfLit.neg' )
    t.compare( CnfLit.Not('a').name, 'a', 'CnfLit.Not.name' )
    t.compare( CnfLit.Not('a').neg, True, 'CnfLit.Not.neg' )
    t.compare( (-CnfLit('a')).name, 'a', '-CnfLit.Not.name' )
    t.compare( (-CnfLit('a')).neg, True, '-CnfLit.Not.neg' )
    t.compare( (--CnfLit('a')).name, 'a', '--CnfLit.Not.name' )
    t.compare( (--CnfLit('a')).neg, False, '--CnfLit.Not.neg' )


    #
    # testy toString, eval pre CnfLit, CnfClause, Cnf
    #
    t.testCnf(
            CnfLit('a'), 'a',
            [
                ({'a':True}, True),
                ({'a':False}, False),
            ])

    t.testCnf(
            CnfLit.Not('a'), '-a',
            [
                ({'a':True}, False),
                ({'a':False}, True),
            ])

    t.testCnf(
            CnfClause( [ CnfLit('a'), CnfLit('a') ] ), 'a a',
            [
                ({'a':True}, True),
                ({'a':False}, False),
            ])

    t.testCnf(
            CnfClause( [ CnfLit('a'), CnfLit.Not('a') ] ), 'a -a',
            [
                ({'a':True}, True),
                ({'a':False}, True),
            ])

    t.testCnf(
            Cnf( [
                CnfClause( [ CnfLit('a'), CnfLit.Not('b') ] ),
                CnfClause( [ CnfLit('b') ] ),
                ]), 'a -b\nb\n',
            [
                ({'a':True, 'b':True}, True),
                ({'a':True, 'b':False}, False),
                ({'a':False, 'b':True}, False),
                ({'a':False, 'b':False}, False),
            ])


    #
    # testy pre VariableMap
    #
    varMap = VariableMap()
    varMap.addVar('z').addVar('y').addVar('x')
    t.compare( varMap.get('y'), 2, 'varMap.get(y)')
    t.compare( varMap['y'], 2, 'varMap[y]')

    for p in itertools.permutations(['a', 'b', 'x']):
        for l in range(3):
            t.testVarMap(p[:l], p[l:])

    #
    # testy extendVarMap
    #
    t.testExtendVarMap(
            Cnf( [
                CnfClause( [ CnfLit('a'), CnfLit.Not('b') ] ),
                CnfClause( [ ] ),
                CnfClause( [ CnfLit('x') ] ),
                CnfClause( [ CnfLit('c'), CnfLit.Not('c'), -CnfLit('c') ] ),
                ]),
            ['a', 'b', 'c', 'x'],
            )

    #
    # testy readFrom / writeToFile
    #
    t.testCnfLitWrite(
            CnfLit('a'),
            VariableMap().addVar('a'),
            [ 1 ])

    t.testCnfClauseWrite(
            CnfClause( [ CnfLit('a'), CnfLit('b'), CnfLit.Not('c') ] ),
            VariableMap().addVar('c').addVar('a').addVar('b'),
            [ 2, 3, -1, 0 ])

    t.testCnfClauseRead(
            '1 -2 3 0\n',
            VariableMap().addVar('c').addVar('b').addVar('a'),
            CnfClause( [ CnfLit('c'), CnfLit.Not('b'), CnfLit('a') ] )
            )

    t.testCnfWrite(
            Cnf( [
                CnfClause( [ CnfLit('a'), CnfLit('b'), CnfLit.Not('a') ] ),
                CnfClause( [] ),
                CnfClause( [ CnfLit('z') ] ),
                ]),
            VariableMap().addVar('z').addVar('a').addVar('b'),
            [ 2, 3, -2, 0, 0, 1, 0 ])

    t.testCnfRead(
            '1 2 3 0\n-1 -2 -3 0\n0\n3 1 0\n',
            VariableMap().addVar('c').addVar('b').addVar('a'),
            Cnf( [
                CnfClause( [ CnfLit('c'), CnfLit('b'), CnfLit('a') ] ),
                CnfClause( [ CnfLit.Not('c'), CnfLit.Not('b'), CnfLit.Not('a') ] ),
                CnfClause( [ ] ),
                CnfClause( [ CnfLit('a'), CnfLit('c') ] ),
                ]))

    print("END")

finally:
    t.status()

# vim: set sw=4 ts=4 sts=4 et :
