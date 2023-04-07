# https://leetcode.com/problems/boats-to-save-people/solutions/3376312/python-greedy-two-pointer-approach-on-log-n/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat,light,heavy = 0,0,len(people)-1
        while light<=heavy:
            if people[light]+people[heavy]<=limit:
                light+=1
            heavy-=1
            boat+=1
        return boat