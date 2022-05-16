class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name, pw):
        super().__init__(name)
        self._pw = pw
    
    def add_ingredient(self, ingredient: str, amount: float, pw):
        if pw == self._pw:
            return super().add_ingredient(ingredient, amount)
        else:
            raise ValueError("Wrong password!")
    
    def print_recipe(self, pw):
        if pw == self._pw:
            return super().print_recipe()
        else:
            raise ValueError("Wrong password!")



