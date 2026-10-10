owner = input()
b = int(input())
owners = [owner]


for i in range(b):
    winner, loser = input().split()
    if loser == owner:
        owner = winner
        if owner not in owners:
            owners.append(owner)
print(owner)
print(len(owners))
