from Perlin import perlingrid as pGrid
from City import City
from Road import Road
from math import ceil,tanh,sqrt
from random import randint
import numpy as np



class World_map:
    def __init__(self, w, h, tile_size, seed, size):
        self.tiles = []
        self.width = w
        self.height = h
        self.tile_size = tile_size
        self.seed = seed
        self.size = size

        self.cities = []
        self.roads = []

        #confine variabels
        if size < 1:
            size = 1
        elif size > 10:
            size = 10

        self.dimensions = w
        if w < h:
            self.dimensions = h
        
        #Generate map
        
        p = pGrid(size, self.dimensions, self.seed)

        #Find extremedies
        i,j = np.unravel_index(p.argmin(), p.shape)
        min_val = p[i,j]
        i,j = np.unravel_index(p.argmax(), p.shape)
        max_val = p[i,j]

        size_val = max_val
        if size_val < abs(min_val):
            size_val = abs(min_val)

        for x in range(w):
            self.tiles.append([])
            for y in range(h):
                tile = tanh(p[x][y]/(0.45*(size_val/0.5)))*0.5+0.5
                #tile = p[x][y]
                """
                if (x, y) == max_pos:
                    b_type = (-1, (255,0,0))
                elif (x, y) == min_pos:
                    b_type = (-1, (255,255,0))
                """
                if tile < 0.2:
                    b_type = (0, (13 - tile * 54, 61 - tile * 57, 120 - tile * 61), 0.2) #Water
                elif tile < 0.22:
                    b_type = (1, (246, 220, 55), 0.75) #Beach
                elif tile < 0.65:
                    b_type = (2, (146, 203, 54), 1.25) #Grassland
                elif tile < 0.7:
                    b_type = (3, (107, 164, 15), 1) #Highlands
                elif tile < 0.8:
                    b_type = (4, (-45 * (tile-0.7)*10 + 140, -45 * (tile-0.7)*10 + 140, -45 * (tile-0.7)*10 + 140), 0.6) #Mountain
                else:
                    b_type = (5, (55 * (tile-0.8)*5 + 200, 55 * (tile-0.8)*5 + 200, 55 * (tile-0.8)*5 + 200), 0.45) #Mountain_top_snow
                self.tiles[x].append(b_type)

        # City generation
        for i in range(100):
            pos = (randint(8,w-8), randint(8,h-8))
            if self.tiles[pos[0]][pos[1]][0] == 2: # checks if city bouandaries are okay
                if self.tiles[pos[0]][pos[1]-4][0] == self.tiles[pos[0]-4][pos[1]][0] == self.tiles[pos[0]+4][pos[1]][0] == self.tiles[pos[0]][pos[1]+4][0] == 2:
                    good_pos = True
                    for city in self.cities:
                        if dist(pos, city.pos) < 25:
                            good_pos = False
                    if good_pos:
                        self.cities.append(City(pos))
        
        # Road generation
        connected_cities = []
        city_distances = []
        self.generato_roado(self.cities[0],connected_cities,city_distances)

    def generato_roado(self,current,connected,distances):
        if len(distances) == 0 and len(connected) > 0:
            return True
        connected.append(current)
        shortest = None
        for c2 in self.cities:
            if (current is not c2) and (c2 not in connected):
                distances.append([current,c2,dist(current.pos, c2.pos)])
        for distance in distances:
            if distance[1] not in connected:
                if shortest is None:
                    shortest = distance
                elif distance[2] < shortest[2]:
                    shortest = distance
            else:
                distances.remove(distance)
        
        if shortest is None:
            return True

        self.roads.append(Road(shortest[0].pos, shortest[1].pos))
        
        if self.generato_roado(shortest[1],connected,distances):
            return True
        
        
        


def dist(P1,P2):
    return sqrt(((P1[0] - P2[0])**2) + ((P1[1] - P2[1])**2))

def uniq(lst):
    seen = set()
    uniq = []
    for i in lst:
        if i not in seen:
            uniq.append(i)
            seen.add(i)
    return uniq