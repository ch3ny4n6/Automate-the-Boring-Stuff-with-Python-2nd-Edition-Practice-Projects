def collatz(number):
    if number % 2 == 0:
        result = number // 2
        return result
    else:
        result = 3 * number + 1
        return result

prompt = "Please input an integer: "
prompt += "(press q to exit) "

while True:
    user_input = input(prompt)
    if user_input == 'q':
        break

    try:
        number = int(user_input)
    except ValueError:
        print("The input must be an integer.")
    else:
        while number != 1:
            print(collatz(number))
            number = collatz(number)