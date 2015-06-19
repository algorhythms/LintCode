package BuildingOutline;

import java.util.*;

/**
 * Created by Daniel on 17/06/15.
 */
public class Solution {
    class Building implements Comparable<Building>{
        int h;
        boolean deleted;
        Building(int h) {
            this.h = h;
            this.deleted = false;
        }


        public int compareTo(Building o) {
            return o.h - this.h;
        }
    }

    class Event {
        List<Building> starts;
        List<Building> ends;

        Event() {
            this.starts = new ArrayList<>();
            this.ends = new ArrayList<>();
        }
    }
    /**
     * @param buildings: A list of lists of integers
     * @return: Find the outline of those buildings
     */
    public ArrayList<ArrayList<Integer>> buildingOutline(int[][] buildings) {
        SortedMap<Integer, Event> events = new TreeMap<>();
        for(int[] b: buildings) {
            Building building = new Building(b[2]);
            if(!events.containsKey(b[0])) events.put(b[0], new Event());
            events.get(b[0]).starts.add(building);
            if(!events.containsKey(b[1])) events.put(b[1], new Event());
            events.get(b[1]).ends.add(building);
        }

        ArrayList<ArrayList<Integer>> ret = new ArrayList<>();
        PriorityQueue<Building> curHeap = new PriorityQueue<>();
        int curMaxHi = 0;
        int begin = 0;
        for(Map.Entry<Integer, Event> e: events.entrySet()) {
            for(Building building: e.getValue().starts)
                curHeap.add(building);
            for(Building building: e.getValue().ends)
                building.deleted = true;

            while(curHeap.size() > 0 && curHeap.peek().deleted)
                curHeap.remove();

            int newHi = 0;
            if(curHeap.size() > 0)
                newHi = curHeap.peek().h;
            if(newHi != curMaxHi) {
                if(curMaxHi != 0) {
                    ArrayList<Integer> r = new ArrayList<>();
                    r.add(begin); r.add(e.getKey()); r.add(curMaxHi);
                    ret.add(r);
                }
                begin = e.getKey();
                curMaxHi = newHi;
            }
        }
        return ret;
    }
    public static void main(String[] args) {
        int[][] buildings = new int[][] {
                {1, 3, 3},
                {2, 4, 4},
                {5, 6, 1}
        };
        List<List<Integer>> expected = new ArrayList<>();
        expected.add(Arrays.asList(1, 2, 3));
        expected.add(Arrays.asList(2, 4, 4));
        expected.add(Arrays.asList(5, 6, 1));
        assert new Solution().buildingOutline(buildings).equals(expected);
    }
}

