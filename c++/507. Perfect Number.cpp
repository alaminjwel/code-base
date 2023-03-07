class Solution {
public:
    bool checkPerfectNumber(int num) {
        if(num < 2) return false;
        int sum = 1;
        for(int i=2;i<=floor(num/2);i++){
            if(num%i==0) sum+=i;
        }
        return sum==num;
    }
};