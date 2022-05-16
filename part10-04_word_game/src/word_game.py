import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        len1 = len(player1_word)
        len2 = len(player2_word)
        if len1 > len2:
            return 1
        elif len1 < len2:
            return 2


class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    
    def round_winner(self, player1_word, player2_word):
        vowels = "aeiou"
        count1 = []
        count2 = []
        
        for letter in player1_word:
            if letter in vowels:
                count1.append(letter)

        for letter in player2_word:
            if letter in vowels:
                count2.append(letter)
        
        if len(count1) > len(count2):
            return 1
        elif len(count1) < len(count2):
            return 2


class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        rps = ["rock", "paper", "scissors"]
        w1 = player1_word
        w2 = player2_word

        if w1 in rps and w2 not in rps:
            return 1
        elif w1 not in rps and w2 in rps:
            return 2
        elif w1 in rps and w2 in rps:
            if w1 == "rock":
                if w2 == "scissors":
                    return 1
                elif w2 == "paper":
                    return 2
            elif w1 == "paper":
                if w2 == "rock":
                    return 1
                elif w2 == "scissors":
                    return 2
            elif w1 == "scissors":
                if w2 == "paper":
                    return 1
                elif w2 == "rock":
                    return 2

        
        
                