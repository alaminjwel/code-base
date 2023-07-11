//https://www.youtube.com/watch?v=I6FA-0vS7Pk
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
      unordered_map<int,int> freq;
      int i = 0, j = 0, maxFruits = 0;

      while(j<fruits.size()){
         freq[fruits[j]]++;

         if(freq.size()>2){
            if(freq[fruits[i]] == 1) freq.erase(fruits[i]);
            else freq[fruits[i]]--;
            i++;
         }
         maxFruits = max(maxFruits, (j-i+1));
         j++;
      }
      return maxFruits;
    }
};