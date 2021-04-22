import game

class Items:
    image = None
    itemID = 0

    def __init__(self, _itemID, _image):
        self.image = _image
        self.itemID = _itemID

class Nuke(Items):
    def __init__(self, _itemID = 1001):
        Items.__init__(self, None, _itemID)

    def DoEvent(self, gameFiled, filedWidth, filedHeight):
        field = []
        for i in range(filedHeight):
            new_line = []
            for j in range(filedWidth):
                new_line.append(0)
            field.append(new_line)

        return field

class ShiftLeft(Items):
    def __init__(self, _itemID = 1002):
        Items.__init__(self, None, _itemID)

    def DoEvent(self, gameFiled, filedWidth, filedHeight):
        for y in range(filedHeight):
            shift = 0
            for x in range(filedWidth):
                if gameFiled[y][x] == 0:
                    shift += 1
                else:
                    gameFiled[y][x - shift] = gameFiled[y][x]
        return gameFiled

class ShiftDown(Items):
    def __init__(self, _itemID = 1003):
        Items.__init__(self, None, _itemID)

    def DoEvent(self, gameFiled, filedWidth, filedHeight):
        shift = 0
        for x in range(filedWidth):
            for y in range(filedHeight):
                if gameFiled[y][x] == 0:
                    shift += 1
                else:
                    gameFiled[y - shift][x] = gameFiled[y][x]

        return gameFiled

class DeleteLine(Items):
    def __init__(self, _itemID = 1004):
        Items.__init__(self, None, _itemID)

    def DoEvent(self, gameFiled, filedWidth, filedHeight):
        gameFiled.pop(len(gameFiled) - 1)
        new_line = []
        for j in range(filedWidth):
            new_line.append(0)
        gameFiled.insert(0, new_line)

        return gameFiled