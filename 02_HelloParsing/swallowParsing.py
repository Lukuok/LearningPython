f = open('data/report_swallow.txt', 'rt')
line = f.readline()
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()