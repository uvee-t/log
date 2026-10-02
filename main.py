total_lines = 0
with open("./data/server.log", "r") as log:
    for line in log:
        total_lines += 1
        print(line, end="")
print(f"\n{total_lines}")
