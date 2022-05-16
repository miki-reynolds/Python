class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        difference = self.balance - amount
        if difference >= 0:
            self.balance -= amount
            return True
        else:
            return False

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        if payment >= 2.5:
            payment = payment - 2.5
            self.funds += 2.5
            self.lunches += 1
        return payment
       
    def eat_special(self, payment: float):
        if payment >= 4.3:
            payment = payment - 4.3
            self.funds += 4.3
            self.specials += 1
        return payment
        
    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(2.5):
            self.lunches += 1
            return True
        else:
            return False
        
    def eat_special_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(4.3):
            self.specials += 1
            return True
        else:
            return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount

