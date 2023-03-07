class Solution {
public:
    bool checkInclusion(string s1, string s2) {
      int l1 = s1.length();
      int l2 = s2.length();
      if (l1 > l2) return false;
        
      vector<int> mapS1(26,0);
      for(auto ch:s1){
         mapS1[ch-'a']++;
      }
      for(int i=0; i < l2-l1+1; i++){
         vector<int> mapS2(26,0);
         for(int j=i; j < i+l1; j++){
             mapS2[s2[j]-'a']++;
         }
         if(mapS1 == mapS2) return true;
      }
      return false;

    }
};