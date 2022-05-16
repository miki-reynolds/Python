class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.nums = []
        self.nums.append(self.numbers)
        
    def add_number(self, number:int):
        self.nums.append(number)
        
      
    def count_numbers(self):
        # self.count_numbers = len(self.nums) - 1
        return (len(self.nums) - 1)
        
    
    def get_sum(self):
        # self.get_sum = sum(self.nums)
        return sum(self.nums)

    def average(self):
        try:
            self.average = sum(self.nums)/(len(self.nums) - 1)
            return self.average
        except:
            ZeroDivisionError

print("Please type in integer numbers:")

nums = NumberStats()
even = NumberStats()
odd = NumberStats()

while True:
    num = int(input())
    if num == -1:
        break
    elif num % 2 == 0:
        even.add_number(num)
    elif num % 2 != 0:
        odd.add_number(num)
    nums.add_number(num)
    
    
print("Sum of numbers:", nums.get_sum())
print("Mean of numbers:", nums.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())
