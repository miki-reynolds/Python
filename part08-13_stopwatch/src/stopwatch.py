from datetime import*
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):    
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 00
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 00

        return self.seconds, self.minutes

    def __str__(self):
        if self.minutes < 10 and self.seconds < 10:
            return f"0{self.minutes}:0{self.seconds}"
        
        elif self.minutes < 10 and self.seconds > 10:
            return f"0{self.minutes}:{self.seconds}"
        
        else:
            return f"{self.minutes}:{self.seconds}"
            

# watch = Stopwatch()
# for i in range(62):
#     print(watch)
#     watch.tick()     
        
