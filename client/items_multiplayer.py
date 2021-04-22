import items_singleplayer as items
# ToDo: create child class of all singleplayer items

# ToDo: implement
class RandomBlocks(items.Items):
    def __init__(self):
        items.Items.__init__(self, None, 2001)

    def DoEvent(self, gameFiled, filedWidth, filedHeight):
        return gameFiled

# ToDo: implement
class SwapFiled(items.Items):
    def __init__(self):
        items.Items.__init__(self, None, 2002)

    def DoEvent(self, gameFiled, filedWidth, filedHeight):
        return gameFiled

# ToDo: implement
class AddLine(items.Items):
    def __init__(self):
        items.Items.__init__(self, None, 2003)

    def DoEvent(self, gameFiled, filedWidth, filedHeight):
        return gameFiled