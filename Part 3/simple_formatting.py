w = "123"
l = 5

space = " "
count = 0
for s in w:
    count += 1
count = l - count
ans = (space * count) + w
print (ans)