class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def search(spell):
            low,high = 0,len(potions)-1
            while low<=high:
                mid = (low+high)//2
                product = potions[mid]*spells[spell]                
                if product<success:
                    low = mid+1
                else:
                    high = mid-1
            return len(potions) - low

        output = []
        for spell in range(len(spells)):
            output.append(search(spell))
        return output