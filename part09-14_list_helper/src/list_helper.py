class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        common = my_list[0]
        max = 0
        for item in my_list:
            if max == 0 or my_list.count(item) > max:
                common = item
                max = my_list.count(item)
        return common
    
    @classmethod
    def doubles(cls, my_list: list):
        count = 0
        unidouble = []
        for item in my_list:
            if my_list.count(item) >= 2 and item not in unidouble:
                count += 1
                unidouble.append(item)

        return count
