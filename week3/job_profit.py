profits=[int(i) for i in input().split()]
slot=[int(i) for i in input().split()]
d={profits[i]:slot[i] for i in range(len(slot))}
print(d)
final=[]
profit=[]

for i in range(max(slot),0,-1):
    for j in range(len(slot)):
        if i==slot[j]:
            final.append(profits[j])
    # print(final)
    profit.append(max(final))

    final.remove(max(final))
    # print(profit)

print("total: ",profit[::-1])
print("total: ",sum(profit))
