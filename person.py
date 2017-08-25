from entity import Entity

class Person(Entity):
    def __init__(self, row, col):
        Entity.__init__(self, row, col)
