class Solution {
    public int hammingDistance(int x, int y) {
        int result=x^y;
        int count=0;
        for (int i = 31; i >= 0; i--) {
            int bit = (result >> i) & 1;
            if (bit==1)
                count++;
            }
            return count;
}
}