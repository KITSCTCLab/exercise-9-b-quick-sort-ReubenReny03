from typing import List

def quick_sort(data, low, high) -> List[int]:
    if low < high:
        i = low
        j = high-1
        pivot = data[high]
        
        while i < j:
            while i< high and data[i] < pivot:
                i+=1
            while j<low and data[j] > pivot:
                j-=1
            if i < j:
                data[i], data[j] = data[j], data[i]
                
        if data[i] > pivot:
            data[i], data[high] = data[high], data[i]
        partision_pos = i
        quick_sort(data,low,partision_pos-1)
        quick_sort(data,partision_pos+1,high)

input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))
