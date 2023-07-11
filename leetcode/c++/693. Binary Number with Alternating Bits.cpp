class Solution {
public:
    bool hasAlternatingBits(int n) {
        int i = 0;
        int prevDigit = -1;
        int curDigit;
        while (n > 0) {    
            curDigit = n % 2;
            if(curDigit==prevDigit) return false;
            prevDigit = curDigit;
            n = n / 2;
            i++;
        }
        return true;
        
    }
};