# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

## Write a function that takes a positive integer and returns the sum of its digits. For example, the sum of the digits in 123 is 1 + 2 + 3 = 6.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

## Write a program that takes a string and counts the number of vowels (a, e, i, o, u) in it. Consider both uppercase and lowercase letters.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

## Write a function that checks if a number is even or odd.
def is_even(n):
    return n % 2 == 0