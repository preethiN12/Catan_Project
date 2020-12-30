import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;
import java.util.*;
//import static java.util.Map.entry;

public class Player {
    private int numRoads = 0;
    private int numSettlements = 0;
    private int numCities = 0;
    private int numArmy = 0;
    private int points = 0;
    private int bank_ratio = 0;
    private HashMap<String, Integer> dev_cards = new HashMap<String, Integer>();
    private HashMap<String, Integer> resources = new HashMap<String, Integer>();
    private ArrayList<int[]> roadList = new ArrayList<>();
    private ArrayList<Integer> settlementList = new ArrayList<>();
    private ArrayList<Integer> cityList = new ArrayList<>();
    private HashMap<String, ArrayList> placements = new HashMap<String, ArrayList>();
    private boolean largest_army = false;
    private boolean longest_road = false;

    public Player() {
        this.numRoads = 2;
        this.numSettlements = 2;
        this.numCities = 0;
        this.numArmy = 0;
        this.points = 0;
        this.bank_ratio = 4;
        {
            {
                dev_cards.put("v", 0);
                dev_cards.put("k", 0);
                dev_cards.put("m", 0);
                dev_cards.put("r", 0);
                dev_cards.put("y", 0);
            }
        }
        ;
        {
            {
                resources.put("lumber", 0);
                resources.put("wool", 0);
                resources.put("brick", 0);
                resources.put("grain", 0);
                resources.put("ore", 0);
            }
        }
        {
            {
                placements.put("road", roadList);
                placements.put("settlement", settlementList);
                placements.put("city", cityList);
            }
        }
    }

    public int victoryPoints(String card) {
        points = numSettlements + 2 * numCities;

        //can reveal all victory points at once
        if (card.equals("v")) {
            points++;
        }
        if (largest_army == true) {
            //first player to get 3 knight cards can claim
            //can change later in the game
            points += 2;
        }
        if (longest_road == false) {
            //first player to get 5 continuous roads can claim
            //can change later
            points += 2;
        }
        return points;
    }
    public void addRoadPlacement(int p1, int p2) {
        int[] newRoadPos = {p1, p2};
        //prints memory reference instead of int[]
        roadList.add(newRoadPos);
        //check if we need to add to longest road -> what its connected to
    }
    //getter/setter for longest-road and largest-army

    public void AddSettlementPlacement(int p1){
        settlementList.add(p1);
        //cant have 2 houses right next to each other need a buffer point -->need to happen in game class
    }

    public void AddCityPlacement(int p1){
        settlementList.remove(p1);
        cityList.add(p1);
    }

    //public void

    //def compare_roads(self, person2, person3, person4=null): -->game class

    public void trade_player(Player person2, String giveAway, String want) {
        if (this.resources.get(giveAway) > 0 && person2.resources.get(want) > 0) {
            int newNumP1A = this.resources.get(want) +1;
            this.setResources(want, newNumP1A);
            int newNumP1B = this.resources.get(giveAway) -1;
            this.setResources(giveAway, newNumP1B);

            int newNumP2A = person2.resources.get(want) -1;
            person2.setResources(want, newNumP2A);
            int newNumP2B = person2.resources.get(giveAway) +1;
            person2.setResources(giveAway, newNumP2B);

        }
    }

    /*
    def trade_bank(self, resource_need, resource_give_away) {
        ratio = 4
        if self.special_harbour[resource_give_away]:
        ratio = 2

        if self.resources[resource_give_away] >= ratio:
        self.resources[resource_give_away] -= ratio
        self.resources[resource_need] += 1

            //def improve_ratio (self):
            //know where special habours are in order to figure this out
        //generic ratio, special habour ratio
    }*/

    //improved ratio 3:1 near a harbour/water

    //set resource??
    /*
    def change_resource(self, key, value){
        self.resources[key]=value
    }*/

    
    //getter methods
    public int getNumRoads() {
        return numRoads;
    }
    public int getNumSettlements() {
        return numSettlements;
    }

    public int getNumCities() {
        return numCities;
    }

    public HashMap<String, Integer> getDev_cards() {
        return dev_cards;
    }
    public HashMap<String, Integer> getResources() {
        return resources;
    }

    public boolean isLargest_army() { return largest_army; }
    public boolean isLongest_road() { return longest_road; }

    //setter methods
    public void setNumRoads(int newRoads) {
        this.numRoads += newRoads;
        //call function that adds road placements
    }
    public void setNumSettlements(int newSettlements) {
        this.numSettlements += newSettlements;
        //call function that adds settlement placements
    }
    public void setNumCities(int newCities) {
        this.numCities += newCities;
        //call function that adds city placements
    }
    public void setDev_cards(String key, int newNum) {
        //maybe change later to add/subtract 1 so user doesnt need to know current number of specific card
        //can only use or gain 1 card per turn, except for victory point cards (can use them all in 1 turn)
        //might have to wait a turn before using a new dev card
        dev_cards.replace(key, newNum);
        //this.dev_cards=dev_cards;
    }
    public void setResources(String key, Integer newNum) {
        resources.replace(key, newNum);
        //this.resources = resources;
    }

    public void setLargest_army(boolean largest_army) { this.largest_army = largest_army; }
    public void setLongest_road(boolean longest_road) { this.longest_road = longest_road; }

    public String toString() {
        return "Player{" +
                "numRoads=" + numRoads +
                ", numSettlements=" + numSettlements +
                ", numCities=" + numCities +
                ", numArmy=" + numArmy +
                ", points=" + points +
                ", bank_ratio=" + bank_ratio +
                ", dev_cards=" + dev_cards +
                ", resources=" + resources +
                ", placements=" + placements +
                ", largest_army=" + largest_army +
                ", longest_road=" + longest_road +
                '}';
    }
}
