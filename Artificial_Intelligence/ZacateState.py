# Dice and game state code for Zacate v0.2 (updated Oct 10 to fix bug with pupusa de queso scoring)
# B551  Fall 2015
# D. Crandall
# 
# DON'T MODIFY THIS CODE WITHOUT CHECKING WITH US FIRST!
# Otherwise we may not be able to grade your submission correctly.
#
import random

class Dice:

    def __init__(self):
        self.dice = []

    def roll(self):
        self.reroll(range(0,5))
        return self.dice

    def reroll(self, dice_list):
        self.dice = [ (random.randrange(1, 7) if i in dice_list else self.dice[i]) for i in range(0,5) ]
        return self.dice

    def __str__(self):
        return " ".join([str(i) for i in self.dice])



class Scorecard:
    Numbers = { "unos" : 1, "doses" : 2, "treses" : 3, "cuatros" : 4, "cincos" : 5, "seises" : 6 }
    Categories = [ "unos", "doses", "treses", "cuatros", "cincos", "seises", "pupusa de queso", "pupusa de frijol", "elote", "triple", "cuadruple", "quintupulo", "tamal" ]

    def __init__(self):
        self.scorecard = {}
        self.totalscore = 0
        self.bonusscore = 0
        self.bonusflag = False

    def record(self, category, roll):
        dice = roll.dice
        counts = [dice.count(i) for i in range(1,7)]

        if category in self.scorecard:
            print "Error: category already full!"

        if category in Scorecard.Numbers:
            score = counts[Scorecard.Numbers[category]-1] * Scorecard.Numbers[category]
        elif category == "pupusa de queso":
            score = 40 if sorted(dice) == [1,2,3,4,5] or sorted(dice) == [2,3,4,5,6] else 0
        elif category == "pupusa de frijol":
            score = 30 if (len(set([1,2,3,4]) - set(dice)) == 0 or len(set([2,3,4,5]) - set(dice)) == 0 or len(set([3,4,5,6]) - set(dice)) == 0) else 0
        elif category == "elote":
            score = 25 if (2 in counts) and (3 in counts) else 0
        elif category == "triple":
            score = sum(dice) if max(counts) >= 3 else 0
        elif category == "cuadruple":
            score = sum(dice) if max(counts) >= 4 else 0
        elif category == "quintupulo":
            score = 50 if max(counts) == 5 else 0
        elif category == "tamal":
            score = sum(dice)
        else:
            print "Error: unknown category"
    
        self.scorecard[category] = score
        self.totalscore += score

        # check for bonus
        if not self.bonusflag and len(set(Scorecard.Numbers.keys()) - set(self.scorecard.keys())) == 0:
            self.bonusscore = 35 if sum([ self.scorecard[i] for i in Scorecard.Numbers ]) >= 63 else 0
            self.bonusflag = True
            self.totalscore += self.bonusscore

    def __str__(self):
        s = ""
        for k in Scorecard.Categories:
            s += "      %4d  %-30s \n" % ( (self.scorecard[k] if k in self.scorecard else 0), k)
        s += "      %4s  %-30s \n" % ("" if not self.bonusflag else self.bonusscore, "Bonus")
        s += "      %4d  %-30s \n" % (self.totalscore, "TOTAL")
        return s
