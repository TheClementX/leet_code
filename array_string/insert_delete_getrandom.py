from typing import * 
import random

class RandomizedSet: 
    def __init__(self): 
        self.key_map = dict() #map values to indices
        self.rand_arr = list() #store vals for random access

    def insert(self, val: int) -> bool:
        if val in self.key_map: return False

        self.rand_arr.append(val)
        self.key_map[val] = len(self.rand_arr) - 1
        return True

    def remove(self, val: int) -> bool: 
        if val not in self.key_map: return False

        if len(self.rand_arr) <= 1: 
            self.key_map = dict()
            self.rand_arr = list()
        elif self.rand_arr[-1] == val: 
            self.rand_arr.pop()
            self.key_map.pop(val)
        else:  
            val_idx = self.key_map.pop(val)
            back_val = self.rand_arr.pop()
            self.rand_arr[val_idx] = back_val 
            self.key_map[back_val] = val_idx

        return True

    def getRandom(self) -> int: 
        r_idx = random.randint(0, len(self.rand_arr)-1)
        return self.rand_arr[r_idx]


def test(): 
    r_set = RandomizedSet()

    assert(r_set.insert(2) == True)
    assert(r_set.insert(2) == False)
    assert(r_set.getRandom() == 2)
    print(r_set.rand_arr, r_set.key_map)

    assert(r_set.remove(2) == True)
    assert(r_set.remove(2) == False)

    r_set.insert(2)
    r_set.insert(3)
    r_set.insert(4)
    r_set.insert(5)
    r_set.insert(6)

    print(r_set.rand_arr, r_set.key_map)
    
    print("all tests passed")

if __name__ == "__main__": 
    test() 


    
