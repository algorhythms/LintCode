package FourSum;

import java.util.*;

/**
 * Created by Daniel on 19/06/15.
 */
public class Solution {
    /**
     * @param numbers : Give an array numbersbers of n integer
     * @param target : you need to find four elements that's sum of target
     * @return : Find all unique quadruplets in the array which gives the sum of
     *           zero.
     */
    public ArrayList<ArrayList<Integer>> fourSum(int[] numbers, int target) {
        int n = numbers.length;
        ArrayList<ArrayList<Integer>> ret = new ArrayList<>();
        Set<ArrayList<Integer>> retSet = new LinkedHashSet<>();  // normall HashSet cannot pass the OJ
        Map<Integer, List<List<Integer>>> sum2index = new HashMap<>();
        if(n<4)
            return ret;

        Arrays.sort(numbers);

        for(int i=0; i<n; i++) {
            for(int j=i+1; j<n; j++) {
                int sum = numbers[i]+numbers[j];
                if(!sum2index.containsKey(sum))
                    sum2index.put(sum, new ArrayList<List<Integer>>());
                sum2index.get(sum).add(Arrays.asList(i, j));
            }
        }

        for(int i=0; i<n; i++) {
            for(int j=i+1; j<n; j++) {
                int sumRemain = target-numbers[i]-numbers[j];
                if(sum2index.containsKey(sumRemain)) {
                    for(List<Integer> pair: sum2index.get(sumRemain)) {
                        if(pair.get(0) > j) {
                            retSet.add(new ArrayList<>(Arrays.asList(
                                    numbers[i],
                                    numbers[j],
                                    numbers[pair.get(0)],
                                    numbers[pair.get(1)]
                            )));
                        }
                    }
                }
            }
        }
        for(ArrayList<Integer> elt: retSet) {
            ret.add(elt);
        }
        return ret;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().fourSum(new int[]{1, 0, -1, 0, -2, 2}, 0));
    }
}

