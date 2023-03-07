//https://www.youtube.com/watch?v=HAgLH58IgJQ&ab_channel=NeetCode

class Solution {
public:
    int reverse(int x) {
        int r = 0;
        while(x){
          int digit = x%10;
          x = x/10;
          if(r > INT_MAX/10 || (r == INT_MAX && digit >= INT_MAX/10)) return 0;
          if(r < INT_MIN/10 || (r == INT_MIN && digit <= INT_MIN/10)) return 0;
          r = r*10 + digit;
        }
        return r;
    }
};