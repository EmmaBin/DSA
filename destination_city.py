#https://leetcode.com/problems/destination-city/

#two ways to solve this problems: set() and dictionary()

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #destion city is the city only appear once and at last index 
        departure = set()
        all_cities = set()

        for cities in paths:
            all_cities.add(cities[0])
            all_cities.add(cities[1])
            departure.add(cities[0])
        return (all_cities-departure).pop()


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
		# Get the source (start), which is the initial point
        source = paths[0][0]
        
		# Create a dictionary to map each source with its destination (source -> destination)
        graph = {source: destination for source, destination in paths}
        
		# Iterate over the graph, if you can not visit any city from you current position, you reached the end
		current = source
        while current in graph:
            current = graph[current]
        
		# Return your current position which is the destination
        return current

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityMap = {} #will keep the track of all paths cityA->cityB
        for city1, city2 in paths:
            cityMap[city1] = city2
            
        for city1,city2 in paths:
            #if cityB(final Destination) does not serve as starting point.
            if city2 not in cityMap: 
                return city2


