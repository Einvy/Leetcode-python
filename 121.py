


prices = [1,5,8,2,3,10]



# result = 0
#
# for i in range(len(prices)):
#     for j in range(i + 1, len(prices)):
#         result = max(result, prices[i] - prices[j])
# print(result)
#
#
left = 0
right = 1
mprofit = 0
while right < len(prices):
    if prices[left] < prices[right]:
        profit = prices[right] - prices[left]
        mprofit = max(mprofit, profit)
    else:
     left = right
    right +=1
print(mprofit)







