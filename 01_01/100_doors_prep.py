# 100 Doors

doors = [False] * 101

# 100 Doors

doors = [False] * 101

print(doors)
# Let's do just one pass
print("First pass:" * 10)
for i in range(1, 101):
    doors[i] = not doors[i]  # Using `not` to invert the Boolean value.
    print("Toggling door", doors[i])

print('second pass:'* 10)
count = 0
for i in range(2, 101, 2):
    doors[i] != doors[i]
    count +=1
    print("Toggling door", doors[i] ,count)
# Time for a nested for loop
print('third pass:'* 10)
for x in range(3, 101, 3):
    doors[i] = not doors[i]
    count +=1
    print("Toggling door", doors[i] ,count)

print('4th pass:'* 10)
for x in range(4, 101, 4):
   doors[i] = not doors[i]
   count +=1
   print("Toggling door", doors[i] ,count)

print('5th pass:'* 10)
for x in range(5, 101, 5):
  doors[i] = not doors[i]
  count +=1
  print("Toggling door", doors[i] ,count)

print('6th pass:'* 10)
for x in range(6, 101, 6):
   doors[i] = not doors[i]
   count +=1
   print("Toggling door", doors[i] ,count)

print('7th pass:'* 10)
for x in range(7, 101, 7):
  doors[i] = not doors[i]
  count +=1
  print("Toggling door", doors[i] ,count)

print('8th pass:'* 10)
for x in range(8, 101, 8):
  doors[i] = not doors[i]
  count +=1
  print("Toggling door", doors[i] ,count)

print('9th pass:'* 10)
for x in range(9, 101, 9):
  doors[i] = not doors[i]
  count +=1
  print("Toggling door", doors[i] ,count)



for  i in    range(5):
    for   j  in  range(3):
                print(i,j)