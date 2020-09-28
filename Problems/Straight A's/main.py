# put your python code here
marks = input()
A = marks.count("A")

print(round(A / len(marks.split(" ")), 2))
