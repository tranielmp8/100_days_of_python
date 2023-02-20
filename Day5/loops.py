student_heights = input("List of heights: \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
students = 0
for height in student_heights:
  total += height
  students += 1
  print(f"{students} - {total}")
