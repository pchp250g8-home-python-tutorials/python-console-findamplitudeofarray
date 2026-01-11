# --coding:utf-8--
import os
import array
import random

os.system("cls")
print("Input a count of elements in array")
nElems = int(input())
print(f"Generating array by filling {nElems} elements:")
iNumbers = array.array('i')
for i in range(0, nElems) :
    nItem = random.randint(1, 100)
    iNumbers.append(nItem)
    print(iNumbers[i], end=" ")
iMax = iNumbers[0]
iMin = iNumbers[0]
nMaxIndex = 0
for i in range(1, nElems) :
    if iNumbers[i] > iMax :
        iMax = iNumbers[i]
        nMaxIndex = i
    if iNumbers[i] < iMin :
        iMin = iNumbers[i]
        nMinIndex = i
print(f"\r\nFound maximum element:{iMax} with index {nMaxIndex}")
print(f"Found minimum element:{iMin} with index {nMinIndex}")
print(f"Found amplitude: {iMax - iMin}")