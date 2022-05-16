class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def tick(self):    
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        
        if self.hours == 24:
            self.hours = 0
        
        return self.seconds, self.minutes, self.hours
    
    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0
        return self.hours, self.minutes, self.seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
            

# clock = Clock(23, 59, 55)

# clock.set(12, 30)
# print(clock)
