def collatz(number):
    if number % 2 == 0:
        result = number // 2
        return result
    else:
        result = 3 * number + 1
        return result

prompt = "Please input an integer: "
number = int(input(prompt))
while number != 1:
    print(collatz(number))
    number = collatz(number)