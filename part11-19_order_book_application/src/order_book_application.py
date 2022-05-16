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
        try:
            if description not in self.__orders:
                self.__orders.append(Task(description, programmer, int(workload)))

        except:
            return f"erroneous input"
    
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
        result = []
        for order in self.__orders:
            if order.is_finished:
                result.append(order)
        return result
        # return [order for order in self.__orders if order.is_finished() == True]

    def unfinished_orders(self):
        return [order for order in self.__orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer):
        names = []
        for order in self.__orders:
            names.append(order.programmer)

        if programmer not in names:
            return False
        
        fin = [order for order in self.__orders if order.is_finished() and order.programmer == programmer]
        unfin = [order for order in self.__orders if not order.is_finished() and order.programmer == programmer]

        sum1, sum2 = 0, 0
        for order in fin:
            sum1 += order.workload
        for order in unfin:
            sum2 += order.workload

        return (len(fin), len(unfin), sum1, sum2)


class OrderBookApplication:
    def __init__(self):
        self.__app = OrderBook()
    
    def help(self):
        print("commands:\n0 exit\n1 add order\n2 list finished tasks\n3 list unfinished tasks\n4 mark task as finished\n5 programmers\n6 status of programmer")
    
    def add_order(self):
        description = input("description: ")
        programwork = input("programmer and workload estimate: ")
        
        if not " " in programwork:
            print("erroneous input")

        else:
            programwork = programwork.split()
            try: 
                if len(programwork) == 2 and len(programwork[0]) != 0 and len(programwork[1]) != 0:
                    self.__app.add_order(description, programwork[0], int(programwork[1]))
                    print("added!")

            except:
                print("erroneous input")

    def finished_orders(self):
        fin = self.__app.finished_orders()
        if len(fin) != 0:
            for order in fin:
                print(order)

        else:
            print("no finished tasks")

    def unfinished_orders(self):
        unfin = self.__app.unfinished_orders()
        if len(unfin) == 0:
            print("no unfinished tasks")
        else:
            for order in unfin:
                print(order)

    def mark_finished(self):
        id = int(input("id: "))
        self.__app.mark_finished(id)
        print("marked as finished")
    
    def programmers(self):
        for name in self.__app.programmers():
            print(name)

    def status_of_programmer(self):
        pro = input("programmer: ")
        status = self.__app.status_of_programmer(pro)
        if status == False:
            print("erroneous input")
        else:
            print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")

    def execute(self):
        self.help()
        while True:
            cmd = input("command: ")
            if cmd == "0":
                break
            elif cmd == "1":
                self.add_order()
            elif cmd == "2":
                self.finished_orders
            elif cmd == "3":
                self.unfinished_orders()
            elif cmd == "4":
                self.mark_finished()
            elif cmd == "5":
                self.programmers()
            elif cmd == "6":
                self.status_of_programmer()
            else:
                self.help()


r = OrderBookApplication()
r.execute()