


def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
                #newlist = []
                #newlist.append(i)
                #newlist.append(j)
                #return newlist
print(twosum([10,30,50,20,5],80))






























