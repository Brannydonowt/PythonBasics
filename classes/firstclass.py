# first class from scratch
# flex your new found knowledge young sire.

class Calculator:
    inputNumbers = []

    def addNumber(self, num):
        self.inputNumbers.insert(len(self.inputNumbers), num)

    def removeNumber(self, num):
        if self.inputNumbers.__contains__(num):
            print(f"Number {num} was found in targets.")
            self.inputNumbers.remove(num)
        else:
            print(f"Number {num} was not in the targets")

    def multiplytargets(self):
        if len(self.inputNumbers) > 0:
            result = 1
            for item in self.inputNumbers:
                result = result * item
            return result
        else:
            print("User has not chosen any numbers")

calc = Calculator()
calc.addNumber(10)
calc.addNumber(5)
calc.addNumber(1)

calc.removeNumber(1)

calc.addNumber(2)

print(calc.multiplytargets())