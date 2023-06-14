from typing import List
import math
from collections import defaultdict
from collections import deque

class SnapshotArray:

    def __init__(self, length: int):

        self.snaps = []
        self.curr = {}

    def set(self, index: int, val: int) -> None:

        self.curr[index] = val

    def snap(self) -> int:
        
        self.snaps.append(self.curr.copy())
        self.curr = {}
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            if index in self.snaps[i]:
                return self.snaps[i][index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
inp = [[3],[0,5],[],[0,6],[0,0]]
obj = SnapshotArray(inp[0][0])
arr={}
arr[0]=None
arr[1]=obj.set(inp[1][0],inp[1][1])
arr[2]=obj.snap()
arr[3]=obj.set(inp[3][0],inp[3][1])
arr[4]=obj.get(inp[4][0],inp[4][1])
print(arr)