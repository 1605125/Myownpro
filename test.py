from random import shuffle
unsorted_list = ["B", "D", "A", "E", "C"]

def is_sorted(iterable):
  for a1,a2 in zip(iterable, iterable[1:]):
     if a1 > a2: return False
  return True

sorted_list = unsorted_list
while True:
   shuffle(sorted_list)
   if is_sorted(sorted_list): break

print(sorted_list)

lst = ['dabc', 'bcd', 'gg', 'ff', 'cc']
lst.sort()
print(lst)
