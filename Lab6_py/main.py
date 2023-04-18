n = int(input("Enter a value for n: "))
x = int(input("Enter a value for x: "))


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def summation(nums):
    result_1 = 0
    for number in nums:
        result_1 += number
    return result_1


terms = lambda i: (n ** i) / factorial(i)

term_list = list(map(terms, range(x + 1)))

result = summation(term_list)

print(f"e^{n} = {result}")


def compute_sum(n2):
    """
    This function computes the sum of the series (-1)^(k+1)/k for k from 1 to n ,
    using recursion and a global variable.

    :paramater n: The number of terms in the series.
    """

    global total_sum
    if n2 == 0:
        return
    else:
        compute_sum(n2 - 1)
        total_sum += (-1) ** (n2 + 1) / n2


total_sum = 0
n2 = int(input("Enter a value for n: "))
compute_sum(n2)
print(compute_sum.__doc__)
print("The sum is : ", total_sum)
