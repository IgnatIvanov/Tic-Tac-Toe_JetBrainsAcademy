import statistics

user_input = input()

user_input = [int(x) for x in user_input]
print(statistics.mean(user_input))