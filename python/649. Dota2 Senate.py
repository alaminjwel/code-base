# https://leetcode.com/problems/dota2-senate/editorial/
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        r_count = senate.count('R')
        d_count = len(senate)-r_count

        def ban(to_ban, start_at):
            loop_around = False
            pointer = start_at

            while True:
                if pointer == 0:
                    loop_around = True
                if senate[pointer] == to_ban:
                    senate.pop(pointer)
                    break
                pointer = (pointer + 1) % len(senate)

            return loop_around
        turn=0
        while r_count>0 and d_count>0:
            if senate[turn]=='R':
                banned = ban('D',(turn+1)%len(senate))
                d_count-=1
            else:
                banned = ban('R',(turn+1)%len(senate))
                r_count-=1
            if banned:
                turn-=1
            turn = (turn+1)%len(senate)
        return 'Radiant' if d_count == 0 else 'Dire'

