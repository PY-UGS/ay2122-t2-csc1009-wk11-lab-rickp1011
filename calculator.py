class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def substractor(self):
        return self.num1 - self.num2

    def multiplier(self):
        return (self.num1 * self.num2)

    def divider(self):
        return (self.num1 / self.num2)

    def clear(self):
        self.num1 = 0
        self.num2 = 0
        return self.num1, self.num2

num1 = int(input("please input 1"))
num2 = int(input("please input number 2"))
c = calculator(num1,num2)
print(c.addition())
print(c.substractor())
print(c.multiplier())
print(c.divider())
print(c.clear())
