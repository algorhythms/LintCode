package ContinuousSubarraySumII;

import java.util.ArrayList;

/**
 * Created by Daniel on 19/06/15.
 */
public class Solution {
    class Sum {
        int sum;
        int i;
        int j;
        Sum(int sum, int i, int j) {
            this.sum = sum;
            this.i = i;
            this.j = j;
        }
    }

    /**
     * @param A an integer array
     * @return  A list of integers includes the index of the first number and the index of the last number
     */
    public ArrayList<Integer> continuousSubarraySumII(int[] A) {
        Sum linearSum = this.linearMaxSum(A);
        Sum circularSum = this.circularMaxSum(A);
        ArrayList<Integer> r = new ArrayList<>();
        if(linearSum.sum>circularSum.sum) {
            r.add(linearSum.i); r.add(linearSum.j);
        }
        else {
            r.add(circularSum.i); r.add(circularSum.j);
        }
        return r;
    }

    Sum linearMaxSum(int[] A) {
        Sum ret = new Sum(A[0], 0, 0);
        int curMax = 0;
        int b = 0;
        for(int i=0; i<A.length; i++) {
            curMax += A[i];
            if(curMax > ret.sum) {
                ret.sum = curMax;
                ret.i = b; ret.j = i;
            }
            if(curMax < 0) {
                b = i+1;
                curMax = 0;
            }
        }
        return ret;
    }

    Sum circularMaxSum(int[] A) {
        Sum[] fromRight = new Sum[A.length];
        Sum[] fromLeft = new Sum[A.length];
        Sum ret = new Sum(A[0], 0, 0);
        int curMax = 0;
        for(int i=0; i<A.length; i++) {
            curMax += A[i];
            if(curMax > ret.sum) {
                ret = new Sum(curMax, 0, i);
            }
            fromLeft[i] = ret;
        }
        ret = new Sum(A[A.length-1], A.length-1, A.length-1);
        curMax = 0;
        for(int i=A.length-1; i>-1; i--) {
            curMax += A[i];
            if(curMax > ret.sum) {
                ret = new Sum(curMax, i, A.length-1);
            }
            fromRight[i] = ret;
        }
        ret = new Sum(A[0], 0, 0);
        for(int i=1; i<A.length; i++) {
            Sum right = fromRight[i];
            Sum left = fromLeft[i-1];
            if(right.sum+left.sum>ret.sum) {
                ret.sum = right.sum+left.sum;
                ret.i = right.i;
                ret.j = left.j;
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        ArrayList<Integer> expected = new ArrayList<>();
        expected.add(4); expected.add(1);
        assert new Solution().continuousSubarraySumII(new int[]{3, 1, -100, -3, 4}).equals(expected);
    }
}
