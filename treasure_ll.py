import time

# treasure is a string which will represents the nodes data
# map will represent the link between nodes acting narrative treasure map


class Node:
    def __init__(self, treasure=None, map=None):
        self.treasure = treasure
        self.map = map


class Treasure_trail:
    def __init__(self):
        self.treasure = None

    def first_treasure(self, treasure):
        node = Node(treasure, self.treasure)
        self.treasure = node

    # function to insert list of treasure items
    def insert_treasure_trail(self, treasure_contents):
        self.treasure = None
        for items in treasure_contents:
            self.insert_at_end(items)

    # function to print out the contents of the linked list
    def print(self):
        if self.treasure is None:
            print('There is no treasure here')

        itr = self.treasure
        treasure_chest = " "

        while itr:
            treasure_chest += str(itr.treasure) + "--->"
            itr = itr.map
        print(treasure_chest)

    # function to access length of linked list
    # Will help with indexing along length of linked list
    def get_length(self):
        count = 0
        itr = self.treasure
        while itr:
            count += 1
            itr = itr.map

        return count

    def insert_at_end(self, treasure):
        if self.treasure is None:
            self.treasure = Node(treasure, None)
            return

        itr = self.treasure
        while itr.map:
            itr = itr.map

        itr.map = Node(treasure, None)

    # insert nodes within the linked listt
    def insert_treasure(self, index, treasure):
        if index < 0 or index > self.get_length():
            raise Exception(
                "You have to leave the treausre within the treasure trail")

        if index == 0:
            self.first_treasure(treasure)
            return

        itr = self.treasure
        count = 0
        while itr:
            if count == index - 1:
                node = Node(treasure, itr.map)
                itr.map = node
                break

            itr = itr.map
            count += 1

        return count
    '''
    # remove nodes by their index
    def remove_treasure(self, index, treasure):
        if index < 0 or index >= self.get_length():
            raise Exception(
                "You have to leave the treausre within the treasure trail")

        if index == 0:
            self.treasure = self.treasure.map
            return

        itr = self.treasure
        count = 0
        while itr:
            if count == index - 1:
                itr.map = itr.map.map
                break
            itr = itr.map
            '''

    def remove_treasure(self, treasure):
        if self.treasure is None:
            return

        if self.treasure == treasure:
            self.treasure = self.treasure.map
            return

        itr = self.treasure
        while itr.map:
            if itr.map.treasure == treasure:
                itr.map = itr.map.map
                break
            itr = itr.map


if __name__ == "__main__":
    tt = Treasure_trail()
    #name = input("Hello young pirate ,what is your name? ---> ")
    #print(f"Nice to meet ya " + {"name"} + "!")
    time.sleep(2)
    print("I'll direct you to the Silver coins, after that you'll have to follow the links")
    print("Here is your map")
    time.sleep(2)
    print("I'll admit, I don't know where the last treasure is, if you obtain a map take it out and give it a read")
    print(
        ["Silver Coins", "Gold", "Precious Jewels", "New Treasure Map", "Rare Artefact"])
    tt.insert_treasure(0, "Silver Coins")
    tt.print()
    time.sleep(2)
    tt.insert_treasure(1, "Gold")
    tt.print()
    time.sleep(2)
    tt.insert_treasure(2, "Precious Jewels")
    tt.print()
    time.sleep(3)
    tt.insert_treasure(3, "New Treasure Map")
    tt.print()
    time.sleep(4)
    print("That's it!!! The map to the final treasure...  If you find it, you'll be...  the King of the Pirates!!!")
    time.sleep(2)
    tt.remove_treasure("New Treasure Map")
    tt.print()
    time.sleep(3)
    print("Obtained The Final Treasure Map!")
    time.sleep(2)
    tt.insert_treasure(3, "Rare Artefact")
    tt.print()
    time.sleep(5)
    print(
        "You've done it!!! I can't believe you actually did it... Congratulations!!! You're the king of the pirates!!!")
    print("Don't forget to take all of your rewards")
    tt.remove_treasure("Silver Coins")
    tt.remove_treasure("Gold")
    tt.remove_treasure("Precious Jewels")
    tt.remove_treasure("Rare Artefact")
    tt.print()
    time.sleep(3)
    print("A great pirate will be remembered if they leave a great treasure,  you should create your own legendary trail!")
    tt.insert_treasure(0, "Diamonds")
    tt.insert_treasure(1, "Legnedary Sword")
    tt.insert_treasure(2, "Gold Pieces")
    tt.insert_treasure(3, "Picure of our pirate crew")
    tt.print()
    time.sleep(5)
    print("So Pirate King... Where will our next adventure take us? ")
