# combine even numbers from 0, 100 and print it out after they have been combined

even_total = 0
for evens in range(0, 101, 2):
  even_total += evens
  
print(even_total)

