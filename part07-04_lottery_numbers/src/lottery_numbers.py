def lottery_numbers(amount: int, lower: int, upper: int):
    from random import sample

    nums =  list(range(lower, upper+1))
    select = sample(nums, amount)
    select.sort()
    return select

# for number in lottery_numbers(2, 1, 10):
#     print(number)