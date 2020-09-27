n = int(input())
matches = list()
for _ in range(0, n):
    matches.append(input())

answer = [x.split(" ") for x in matches if x.endswith('win')]
print([x[0] for x in answer])
print(len(answer))