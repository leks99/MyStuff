print("liczba n: ")
n = int(input())
print("wprowadz plan")
plan = []
planc = plan
for i in range(n):
    plan.append(int(input()))
for i in range(len(plan)):
    if plan[0] == 0:
        plan.pop(0)
    if len(plan) == 0:
        break
    if plan[-1] == 0:
        plan.pop(-1)
toPop = []
for i in range(len(plan)):
    if i >= 1:
        if plan[i] == 0 and plan[i-1] == 0:
            if i-1 not in toPop:
                toPop.append(i-1)
            if i not in toPop:
                toPop.append(i)
toPop.sort(reverse=True)
for p in toPop:
    plan.pop(p)
print(len(plan))