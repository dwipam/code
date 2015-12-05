###################################
# CS B551 Fall 2015, Assignment #5
# 
# Scoring code by D. Crandall
#
# PLEASE DON'T MODIFY THIS FILE.
# Edit pos_solver.py instead!
#

class Score:
    def __init__(self):
        self.word_scorecard = {}
        self.sentence_scorecard = {}
        self.word_count = 0
        self.sentence_count = 0


    def score(self, algo_outputs):
        gt = algo_outputs["0. Ground truth"][0][0]
        self.word_count += len(gt)
        self.sentence_count += 1

        for algo,labels in algo_outputs.items():
            labels = labels[0][0]
            correct = 0
            for j in range(0, len(gt)):
                correct += 1 if gt[j] == labels[j] else 0
        
            self.word_scorecard[algo] = self.word_scorecard.get(algo, 0) + correct
            self.sentence_scorecard[algo] = self.sentence_scorecard.get(algo, 0) + (correct == len(gt))


    def print_scores(self):
        print ""
        print "==> So far scored %d sentences with %d words." % (self.sentence_count, self.word_count)
        print "                   Words correct:     Sentences correct: "
        
        for i in sorted(self.word_scorecard):
            print "%18s:     %7.2f%%             %7.2f%%" % (i, self.word_scorecard[i]*100 / float(self.word_count), self.sentence_scorecard[i]*100 / float(self.sentence_count))


    @staticmethod
    def print_helper(description, list, sentence):
        print (("%26s" % description) + ": " + " ".join([(("%-" + str(max(4,len(sentence[i]))) + "s") % list[i]) for i in  range(0,len(list)) ] ) )

    @staticmethod
    def print_results(sentence, outputs, posteriors):
        Score.print_helper("", sentence, sentence)
        for algo in sorted(outputs.keys()):
            for j in range(0, len(outputs[algo][0])):
                Score.print_helper((algo if j==0 else "") + " (%7.2f)" % posteriors[algo][j], outputs[algo][0][j], sentence)
            for j in range(0, len(outputs[algo][1])):
                Score.print_helper("", outputs[algo][1][j], sentence)

