class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        unordered_map<char,char> alphabet;
        for(int i=0;i<26;i++){
            alphabet[order[i]] = 'a'+i;
        }
        for(int i=0;i<words.size();i++){
            for(int j=0;j<words[i].size();j++){
               words[i][j] = alphabet[words[i][j]];
            }
        }
        return is_sorted(words.begin(),words.end());
    }
};