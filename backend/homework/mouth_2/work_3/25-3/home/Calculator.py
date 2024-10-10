class Calculator:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Calculator(self.number + other.number)

    def __sub__(self, other):
        return Calculator(self.number - other.number)

    def __mul__(self, other):
        return Calculator(self.number * other.number)

    def __truediv__(self, other):
        if other.number != 0:
            return Calculator(self.number / other.number)
        else:
            raise ValueError("На ноль делить нельзя")

    def __str__(self):
        return str(self.number)



num1 = Calculator(15)
num2 = Calculator(3)

sum_result = num1 + num2
print(sum_result)

sub_result = num1 - num2
print(sub_result)

mul_result = num1 * num2
print(mul_result)

div_result = num1 / num2
print(div_result)

