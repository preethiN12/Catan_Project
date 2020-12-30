playerList = []
class Person:
    id = 0
    numRoads = 0
    numSettlements=0
    numCities=0
    numArmy=0
    points=0
    bank_ratio=0
    dev_cards = {}
    resources = {}
    placements = {}
    largest_army = False
    longest_road=False
    special_harbour =  {}
    def __init__(self, id, playerList):
        #id+=1 #hwo to generate unique id without user entering it
        self.id=id
        self.numRoads = 2
        self.numSettlements=2
        self.numCities=0
        self.bank_ratio=4
        self.resources = {"lumber":0, "brick":0, "grain":0, "ore":0, "wool":0}
        self.placements = {"road": [], "settlement": [], "city": []}
        self.special_harbour =  {"lumber":False, "brick":False, "grain":False, "ore":False, "wool":False}
        self.dev_cards = {"v":0, "k":0, "m":0, "r":0, "y":0}
        self.largest_army = False
        self.numArmy=0
        self.longest_road=False
        playerList.append(id)

    def change_numRoads(self, newNumRoads):
        self.numRoads=newNumRoads

    def change_numSettlements(self, newNumSettlements):
        self.numSettlements=newNumSettlements

    def change_numCities(self, newNumCities):
        self.numCities=newNumCities

    def change_dev_card(self, type, newNum):
        self.dev_cards[type[0]]=newNum

    #def compare_roads(self, person2, person3, person4=null):

    def trade_player(self, person2, resource1, resource2):
        if self.resources[resource1]>0 and person2.resources[resource2]>0:
            self.resources[resource2]+=1
            self.resources[resource1]-=1
            person2.resources[resource2]-=1
            person2.resources[resource1]+=1

    def trade_bank(self, resource_need, resource_give_away):
        ratio=4
        if self.special_harbour[resource_give_away]:
            ratio=2

        if self.resources[resource_give_away]>=ratio:
            self.resources[resource_give_away]-=ratio
            self.resources[resource_need]+=1

    #def improve_ratio(self):
        #know where special habours are in order to figure this out
        #generic ratio, special habour ratio

    def change_resource(self, key, value):
        self.resources[key]=value

    def description(self):
        print("person has id %s, %s roads, %s settlements, %s cities" % (self.id, self.numRoads, self.numSettlements, self.numCities))

    def victoryPoints(self, card=""):
        self.points = self.numSettlements + 2*self.numCities
        #include development cards, etc.
        #largest army, largest roads

        #can reveal all victory points at once
        if card[0]=="v":
            self.points+=1
        return self.points

    def roadPlacement(self, hexagonNum, edge):
        #road always in dict
        self.placements["road"].append([hexagonNum,edge])

    def settlementPlacement(self, hexagonNum, vertice):
        #settlment always in dict
        self.placements["settlement"].append([hexagonNum,vertice])
        #cant have 2houses right next to each other need a buffer point

    def cityPlacement(self, hexagonNum, vertice):
        #city always in dict because defined
        self.placements["settlement"].remove([hexagonNum,vertice])
        self.placements["city"].append([hexagonNum,vertice])

person1 = Person(1, playerList)
person2 = Person(2, playerList)
#person1.resources{"forest":4}
#person1.cityPlacement(1,3)
person1.description()
person2.description()
#person1.trade_player(person2, "forest", "hills")
person1.change_resource("lumber", 4)
person2.change_resource("brick", 1)
#print(person2.resources)
person1.change_dev_card("knight", 3)
print(person1.dev_cards)
#print(person2.resources)
#print(playerList)
#print(person1.victoryPoints(curr_dev_card))
