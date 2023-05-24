//https://www.youtube.com/watch?v=Q2Tw6gcVEwc&ab_channel=NeetCode
class Solution {
public:
    string convert(string s, int numRows) {
      if(numRows==1) return s;
      string converted = "";
      int jump = (numRows-1)*2;
      for(int row = 0; row < numRows; row++){
         for(int i=row; i < s.length(); i+=jump){
            converted += s[i];
            int missingCol = i+jump-2*row;
            if((row > 0 && row < numRows-1) && missingCol<s.length())
            converted += s[missingCol];
         }
      }
      return converted;
    }
};