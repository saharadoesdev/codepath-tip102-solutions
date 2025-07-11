# This was a live share so I didn't do all of this

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    # ... methods from previous problems
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(c.isalpha() or c.isspace() for c in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
        valid_items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid_items:
            self.furniture.append(item_name)
        
    def print_inventory(self):
        # Implement the method here
        items = dict()
        if not self.furniture:  
            print("Inventory empty")
        for item in self.furniture:
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        result = ", ".join(f"{item}: {count}" for item, count in items.items())
        print(result)

    
def of_personality_type(townies, personality_type):
        # if townie.perso for c in new_catchphrase):

        return [villager.name for villager in townies if villager.personality == personality_type]


def message_received(start_villager, target_villager):
    current = start_villager
    while current.neighbor != None:
        if (current.neighbor == target_villager):
            return True
        current = current.neighbor
    
    return False

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_list(head):
    #while head: print(head.value, end=' -> '); head = head.next
    nodeList = []
    while head:
        nodeList.append(head.value)
        head = head.next
    return " -> ".join(nodeList)

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))




# tom_nook = Node("Tom Nook")
# tommy = Node("Tommy") 
# # tom_nook.next = tommy 
# timmy = Node("Timmy")
# tom_nook.next = None
# timmy.next = tommy
# saharah = Node("Saharah")
# tommy.next = saharah


# print(tom_nook.next) 
# print(timmy.value) 
# print(timmy.next.value)  
# print(tommy.value) 
# print(tommy.next.value)
# print(saharah.value)  
# print(saharah.next) 


# print(tom_nook.value)
# print(tom_nook.next.value)
# print(timmy.value)
# print(timmy.next.value)
# print(tommy.value)
# print(tommy.next)

# print(tom_nook.value) 
# print(tom_nook.next.value) 
# print(tommy.value) 
# print(tommy.next) 


# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider
# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))




# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))




# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()




# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)



# # Instantiate your villager here
# apollo = Villager("Apollo", "Eagle", "pah")
# bones = Villager("Bones", "Dog", "yip yip")


# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 

# bones.catchphrase = "ruff it up"
# print(bones.greet_player("Sahara"))

