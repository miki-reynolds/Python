def dict_of_numbers():
    list = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
               9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 15: 'fifteen', 18: 'eighteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
               50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    for i in range(100):
        if i not in list:
            if i < 20:
                list[i] = list[i-10] + 'teen'
            if 20 < i < 100 and i % 10 != 0:
                list[i] = list[i - (i%10)] + '-' + list[i%10]
    return list