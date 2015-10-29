# Automatic Zacate game player
# B551 Fall 2015
# PUT YOUR NAME AND USER ID HERE!
#
# Based on skeleton code by D. Crandall
#
# PUT YOUR REPORT HERE!
#
#
# This is the file you should modify to create your new smart Zacate player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#


""" 
(a) 	I have considered the the value for the first roll and the second roll depending upon the calculation of 
    	all the permetuations and combinations of the currect dice state. With highest cost will be value that will be  
    	considered then, the next move is suggested. 
(b) 	I faced the problem of calcualting the probability for the next moves. I am assuming the best cost combination
	for the current roll and not the probability for the next roll that can be true. Hence highest average i got after 
	many runs, was 140.
(c)	My program can be improved with by calculating the probability on the given dice for next roll, and then considering
	the roll from previous turn. As the number of turns increases, we can get a better probability by calculating the
	Baye's equation. 

"""


from ZacateState import Dice
from ZacateState import Scorecard
import random
from itertools import permutations
from itertools import product

class ZacateAutoPlayer:

      	def __init__(self):
            pass  

      	def first_roll(self, dice, scorecard):
		array = []
		first =[]
		array=self.calc_prob(dice.dice,scorecard)
		for i in range(0,5):
			if array[i]!=dice.dice[i]:
				first.append(dice.dice.index(dice.dice[i]))	
		
            	return first 

      	def second_roll(self, dice, scorecard):
		array = []
		first =[]
		array=self.calc_prob(dice.dice,scorecard)
		for i in range(0,5):
			if array[i]!=dice.dice[i]:
				first.append(dice.dice.index(dice.dice[i]))	
		
            	return first 	
      
      	def third_roll(self, dice, scorecard):
            # stupidly just randomly choose a category to put this in
		if self.check(dice.dice,scorecard,1)== 0:
			return self.calc_unknown(dice.dice,scorecard)
            		#return random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) )
		else:  
			
			return self.check(dice.dice,scorecard,1)
	def check(self,dice,Scorecard,flag):
		temp_score_pup = 0
		temp_score_pup_fri = 0
		temp_score_elote = 0
		temp_score_triple = 0
		temp_score_cuadruple = 0
		temp_score_quintupulo = 0
		temp_score_tamal = 0
		temp_score_unknown = 0
		max_score = 0
		
		counts = [dice.count(i) for i in range(1,7)]
		temp_score_unos=sum(1 for i in sorted(dice) if i == 1 and "unos" not in Scorecard.scorecard)
		temp_score_doses=sum(1 for i in sorted(dice) if i == 2 and "doses" not in Scorecard.scorecard)*2
		temp_score_treses=sum(1 for i in sorted(dice) if i == 3 and "treses" not in Scorecard.scorecard)*3
		temp_score_cuatros=sum(1 for i in sorted(dice) if i == 4 and "cuatros" not in Scorecard.scorecard)*4
		temp_score_cincos=sum(1 for i in sorted(dice) if i == 5 and "cincos" not in Scorecard.scorecard)*5
		temp_score_seises=sum(1 for i in sorted(dice) if i == 6 and "seises" not in Scorecard.scorecard)*6
		if sorted(dice) == [1,2,3,4,5] or sorted(dice) == [2,3,4,5,6]and "pupusa de quesso"  not in Scorecard.scorecard:
			temp_score_pup = 40	
		if (len(set([1,2,3,4]) - set(dice)) == 0 or len(set([2,3,4,5]) - set(dice)) == 0 or len(set([3,4,5,6]) - set(dice)) == 0)and "pupusa de frijol"  not in Scorecard.scorecard:

			temp_score_pup_fr = 30
		if (2 in counts) and (3 in counts)and "elote"  not in Scorecard.scorecard:
			temp_score_elote = 25
		if max(counts) >= 3 and "triple"  not in Scorecard.scorecard:
			temp_score_triple = sum(dice)
		if max(counts) >= 4 and "cuadruple"  not in Scorecard.scorecard:
			temp_score_cuadruple = sum(dice)
		if max(counts) == 5 and "quintupulo"  not in Scorecard.scorecard:
			temp_score_quintupulo = 50
		if "tamal"  not in Scorecard.scorecard:
			temp_score_tamal = sum(dice)
		
		max_score=max([temp_score_unos,temp_score_doses,temp_score_treses,temp_score_cuatros,temp_score_cincos,temp_score_seises,temp_score_pup, temp_score_elote, temp_score_triple, temp_score_cuadruple, temp_score_quintupulo,temp_score_tamal,temp_score_tamal])
		if max_score == temp_score_unos and "unos" not in Scorecard.scorecard: 
			if flag == 1 :return "unos" 
			else: return max_score
		if max_score == temp_score_doses and "doses" not in Scorecard.scorecard:

			if flag == 1: return "doses" 
			else: return max_score
		if max_score == temp_score_treses and "treses" not in Scorecard.scorecard:
			if flag == 1: return "treses" 
			else: return max_score
		if max_score == temp_score_cuatros and "cuatros" not in Scorecard.scorecard:
			if flag == 1: return "cuatros" 
			else: return max_score
		if max_score == temp_score_cincos and "cincos" not in Scorecard.scorecard:
			if flag == 1: return "cincos" 
			else: return max_score
		if max_score == temp_score_seises and "seises" not in Scorecard.scorecard:
			if flag == 1: return "seises" 
			else: return max_score
		
		if max_score == temp_score_pup and "pupusa de queso" not in Scorecard.scorecard:
			if flag== 1: return "pupusa de queso" 
			else: return max_score
		if max_score == temp_score_pup_fri and "pupusa de frijol" not in Scorecard.scorecard: 
			if flag == 1: return "pupusa de frijol" 
			else:return max_score			
		if max_score == temp_score_elote and "elote" not in Scorecard.scorecard:	
			if flag ==1: return "elote" 
			else: return max_score
		if max_score == temp_score_triple and "triple" not in Scorecard.scorecard:
			if flag == 1: return "triple" 
			else: return max_score
		if max_score == temp_score_cuadruple and "cuadruple" not in Scorecard.scorecard:
			if flag == 1: return "cuadruple" 
			else: return max_score
		if max_score == temp_score_quintupulo and "quintupulo" not in Scorecard.scorecard: 
			if flag == 1: return "quintupulo" 
			else: return max_score
		if max_score == temp_score_tamal and "tamal" not in Scorecard.scorecard:	
			if flag == 1: return "tamal" 
			else: return max_score
		else: return 0
	def calc_prob(self,dice,scorecard):
		max_prob = []
		temp_dice = (list(product(dice,repeat=5)))
		for i in range(0,len(temp_dice)):
			max_prob.append(self.check(list(temp_dice[i]),scorecard,0))
		return temp_dice[max_prob.index(max(max_prob))]		
	
	def calc_unknown(self,dice,scorecard):
		max_prior = []
		priority = {"unos":1,"doses":2,"treses":3,"cuatros":4,"cincos":5,"seises":6,"pupusa de queso":7,"elote":8,"triple":9,"cuadrople":10,"pupusa de frijol":11,"cuadruple":12,"quintupulo":13,"tamal":14}
		prior_rev = {1:"unos",2:"doses",3:"treses",4:"cuatros",5:"cincos",6:"seises",7:"pupusa de queso",8:"elote",9:"triple",10:"cuadrople",11:"pupusa de frijol",12:"quintupulo",13:"tamal"}
		remaining = (list(scorecard.scorecard))
		for i in scorecard.Categories:
			if i not in remaining:
				max_prior.append(priority[i]) 
		return prior_rev[max(max_prior)]
				
			
									 
				
