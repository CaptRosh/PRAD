

points = []
with open('datalof.txt','r') as file:
    lines = file.readlines()

for line in lines:
    points.append((int(line.split(",")[0]),int(line.split(",")[1])))

