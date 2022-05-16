class LotteryNumbers:
    def __init__(self, week , nums):
        self._w = week
        self.__nums = nums

    def number_of_hits(self, nums):
        return len([n for n in nums if n in self.__nums])

    def hits_in_place(self, nums):
        return [nums[n] if nums[n] == self.__nums[n] else -1 for n in range(7)]

# week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
# my_numbers = [1,4,7,10,11,20,30]

# print(week8.hits_in_place(my_numbers))