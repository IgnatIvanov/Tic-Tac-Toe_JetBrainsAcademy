u_in = input().split(" ")

u_in = [x for x in u_in if x.endswith("s")]
print("_".join(u_in))