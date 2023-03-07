class Solution {
public:
    bool isAnagram(string s, string t) {
        if(t.length() > s.length()) return false;

        vector<int> s1(26,0),s2(26,0);

        for(auto ch : s) s1[ch - 'a']++;
        for(auto ch : t) s2[ch - 'a']++;

        return s1==s2;

    }
};