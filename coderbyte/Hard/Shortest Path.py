# Shortest Path
# Have the function ShortestPath(strArr) take strArr which will be an array of strings which models a non-looping Graph. The structure of the array will be as follows: The first element in the array will be the number of nodes N (points) in the array as a string. The next N elements will be the nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.). Then after the Nth element, the rest of the elements in the array will be the connections between all of the nodes. They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.). Although, there may exist no connections at all.

# An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. Your program should return the shortest path from the first Node to the last Node in the array separated by dashes. So in the example above the output should be A-B-D. Here is another example with strArr being ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]. The output for this array should be A-E-D-F-G. There will only ever be one shortest path for the array. If no path between the first and last node exists, return -1. The array will at minimum have two nodes. Also, the connection A-B for example, means that A can get to B and B can get to A.
# Examples
# Input: ["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]
# Output: A-C-D-F
# Input: ["4","X","Y","Z","W","X-Y","Y-Z","X-W"]
# Output: X-W


from collections import defaultdict
from collections import deque 
def ShortestPath(strArr):
  n = int(strArr[0])
  nodes = strArr[1:n+1]
  connections = strArr[n+1:]
  edges = defaultdict(list)
  for e in connections:
    s,d = e.split('-')
    edges[s].append(d)
    edges[d].append(s)

  queue=deque([(nodes[0],[nodes[0]])])
  shortestPath=[]
  while queue:
    node,path = queue.popleft()    
    if node == nodes[-1]:
      shortestPath = path
      break

    for neighbor in edges[node]:
      if neighbor not in path:
        queue.append((neighbor, path + [neighbor]))
        
  if len(shortestPath)==0:
    return -1
  return "-".join(shortestPath)

  

print(ShortestPath(input()))