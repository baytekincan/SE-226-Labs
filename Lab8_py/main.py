from abc import ABC, abstractmethod

class FrequencyCounter(ABC):
    address = ""

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(FrequencyCounter):
    def calculateFreqs(self):
        initialLetters = []
        FreqLetters = []
        letters = []

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        letters.append(char.lower())

        uniqueLetters = set(letters)

        for letter in uniqueLetters:
            frequency = letters.count(letter)
            initialLetters.append(letter)
            FreqLetters.append(letter + " = " + str(frequency))

        print("List =", initialLetters)
        print("Resulting List =", FreqLetters)


class DictCount(FrequencyCounter):
    def calculateFreqs(self):
        initialLetters = {}
        FreqLetters = {}

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        char = char.lower()
                        initialLetters[char] = initialLetters.get(char, 0)
                        FreqLetters[char] = FreqLetters.get(char, 0) + 1

        print("Dict =", initialLetters)
        print("Updated Dict =", FreqLetters)

listCounter = ListCount("weirdWords.txt")
listCounter.calculateFreqs()

dictCounter = DictCount("weirdWords.txt")
dictCounter.calculateFreqs()
