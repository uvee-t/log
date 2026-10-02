total_lines = 0
log_type_cnt = {"DATA": 0, "WARNING": 0, "INFO": 0, "ERROR": 0, "DEBUG": 0, "ENTRY": 0}
with open("./data/server.log", "r") as log:
    for line in log:
        total_lines += 1
        log_array = line.split()
        if len(log_array) < 3:
            continue
        date, time, level, *msg = log_array
        if level in log_type_cnt:
            log_type_cnt[level] += 1
print(log_type_cnt)
print(f"\n{total_lines}")
