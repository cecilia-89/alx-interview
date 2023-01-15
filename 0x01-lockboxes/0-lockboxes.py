#!/usr/bin/python3
def canUnlockAll(boxes):
  unboxed = [] 
  for count, value in enumerate(boxes):
    if count == 0:
      subarray = [boxes[item] for item in value]
      unboxed.append(value)
    else:
      sublist = []
      for array in subarray:
        for item in array:
          sublist.append(boxes[item])
      unboxed.append(sublist)
      subarray = sublist
  return unboxed

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))
