print("Welcome to the Love Calculator!")

name1 = input("what is your name? \n")
name2 = input("what is your loves name? \n")
count1 = 0
count2 = 0

if "t" in name1.lower():
   t = name1.count("t")
   count1 += t
if "r" in name1.lower():
   r = name1.count("r")
   count1 += r
if "u" in name1.lower():
   u = name1.count("u")
   count1 += u
if "e" in name1.lower():
   e = name1.count("e")
   count1 += e
if "l" in name1.lower():
   l = name1.count("l")
   count1 += l
if "o" in name1.lower():
   o = name1.count("o")
   count1 += o
if "v" in name1.lower():
   v = name1.count("v")
   count1 += v
if "e" in name1.lower():
   e = name1.count("e")
   count1 += e
   
   
if "t" in name2.lower():
   t = name2.count("t")
   count2 += t
if "r" in name2.lower():
   r = name2.count("r")
   count2 += r
if "u" in name2.lower():
   u = name2.count("u")
   count2 += u
if "e" in name2.lower():
   e = name2.count("e")
   count2 += e
if "l" in name2.lower():
   l = name2.count("l")
   count2 += l
if "o" in name2.lower():
   o = name2.count("o")
   count2 += o
if "v" in name2.lower():
   v = name2.count("v")
   count2 += v
if "e" in name2.lower():
   e = name2.count("e")
   count2 += e

print(str(count1), str(count2))



