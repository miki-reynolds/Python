class Task:
    id = 0
    def __init__(self, description, programmer, workload):
        self.__description = description
        self.__programmer = programmer
        self.__workload = workload
        self.__is_finished = False
        Task.id += 1
        self.id = Task.id

    @property
    def description(self):
        return self.__description
    @property
    def programmer(self):
        return self.__programmer
    @property
    def workload(self):
        return self.__workload
    
    def mark_finished(self):
        self.__is_finished = True
        return self.__is_finished

    def is_finished(self):
        return self.__is_finished

    def __repr__(self):
        if self.is_finished():
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        else:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"


class OrderBook:
    def __init__(self):
        self.__orders = []
    
    def add_order(self, description, programmer, workload):
        if description not in self.__orders:
            self.__orders.append(Task(description, programmer, workload))
    
    def programmers(self):
        result = []
        if len(self.__orders) != 0:
            for order in self.__orders:
                if order.programmer not in result:
                    result.append(order.programmer)
        return result
    
    def all_orders(self):
        return self.__orders

    def mark_finished(self, id):
        if int(id) <= len(self.__orders):
            for order in self.__orders:
                if order.id == int(id):
                    order.mark_finished()
        else:
            raise ValueError("id nonexistenct")


    def finished_orders(self):
        return [order for order in self.__orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.__orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer):
        try:
            fin = [order for order in self.__orders if order.is_finished() and order.programmer == programmer]
            unfin = [order for order in self.__orders if not order.is_finished() and order.programmer == programmer]
            sum1, sum2 = 0, 0

            for order in fin:
                sum1 += order.workload

            for order in unfin:
                sum2 += order.workload

            return (len(fin), len(unfin), sum1, sum2)
            
        except:
            print("erroneous input")

# t = OrderBook()
# t.add_order("program web store", "Andy", 10)
# t.add_order("program mobile gane", "Eric", 5)
# t.add_order("code better facebook", "Jonas", 5000)
# t.mark_finished(1)
# t.mark_finished(22)
# print(t.finished_orders())

# # print(t.unfinished_orders())
