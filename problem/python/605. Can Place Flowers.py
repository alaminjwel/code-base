class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i,beds = 0,len(flowerbed)
        if n==0:
            return True
        if beds == 1 and flowerbed[0]==1:
            return False
        if beds == 1 and flowerbed[0]==0:
            return True

        canPlace = 0
        while i<beds:
            if flowerbed[i] == 1:
                i += 1
                continue

            success = False

            if i==0 and flowerbed[i+1]==0:
                success = True
            elif i==beds-1 and flowerbed[i-1]==0:
                success = True
            elif flowerbed[i-1]==0 and flowerbed[i+1]==0:
                success = True

            if success:
                canPlace += 1
                flowerbed[i] = 1
                i += 2
            else:
                i += 1

            if canPlace == n:
                break

        return canPlace==n