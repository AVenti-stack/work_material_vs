# TODO: LINKED LIST 
# TODO: ARRAYS
# TODO: QUEUES
# TODO: STACKS


# TODO: HASHMAPS
# USECASE: 
class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if key in self.map:
            return self.map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.map:
            self.map.pop(key)
        
