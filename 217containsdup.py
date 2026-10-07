
nums = [1,8,3,2,1,2,]
seenalready = set()

for values in nums:
    if values in seenalready:
        print(True)
        seenalready.add(values)
    print(False)
