import numpy as np
def markerEqui1(marketShare,traProb):
    y1 = np.array([0]*len(marketShare))
    while not np.array_equal(marketShare,y1):
        y1 = marketShare
        marketShare = np.dot(marketShare,traProb)
        print marketShare
    return map(lambda x:round(x,4),marketShare)

class Marker(object):
    def markerEqui(self,markerShare,traProb):
        x = map(lambda x:round(x,7),np.dot(markerShare,traProb))
        if np.array_equal(markerShare,x):
            return map(lambda x:round(x,4),markerShare)
        else:
            return self.markerEqui(x,traProb)

m = Marker()
print m.markerEqui(np.array([.4,.6]),np.array([[.8,.2],[.1,.9]]))  
