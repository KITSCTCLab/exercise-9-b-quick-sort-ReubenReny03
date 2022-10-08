from typing import List

def sorting(data, low ,high):
    i=0
    pivot = data[-1]
    for j in range(high-1):
        if data[j] <= pivot:
            i+=1
            data[j], data[i] =  data[i], data[j]
    data[i+1], pivot = pivot,data[i+1]
    return i+1
    

def quick_sort(data, low, high) -> List[int]:
    if low<high:
        pi = sorting(data,low,high)
        quick_sort(data,low,pi-1)
        quick_sort(data,pi+1,low)
        
        
    

input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))
