import java.util.*;
class Solution {
    public int missingNumber(int[] nums) {
    int sum1=0;
    for(int i=0; i<=nums.length; i++){
        sum1+=i; 
    }
    int sum2=0;
    for(int x: nums){
        sum2+=x;
    }
    return sum1-sum2;
}
}