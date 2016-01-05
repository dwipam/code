"""    
--------------------------------------------------------------------------------
Authors: Srivatsan Iyer, Dwipam Katariya
    
Comparison of BFS and Astar with respect to Distance, Time, Segments
and considering route from 
1. Spencer,_Massachusetts to Bolto_Notch,_Connecticut 
2. Englewood,_Tennessee to Dalton,_Georgia 

we analyzed :

1. While considering Time with minimum time function and using BFS, computation 
   time on an average calculated is 214 milliseconds while using ASTAR it is 208 
   milliseconds.
2. While considering Distance with minimum distance function and using BFS, 
   computation time on an average 
   calculated is 201 milliseconds while using ASTAR it is 201 miliseconds.
3. While considering Segments with minimum segments function, ASTAR works similar
   to BFS and hence computation of both the algorithm remains the same.

DFS ends up into infinite loop as it goes on expanding the first node it gets at
every level. It also revisits the same set of cities back and forth. For example,
when start city = Englewood,_Tennessee and end city = Dalton,_Georgia, program goes
to and fro between Almond,_North_Carolina and Maryville,_Tennessee as both nodes
 are connected to each other with the least distance in the fringe.

AStar search seems to work the best for both "Time" and "Distance".

Heuristic Functions:

1) Distance: For distance, we simply calculate the curved distance
   (curve of the globe), between two coordinates. Whichever cities do not have
   longitude and latitude we calculate approximate coordinates.This is done by 
   drawing an imaginary line that joins the previous city and the goal city.
   The current city lies on this line at a distance equal to the length of the 
   highway from the previous city. 
2) Time: For time, we divide the curved distance by the maximum speed limit across
   all highways.This will always give us the least time required to get to the goal.
   Max Speed limit is used wherever the speed limit is not present
3) Segments: For segments, the heuristic function is h(n) = 1. This makes AStar
   search equivalent to BFS.

The estimates based on curved distances between two coordinates produce good 
heuristics judging from the results.

Scope for improvement:
1) We can pre-calculate some of the distances, segments, and time to major cities. 
This will make it more accurate heuristic. 
--------------------------------------------------------------------------------
"""

import sys
from collections import defaultdict
from math import sin, cos, sqrt, atan2, radians, asin, acos, degrees

MAX_SPEED_LIMIT = 40
EARTH_RADIUS = 3959.0

class Meta(object):
	def __init__(self):
		self.pathCost = 0
		self.cities = []
		self.totalTime = 0
		self.totalDistance = 0
		self.heurisiticValue = 0
	
	def __repr__(self):
		return "%d %f"%(self.totalDistance, self.totalTime) + " " +  " ".join(x.name for x in self.cities)
	
class City(object):
	def __init__(self, name, latitude=None, longitude=None):
		self.name = name
		self.latitude = latitude
		self.longitude = longitude
		self.empty = (not latitude) and (not longitude)
	
	def hasGPS(self):
		return self.latitude is not None or self.longitude is not None
	
	def location(self):
		return (self.latitude, self.longitude) if self.hasGPS() else (self.tempLat, self.tempLong)
			
	def __eq__(self, other):
		return self.name == other.name

	def __hash__(self):
		return hash(self.name)
	
	def __repr__(self):
		return "<City: '%s' (%f, %f)>"%(self.name, self.latitude, self.longitude)
	
class Highway(object):
	def __init__(self, city1, city2, length, speedLimit, name):
		self.city1 = city1
		self.city2 = city2
		self.length = length
		self.speedLimit = speedLimit
		self.time = length / float(speedLimit)
		self.name = name
	
	def __repr__(self):
		return "<Highway: '%s' %s => %s>"%(self.name, repr(self.city1), repr(self.city2))

class CityStore(object):
	def __init__(self, f):
		cities = {} 
		for line in f:
			if not line.strip():
				continue
			cityObj = self.parseCity(line.rstrip())
			cities[cityObj.name] = cityObj
		self.cities = cities

	def parseCity(self, line):
		name, lat, lon = line.strip().split()
		return City(name, float(lat), float(lon))

class HighwayStore(object):
	def __init__(self, f, cityStore):
		self.cityStore = cityStore
		highways = {}
		outwardHighways = defaultdict(list)
		for line in f:
			if not line.strip():
				continue
			highwayObj1 = self.parseHighway(line.rstrip())
			highwayObj2 = self.parseHighway(line.rstrip())
			highwayObj2.city1, highwayObj2.city2 = highwayObj2.city2, highwayObj2.city1
			highways[(highwayObj1.city1, highwayObj1.city2)] = highwayObj1
			highways[(highwayObj2.city2, highwayObj2.city1)] = highwayObj2
			outwardHighways[highwayObj1.city1].append(highwayObj1)
			outwardHighways[highwayObj2.city1].append(highwayObj2)
		self.highways = highways
		self.outwardHighways = outwardHighways

	def parseHighway(self, line):
		cityName1, cityName2, length, speedLimit, name = line.strip().split(" ")
		city1 = self.cityStore.cities.setdefault(cityName1, City(cityName1, None, None))
		city2 = self.cityStore.cities.setdefault(cityName2, City(cityName2, None, None))
		return Highway(city1, city2, int(length), int(speedLimit or '0') or MAX_SPEED_LIMIT, name)
	
	def getOutwardHighways(self, city1, sortKey):
		return sorted(self.outwardHighways[city1], key=sortKey)
	
	def maxSpeed(self):
		return max(x.speedLimit for x in self.highways.itervalues())

class BFSSearch(object):
	def search(self, node, successorFn, pathCostFn, sortKey, goal, heuristic=None):
		m = Meta()
		m.cities = [node]
		fringe = [(node, m)]

		while fringe:
			curCity, meta = fringe.pop(0)
			print "Current Meta:", meta

			if curCity == goal:
				return curCity, meta
			outwardHighways = successorFn(curCity, sortKey)
			for highway in outwardHighways:
				nextCity = highway.city2
				m = Meta()
				m.pathCost = meta.pathCost + pathCostFn(highway)
				m.totalTime = meta.totalTime + highway.time
				m.totalDistance = meta.totalDistance + highway.length
				m.cities = meta.cities + [nextCity]
				fringe.append((nextCity, m))

		
class DFSSearch(object):
	def search(self, node, successorFn, pathCostFn, sortKey, goal, heuristic=None):
		m=Meta()
		m.cities=[node]
		fringe = [(node,m)]

		while fringe:
			curCity, meta = fringe.pop(0)
			if curCity == goal:
				return curCity, meta
			print meta
			outwardHighways = successorFn(curCity, sortKey)
			for highway in outwardHighways : 	
				nextCity = highway.city2
				m = Meta();
				m.pathCost = meta.pathCost + pathCostFn(highway)
				m.totalTime = meta.totalTime + highway.time
                                m.totalDistance = meta.totalDistance + highway.length
                                m.cities = meta.cities + [nextCity]

				fringe.insert(0,(nextCity, m))

class AStarSearch(object):
	def search(self, node, successorFn, pathCostFn, sortKey, goal, heuristicFn):
		m = Meta()
		m.cities = [node]
		fringe = [(node, m)]

		while fringe:
			obj = min(fringe, key=lambda x: x[1].heurisiticValue + x[1].pathCost)
			fringe.remove(obj)
			curCity, meta = obj
			print "Current meta:", meta

			if curCity == goal:
				return curCity, meta

			outwardHighways = successorFn(curCity, sortKey)
			for highway in outwardHighways:
				nextCity = highway.city2
				m = Meta()
				m.pathCost = meta.pathCost + pathCostFn(highway)
				m.totalTime = meta.totalTime + highway.time
				m.totalDistance = meta.totalDistance + highway.length
				m.cities = meta.cities + [nextCity]
				if not nextCity.hasGPS():
					fixTempLocation(curCity, nextCity, goal, highway)
				m.heurisiticValue = heuristicFn(nextCity)
				fringe.append((nextCity, m))

def fixTempLocation(curCity, nextCity, goal, highway):
        """
        Author: David M (http://stackoverflow.com/users/493559/david-m)
        The function below is used to get the position of the second point, given
        the first point and the angle. Modified a bit to suit our case. Read the
        text at the beginning of the file for more info on how the temporary location
        is being fixed.
        """
	lat1, long1 = map(radians, curCity.location())
	lat2, long2 = map(radians, goal.location())
	dx = long2 - long1
	dy = lat2 - lat1
	angle = atan2(dy, dx)

        endLat = asin(sin(lat1)*cos(highway.length/EARTH_RADIUS) +
                        cos(lat1)*sin(highway.length/EARTH_RADIUS)*cos(angle))
        endLong = long1 + atan2(sin(angle)*sin(highway.length/EARTH_RADIUS)*cos(lat1),
                        cos(highway.length/EARTH_RADIUS) - sin(lat1)*sin(endLat))

	nextCity.tempLat = degrees(endLat)
	nextCity.tempLong = degrees(endLong)

def curvedDistance(pos1, pos2):
	"""
	Author: Michael0x2a (http://stackoverflow.com/users/646543/michael0x2a)
	The function below was found on StackOverflow: http://stackoverflow.com/a/19412565/227884
	"""
	lat1, long1 = pos1
	lat2, long2 = pos2
	lat1 = radians(lat1)
	lon1 = radians(long1)
	lat2 = radians(lat2)
	lon2 = radians(long2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	return  EARTH_RADIUS * c

def main():
	with open("city-gps.txt") as f:
		cityStore = CityStore(f)
	
	with open("road-segments.txt") as f:
		highwayStore = HighwayStore(f, cityStore)

	MAX_SPEED_LIMIT = highwayStore.maxSpeed()

	startCity = cityStore.cities[sys.argv[1]]
	endCity = cityStore.cities[sys.argv[2]]
	routingOption = sys.argv[3]
	routingAlgo = sys.argv[4]

	searches = {"bfs": BFSSearch, "dfs": DFSSearch, "astar": AStarSearch}

	cityDistToGoal = lambda city: curvedDistance(city.location(), endCity.location())

	options = {
		"segments": {
			"pathCostFn": lambda highway: 1,
			"sortKey": lambda highway: -highway.length,
			"heuristicFn": lambda city: 1, #Dummy
		},
		"time": {
			"pathCostFn": lambda highway: highway.time,
			"sortKey": lambda highway: highway.time,
			"heuristicFn": lambda city: cityDistToGoal(city) / MAX_SPEED_LIMIT
		},
		"distance": {
			"pathCostFn": lambda highway: highway.length,
			"sortKey": lambda highway: highway.length,
			"heuristicFn": lambda city:	cityDistToGoal(city)
		}
	}
	curOptions = options[routingOption]
	
	search = searches[routingAlgo]().search
	goal, meta = search(node=startCity, 
						successorFn=highwayStore.getOutwardHighways,
						goal=endCity,
						**curOptions)

	print meta	

if __name__ == '__main__':
	main()
