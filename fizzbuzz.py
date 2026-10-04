
def fizzBuzz(n):
    val = []
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            val.append("FIZZBUZZ")
        elif number % 3 == 0:
            val.append("Fizz")
        elif number % 5 == 0:
            val.append("Buzz")
        else:
            val.append(str(number))
    return (val)






























