import java.math.BigInteger;
import java.util.*;

class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {

        String str = "";

        for (int i : num) {
            str += i;
        }

        BigInteger result = new BigInteger(str);
        result = result.add(BigInteger.valueOf(k));

        String ans = String.valueOf(result);

        List<Integer> list = new ArrayList<>();

        for (char c : ans.toCharArray()) {
            list.add(c - '0');
        }

        return list;
    }
}