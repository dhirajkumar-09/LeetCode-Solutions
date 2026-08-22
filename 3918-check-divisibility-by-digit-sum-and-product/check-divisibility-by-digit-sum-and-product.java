class Solution {
    public boolean checkDivisibility(int n) {
        String str=Integer.toString(n);
        int sum=0;
        int product=1;
        for(int i=0; i<str.length(); i++){
            int digit = Integer.parseInt(String.valueOf(str.charAt(i)));

            sum+=digit;
            product*=digit;
        }
        return n%(sum+product)==0;
    }
}