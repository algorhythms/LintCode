package CountofSmallerNumberbeforeitself;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by Daniel on 16/06/15.
 */
public class Solution {
    class Node {
        int val, count, countLeft;
        Node left, right;
        Node(int val) {
            this.val = val;
        }
    }

    class BST {
        Node root;

        void insert(Node root, int val) {
            if(this.root == null) {
                this.root = new Node(val);
                root = this.root;
            }
            assert root != null;

            if(root.val == val)
                root.count += 1;
            else if(val < root.val) {
                root.countLeft += 1;
                if(root.left == null) root.left = new Node(val);
                this.insert(root.left, val);
            }
            else {
                if(root.right == null) root.right = new Node(val);
                this.insert(root.right, val);
            }
        }

        int query(Node root, int val) {
            if(root == null)
                return 0;
            if(root.val < val)
                return root.count+root.countLeft+this.query(root.right, val);
            else if(root.val == val)
                return root.countLeft;
            else
                return this.query(root.left, val);
        }
    }
    /**
     * @param A: An integer array
     * @return: Count the number of element before this element 'ai' is
     *          smaller than it and return count number array
     */
    public ArrayList<Integer> countOfSmallerNumberII(int[] A) {
        ArrayList<Integer> ret = new ArrayList<Integer>();
        BST tree = new BST();
        for(int a: A) {
            tree.insert(tree.root, a);
            ret.add(tree.query(tree.root, a));
        }
        return ret;
    }

    public static void main(String[] args) {
        List<Integer> expected = Arrays.asList(0, 1, 2, 3, 2);
        assert new Solution().countOfSmallerNumberII(new int[] {1, 2, 7, 8, 5}).equals(expected);
    }
}

