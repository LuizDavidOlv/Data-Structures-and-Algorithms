import random
class RandomizedSet:

    def __init__(self):
        self.num_list = []
        self.hash_table = {}

    def insert(self, val: int) -> bool:
        if val not in self.hash_table:
            listLength = len(self.num_list)
            self.num_list.append(val)
            self.hash_table[val] = listLength
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.hash_table:
            return False
        
        index = self.hash_table[val]

        last_index = len(self.num_list)-1
        last_num = self.num_list[last_index]

        self.num_list[index] = last_num
        self.hash_table[last_num] = index

        self.num_list.pop()
        del self.hash_table[val]
        
        return True
       
        

    def getRandom(self) -> int:
        return random.choice(self.num_list)