#! --*-- coding: utf-8 --*--
__author__ = 'gaoxingsheng'


# class Solution(object):
#     def checkNextChange(self, prices, index):
#         value = prices[index]
#         xindex = -1
#         while index < len(prices):
#             if value < prices[index]:
#                 value = prices[index]
#                 xindex = index
#             index += 1
#
#         return xindex
#
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#
#         index = 0
#         get = 0
#         while index < len(prices):
#             real = self.checkNextChange(prices, index)
#             if real >= 0:
#                 print index, real, prices[real], prices[index]
#                 get += prices[real] - prices[index]
#                 index = real + 1
#             else:
#                 index += 1
#
#         return get
#
# a = Solution()
#
# prs = [1,2,3,4,5]
# prs = [7,1,5,3,6,4]
#
# print(a.maxProfit(prs))

#
all_counts = []

def check_count(prices, count, log):
    for index in xrange(len(prices)):
        value = log[len(log) - 1]
        # 如果有下一天，不管本次可不可以卖出，选择不卖出
        if index + 1 < len(prices):
            check_count(prices[index + 1:], count, log[:])

        if prices[index] > value:  # 今天有差价，选择卖出
            count += prices[index] - value
            log.append(prices[index])  # 记录

            if index + 1 < len(prices):  # 若果有下一天，开始下一次交易
                # print prices, index
                for nindex in xrange(index + 1, len(prices)):
                    new_prices = prices[nindex:]
                    log.append(new_prices[0])
                    check_count(new_prices, count, log[:])


    all_counts.append(count)  # 没有有差值的交易日


prices = [1,2,3,4,5]
prices = [3,2,6,5,0,3]


for index in xrange(len(prices)):
    check_count(prices[index:], 0, [prices[index]])


print(max(all_counts))