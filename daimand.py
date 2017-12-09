user=int(input("inter the roe size:"))
for i in range(row):
    print(''*(rows-i-1)+'* '*(i+1))
for j in range(row-1,0,-1):
    print(''*(rows-j)+'* '*(j))