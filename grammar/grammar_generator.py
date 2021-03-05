import csv
import random
from collections import defaultdict

class CFG(object):
    """ 
    see https://eli.thegreenplace.net/2010/01/28/generating-random-sentences-from-a-context-free-grammar 
    """
    def __init__(self):
        self.prod = defaultdict(list)

    def add_production_rule(self, lhs, rhs):
        """ Add production rule to the grammar. 'rhs' can
            be several productions separated by '|'.
            Each production is a sequence of symbols
            separated by whitespace.

            Usage:
                grammar.add_prod('NT', 'VP PP')
                grammar.add_prod('Digit', '1|2|3|4')
        """
        prods = rhs.split('|')
        for prod in prods:
            self.prod[lhs].append(tuple(prod.split()))

    def add_production_rule_list(self, lhs, rhs):
        """ Add production rule to the grammar. 'rhs' is a
            list of terminal strings.

            Usage:
                grammar.add_prod('N', ["dog","cat"])
                grammar.add_prod('V', ["jump", "fly"])
        """
        for prod in rhs:
            self.prod[lhs].append(prod)

    def gen_random(self, symbol):
        """ Generate a random sentence from the
            grammar, starting with the given
            symbol.
        """
        sentence = ''

        # select one production of this symbol randomly
        rand_prod = random.choice(self.prod[symbol])

        if (isinstance(rand_prod,tuple)):
            for sym in rand_prod:
                # for non-terminals, recurse
                if sym in self.prod:
                    sentence += self.gen_random(sym)
                else:
                    sentence += sym + ' '
        else:
            sentence += rand_prod + ' '

        return sentence

cfg1 = CFG()
cfg1.add_production_rule('S', 'NP VP')
cfg1.add_production_rule('NP', 'N | Adj N')
cfg1.add_production_rule('VP', 'V NP | VP')
cfg1.add_production_rule('Adj', 'Big | Evil | Weird | Smelly | Tiny | Rogue | Unlucky | Local')
cfg1.add_production_rule('N', 'Crocodile | Pot Plant | Kitten | Trousers')
cfg1.add_production_rule('V', 'Disintegrates | Terrorizes | Tickles')

for i in range(5):
    print(cfg1.gen_random('S'))
