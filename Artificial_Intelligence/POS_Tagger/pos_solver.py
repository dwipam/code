###################################
# CS B551 Fall 2015, Assignment #5
#
# Your names and user ids : Dwipam Katariya, Srivatsan Iyer
#                           ddkatari@iu.edu, srriyer@iu.edu
#
# (Based on skeleton code by D. Crandall)
#
#
####
# Analysis:
"""
(1) We have implemented the program for NaiveBaye's, Gibbs Sampling, MaxMarginal Inference
    and HMM Viterbi Deconding. During the learning stage, we store the results of P(Word),
    P(Speech),P(Speech|Word) and P(Word|Speech) in a dictionary based on the training data.
    This is implemented for the learning stage. Now we apply above mentioned algorithms on
    the test data to predict the appropriate part of speech. 
    For NaiveBaye's, we compute the maximum probable part of speech for the given word from 
    the dictonary.
    For MCMC Gibbs Sampling, we compute by default 400 samples as the algorithm.
    First Sample we select at random for the test data, only the first element in further 
    samples are calculated dependent on previous sample. and others are dependent on current
    element that was computed. If time complexity is the factor, we suggest to reduce the 
    sample count from 400 to 10 because, execution time would improve dramatically. This you
    can do by changing the variable name global varaible MCMC_SAMPLE.
    For words that are not in the learned dictonary, we choose the part of speech based upon
    the neighbouring elements, both previous and next elements and then assign the part of 
    speech with the highest probability. For example P(nick's=noun|S1=noun,S3=Verb), so we 
    calculate for 'nick's'= other 11 part of speech and then select the part of speech with 
    max probability. 
    For Max Inference, for each word, we compute the highest occurence of the part of speech
    in all the samples that were computed in MCMC Gibs Sampling, and assign the same. 
    For HMM Viterbi, we follow the computation steps for the next state dependent upon the 
    already computed value for previous state.
(2) For the bc.test data we get following results based on multiple runs:
    So far scored 2000 sentences with 29442 words.
                   Words correct:     Sentences correct: 
   0. Ground truth:      100.00%              100.00%
          1. Naive:       91.84%               38.30%
        2. Sampler:       87.43%               26.75%
   3. Max marginal:       88.52%               29.15%
            4. MAP:       93.16%               44.40%
           5. Best:       90.05%               32.55%
(3) While programming, we faced the problem of time efficiency with the number of sampler,
    then we noticed after multiple runs and variation, Score for the same does not largely
    vary, but the execution time dramatically varies.
    When we checked the pos_scorer.py. we noticed that only the first sample is being used
    for scoring purposes, so we picked the last few samples and reveresed the order, so that
    the sample being picked for scoring is the last sample.
(4) Implementation of best algorithm:
    For the purposes of the best algorithm we have chosen, naive baye's, MAP and Max-Marginal
    We put the three algorithms, through a voting process, where they vote on the best part
    of speech for a given word. For each of the word, the part of speech with the larges number
    of votes wins.
    Additionaly we have dynamically allocated the part of speech to punctuations based on training
    data.


FUTURE IMPROVEMENTS: 
 -  We can improve this algorithm, by calculating the sequence of part of speech for the entire
    sentence, and then improve the values for the next part of speech
 -  We can also use the adaptive learning by updating the probability values of the learned data 
    while we are allocating the part of speech to the word, this way, if we encounter right part of
    speech in the first sentence we would skip the chance of being wrong for the word in the next 
    sentence. 
 -  Specific to Viterbi algorithm, we are currently considering only the previous word to calculate the
    probability of the next word. We can improvise on this one, by giving it more words. In other
    words increase the context that is being used for prediction. In the training phase, we can 
    calculate the probability of the words and states given the previous two words and previous 
    two states.
    
"""

####
import random
from bisect import bisect
import math
from collections import Counter, defaultdict
from itertools import product

# We've set up a suggested code structure, but feel free to change it. Just
# make sure your code still works with the label.py and pos_scorer.py code
# that we've supplied.
#
MCMC_SAMPLES = 400
def print_table(t, s, w):
    """
    Prints the viterbi table.
    """
    for _, row in t.items():
        for _, cell in row.items():
            if isinstance(cell, int):
                print "%7d"%cell,
            else:
                print "%5.2f"%cell,
        print


class Solver:
    def __init__(self):
        self.prob_s = {}
        self.prob_s1_s2 = {}
        self.prob_w_s = {}
        self.prob_w = {}
        self.prob_start_s = {}
        self.mcmc_dict = []

    # Calculate the log of the posterior probability of a given sentence
    #  with a given part-of-speech labeling
    def posterior(self, sentence, label):
        """ Calculate the posterior probability"""
        res = sum(math.log(self.prob_s_w1.get((s, w), 0.00000001)) for s, w in zip(label, sentence))
        for index in range(len(label) -1):
            s1 = label[index]
            s2 = label[index + 1]
            v = self.prob_s1_s2.get((s2, s1), 0.00000001)
            res += math.log(v)
        res -= math.log(sum(self.prob_w_s.get((w, s), 0.00001) * 
                    self.prob_s.get(s, 0.00001)
                    for s, w in zip(label, sentence)))

        return res

    # Do the training!
    #
    def train(self, data):
        all_s = Counter()                       #Count of all parts of speech
        all_ss = Counter()                      #Count of all pairs of part of speech
        all_ws = Counter()                      #Count of all pairs of words/part of speech.
        all_w = Counter()                       #Count of all words.
        start_s = Counter()                     #Count of all starting words.

        self.puncts = set()                     #Set of all punctuations.

        for index, line in enumerate(data):
            line = zip(*line)
            for word, typ in line:
                all_s[typ] += 1
                all_ws[(word, typ)] += 1
                all_w[word] += 1

                if typ == ".":
                    self.puncts.add(word)

            for (w1, t1), (w2, t2) in zip(line, line[1:]):
                all_ss[(t1,t2)] += 1
            start_s[line[0][1]] += 1

        all_s_count = sum(all_s.values())
        start_s_count = sum(start_s.values())
        all_w_count = sum(all_w.values())

        #Use count(items)/totalItems for all probability calculations.
        self.prob_w = {k: v/float(all_w_count) for k,v in all_w.iteritems()}
        self.prob_s = {k: v/float(all_s_count) for k,v in all_s.iteritems()}
        self.prob_s1_s2 = {(t1,t2):float(v)/all_s[t1] for (t1, t2), v in all_ss.iteritems()}
        self.prob_w_s = {(w,t):float(v)/all_s[t] for (w,t), v in all_ws.iteritems()}

        self.prob_s_w1 = {(t,w):float(v)/all_w[w] for (w,t), v in all_ws.iteritems()}
        self.prob_s_w2 = {(t,w):(v * self.prob_s[t]) / self.prob_w[w]
                             for (w,t), v in self.prob_w_s.iteritems()}

        self.prob_start_s = {t: v/float(start_s_count) for t,v in start_s.iteritems()}

    # Functions for each algorithm.
    #
    def naive(self, sentence):
        res = [max([s for s in self.prob_s.keys()], key=lambda x: self.prob_s_w1.get((x, w), 0)) for w in sentence]
        self.results_naive = res
        return [[res], []]

    def mcmc(self, sentence, sample_count):
      #  return [ [ ["noun"] * len(sentence) ] * sample_count, [] ]
        result = []
        temp_dict = [None] * len(sentence)
        for i in range(0,len(sentence)):
            temp_dict[i]=self.prob_s.keys()[random.choice(range(0,len(self.prob_s)))] 
        result.append(temp_dict)
        for sample in range(1,MCMC_SAMPLES):
            prev_sample = result[sample-1]
            next_sample = [None] * len(sentence)
            for i in range(0,len(sentence)):
                if sentence[i] not in self.prob_w:
                    if len(prev_sample)==1:
                        next_sample[i] = self.calc_weight(None,None,prev_sample[i])
                    elif i==0:
                        next_sample[i] = self.calc_weight(None,None,prev_sample[i+1])
                    elif i == len(sentence)-1:
                        next_sample[i] = self.calc_weight(prev_sample[i-1],None,None)
                    else:
                        next_sample[i] = self.calc_weight(prev_sample[i-1],None,prev_sample[i+1])
                elif len(prev_sample)==1:
                    next_sample[i] = self.calc_weight(None,sentence[i],prev_sample[i]) 
                elif i == 0:
                    next_sample[i] = self.calc_weight(None,sentence[i],prev_sample[i+1])
                elif i == len(sentence)-1:
                    next_sample[i] = self.calc_weight(prev_sample[i-1],sentence[i],None)
                else:
                    next_sample[i] = self.calc_weight(prev_sample[i-1],sentence[i],prev_sample[i+1])
            result.append(next_sample)
        self.mcmc_dict = result
        return [ result[::-1][0:sample_count], [] ]

    def calc_weight(self,prev_sample,word,next_sample):
        """
        This function calculates the part of speech for the element in 
        the next sample
        We have handled all the conditions, of word not in the train data
        as decribed in analysis, combination of noun and adjective not in
        train data.
        """
        #impor pdb;pdb.set_trace()
        available_choices = []
        for speech in self.prob_s.keys():
            if prev_sample == None and word != None:
                value = self.prob_w_s.get((word,speech),self.calc_dummy_word(word,speech))*self.prob_s1_s2.get((next_sample,speech),self.calc_dummy(next_sample,speech))
            elif next_sample == None and word != None:
                value = self.prob_w_s.get((word,speech),self.calc_dummy_word(word,speech))*self.prob_s1_s2.get((speech,prev_sample),self.calc_dummy(speech,prev_sample))
            elif prev_sample !=None and next_sample != None and word != None:
                value = self.prob_w_s.get((word,speech),self.calc_dummy_word(word,speech))*self.prob_s1_s2.get((next_sample,speech),self.calc_dummy(next_sample,speech))*self.prob_s1_s2.get((speech,prev_sample),self.calc_dummy(speech,prev_sample))
            elif prev_sample == None and word == None:
                value = self.prob_s1_s2.get((next_sample,speech),self.calc_dummy(next_sample,speech))
            elif next_sample == None and word == None:
                value = self.prob_s1_s2.get((speech,prev_sample),self.calc_dummy(speech,prev_sample))
            elif prev_sample !=None and next_sample != None and word ==None:
                value = self.prob_s1_s2.get((next_sample,speech),self.calc_dummy(next_sample,speech))*self.prob_s1_s2.get((speech,prev_sample),self.calc_dummy(speech,prev_sample)) 
            available_choices.append([speech,value])
        return self.weightedChoice(available_choices)
    def calc_dummy(self,next_sample,speech):
            value = self.prob_s1_s2.get((speech,next_sample),0)*self.prob_s.get((next_sample),0)/self.prob_s.get((speech),0)
            return value
    def calc_dummy_word(self,word,speech):
            value = self.prob_s_w1.get((speech,word),0)*self.prob_w.get((word),0)/self.prob_s.get((speech),0)
            return value
    def weightedChoice(self,keys):
        """
        This function returns the random choice for the sampler as per the
        probability weights, this means if a=0.1 and b=0.9 out of 10 iterations
        atleast a will be return once and b other times. 
        We do this, by taking the sum of the weights for the respective part of
        speech and then store it in an array. We multiply the total weights by 
        a random float value with a rando function and then use bisect function
        to get the index location to insert the value, hence probable times it 
        will occur that, index will the returned as per proabability.
        """
        speech, prob = zip(*keys)
        prob_tot = 0
        prob_array = []
        for each_prob in prob:
                prob_tot+= each_prob
                prob_array.append(prob_tot)
        pos_bis = random.random()*prob_tot
        index = bisect(prob_array, pos_bis)
        if index == len(speech):
            index=index-1
        return speech[index]

    def best(self, sentence):
        """
        Puts the three below algos to a voting process, and picks the best one of of them.
        """
        res = [max(x) for x in zip(self.results_max_marginal, self.results_viterbi, self.results_naive)]
        for index, (state, word) in enumerate(zip(res, sentence)):
            if word in self.puncts:
               res[index] = "."
        return [ [ res ], [] ]

    def max_marginal(self, sentence):
        max_margin_dict = []
        post_prob = []
        for i in range(0,len(sentence)):
            temp = []
            for sample in self.mcmc_dict:
                temp.append(sample[i])
            speech = Counter(temp).keys()
            occurence = Counter(temp).values()
            
            max_margin_dict.append(speech[occurence.index(max(occurence))])
            post_prob.append(float(max(occurence))/float(len(self.mcmc_dict)))
        self.results_max_marginal = max_margin_dict
        return [ [max_margin_dict], [post_prob,] ]

    def calc_postprob(self,max_margin_dict,sentence,occurence):
        post_prob = []
        for i in range(0,len(sentence)):
            post_prob.append(self.prob_s_w1.get((max_margin_dict[0],sentence[i]),0.00001))
        return post_prob

    def viterbi(self, sentence):
        l = math.log
        t1 = defaultdict(dict)
        t2 = defaultdict(dict)
        t = len(sentence)
        MIN = 0.00001

        #Using pseudocode from Wikipedia: https://www.wikiwand.com/en/Viterbi_algorithm#/Pseudocode
        all_states = self.prob_s.keys()
        for i, s in enumerate(all_states):
            t1[i][0] = l(self.prob_start_s.get(s, MIN)) + \
                            l(self.prob_w_s.get((sentence[0], s), MIN))
            t2[i][0] = 0

        for i in range(1,t):
            for j, s in enumerate(all_states):
                maxItem = (-1e10, -1)
                for k, new_state in enumerate(all_states):
                    prevProb = t1[k][i-1]
                    transProb = self.prob_s1_s2.get((new_state, s), MIN)
                    emissProb = self.prob_w_s.get((sentence[i], s), MIN)
                    curProb = prevProb + l(transProb) + l(emissProb)
                    curItem = curProb, k
                    if curItem > maxItem:
                        maxItem = curItem
                t1[j][i], t2[j][i] = maxItem

        z = [0] * t
        z[t-1] = max(range(len(all_states)), key=lambda k: t1[k][len(sentence)-1])
        result = [all_states[z[t-1]]]
        for i in range(t-1, 0, -1):
            z[i-1] = t2[z[i]][i]
            result = [all_states[z[i-1]]] + result
        
        self.results_viterbi = result
        return [[result], []]

    # This solve() method is called by label.py, so you should keep the interface the
    #  same, but you can change the code itself. 
    # It's supposed to return a list with two elements:
    #
    #  - The first element is a list of part-of-speech labelings of the sentence.
    #    Each of these is a list, one part of speech per word of the sentence.
    #    Most algorithms only return a single labeling per sentence, except for the
    #    mcmc sampler which is supposed to return 5.
    #
    #  - The second element is a list of probabilities, one per word. This is
    #    only needed for max_marginal() and is the marginal probabilities for each word.
    #
    def solve(self, algo, sentence):
        if algo == "Naive":
            return self.naive(sentence)
        elif algo == "Sampler":
            return self.mcmc(sentence, 5)
        elif algo == "Max marginal":
            return self.max_marginal(sentence)
        elif algo == "MAP":
            return self.viterbi(sentence)
        elif algo == "Best":
            return self.best(sentence)
        else:
            print "Unknown algo!"

