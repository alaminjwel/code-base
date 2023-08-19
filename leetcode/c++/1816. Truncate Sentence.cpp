class Solution {
public:
   string truncateSentence(string s, int k) {
   string makeString = "";
   string truncated = "";
   s = s + " ";
   for(int i=0;i<s.length();i++){
      if(s[i]==' ') {
         truncated = truncated + makeString;
         makeString = "";
         k--;
         if(k==0) break;
         truncated += " ";
      }
      else makeString += s[i];
   }
   return truncated;
   }
};
