class VariableMap(object):
    """ Mapovanie mien premennych na cisla.

    Premennym vzdy priraduje suvisly usek cisel 1..n.
    """
    def __init__(self, variables = []):
        """ Vytvori nove mapovanie, ktore bude obsahovat premenne z variables. """
        pass

    def addVar(self, var):
        """ Prida premennu var.

        Ak je uz v mape, nic sa nestane, ak nie prida ju s dalsim cislom v poradi.
        Vrati referenciu na seba, aby sa dala zretazovat.
        """
        # prida premennu
        return self

    def get(self, var):
        """ Vrati cislo priradene premennej var.

        Vyhodi KeyError vynimku ak taka premenna nie je v mape.
        """
        return 1

    def __getitem__(self, var):
        """ Vrati cislo priradene premennej var.

        Vyhodi KeyError vynimku ak taka premenna nie je v mape.
        """
        return 1

    def keys(self):
        """ Vrati zoznam vsetkych premennych v mape. """
        return []

    def toString(self):
        """ Vrati textovu reprezentaciu mapovania premennych.

        Napriklad vo formate "{'a':1, 'b':2, ...}" alebo podobnom.
        """
        return ''

    def reverse(self):
        """ Vrati reverzne mapovanie ako jednoduchy slovnik z cisel na mena premennych. """
        return {1: 'a'}

    def writeToFile(self, outFile):
        """ Zapise mapu do suboru outFile. """
        pass

    @staticmethod
    def readFromFile(inFile):
        """ Nacita novu mapu zo suboru inFile a vrati ju. """
        varMap = VariableMap([])
        # nacitame z inFile
        #...
        return varMap



class CnfLit(object):
    """ Reprezentacia literalu (premenna alebo negovana premenna) v CNF formule. """
    def __init__(self, name):
        """ Vytvori novy, kladny (nenegovany) literal pre premennu name. """
        self.name = name
        self.neg = False

    @staticmethod
    def Not(name):
        """ Vytvory novy, negovany literal pre premennu name. """
        return CnfLit('x')

    def __neg__(self):
        """ Vrati novy literal, ktory je negaciou tohoto. """
        return CnfLit('x')

    def toString(self):
        """ Vrati textovu reprezentaciu tohoto literalu (vid zadanie). """
        return ''

    def eval(self, i):
        """ Vrati ohodnotenie tohoto literalu pri interpretacii i. """
        return False

    def extendVarMap(self, varMap):
        """ Rozsiri varMap o premennu v tomto literali. """
        pass

    def writeToFile(self, outFile, varMap):
        """ Zapise literal do suboru outFile s pouzitim mapovania premennych varMap. """
        pass

class CnfClause(list):
    """ Reprezentacia klauzy (pole literalov). """
    def __init__(self, vars = []):
        """ Vytvori novu klauzu obsahujucu literaly literals. """
        list.__init__(self, vars)

    def toString(self):
        """ Vrati textovu reprezentaciu tejto klauzy (vid zadanie). """
        return ''

    def eval(self, i):
        """ Vrati ohodnotenie tejto klauzy pri interpretacii i. """
        return False

    def extendVarMap(self, varMap):
        """ Rozsiri varMap o premenne v tejto klauze. """
        pass

    def writeToFile(self, oFile, varMap):
        """ Zapise klauzu do suboru outFile v DIMACS formate
            pricom pouzije varMap na zakodovanie premennych na cisla.

        Klauzu zapise na jeden riadok (ukonceny znakom konca riadku).
        """
        pass

    @staticmethod
    def readFromFile(inFile, varMap):
        """ Nacita novu klauzu zo suboru inFile a vrati ju ako vysledok.

        Mozete predpokladat, ze klauza je samostatne na jednom riadku.

        Ak sa z aktualneho riadku na vstupe neda nacitat korektna klauza,
        vyhodi vynimku IOError.
        """
        return CnfClause([])

class Cnf(list):
    """ Reprezentacia Cnf formuly ako pola klauz. """
    def __init__(self, clauses = []):
        """ Vytvori novu Cnf formuly obsahujucu klauzy clauses. """
        list.__init__(self, clauses)

    def toString(self):
        """ Vrati textovu reprezentaciu tejto formule (vid zadanie). """
        return ''

    def eval(self, i):
        """ Vrati ohodnotenie tejto formule pri interpretacii i. """
        return False

    def extendVarMap(self, varMap):
        """ Rozsiri varMap o premenne v tejto formule. """
        pass

    def writeToFile(self, oFile, varMap):
        """ Zapise klauzu do suboru outFile v DIMACS formate
            pricom pouzije varMap na zakodovanie premennych na cisla a
            zapise kazdu klauzu na jeden riadok.
        """
        pass

    @staticmethod
    def readFromFile(inFile, varMap):
        """ Nacita novu formulu zo suboru inFile a vrati ju ako vysledok.

        Mozete predpokladat, ze kazda klauza je samostatne na jednom riadku.
        """
        return Cnf([])

# vim: set sw=4 ts=4 sts=4 et :
