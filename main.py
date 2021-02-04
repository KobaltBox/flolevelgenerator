import json
from json import JSONEncoder
import random
from itertools import repeat

#STATIC CONSTANTS
BLOCK_TYPE = -1
ENEMY_TYPES = [0,1,2]
SPAWN_POSITIONS = [0,1,2,3,4,5]

#PARAMS
NUM_INCREMENTS = 20
LEVEL_NAME = 'Level-3'

class Level(object):
    def __init__(self, levelname):
        self.levelname = levelname
        self.increments = []
        
    def add(self, increment):
        self.increments.append(increment)


class SpawnIncrement:
    def __init__(self):
        self.time = round(random.uniform(1, 4), 2)
        self.spawns = []
        # Generate Random amount of spawns
        for i in repeat(None, random.randrange(1,5)):
            self.spawns.append(self.Spawn())
        
        for idx, val in enumerate(self.spawns[1:]):
            try:
                # If the position of one increment is the same as the previous, replace
                if(val.position == self.spawns[idx-1].position):
                    different_positions = list(SPAWN_POSITIONS)
                    different_positions.remove(int(val.position))
                    val.position = random.choice(different_positions)
            except (IndexError, ValueError):
                continue

        # Insert SpawnBlocks % chance
        block_tracker = 0
        if(random.random() * 100 < 70):
            print("Block Added")
            self.spawns[-1].type = BLOCK_TYPE


    class Spawn:
        def __init__(self):
            self.type = random.choice(ENEMY_TYPES)
            self.position = random.choice(SPAWN_POSITIONS)
            self.quantity = random.randrange(1,4)

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


if __name__ == '__main__':
    my_level = Level(LEVEL_NAME)
    print(my_level.levelname)
    # Generate Level
    for i in repeat(None, NUM_INCREMENTS):
        my_level.add(SpawnIncrement())

    # Output
    json_data = MyEncoder().encode(my_level)
    print(json_data)
    with open('output/' + LEVEL_NAME + '.json', 'w') as file:
        file.write(json_data)
