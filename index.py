# 1. arb_args — Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
    for a in args:
        print(a)

# Example usage:
print("Example 1 - arb_args:")
arb_args(10, 20, 30, 40)
print()  # For better readability in the output

# 2. inner_func — Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(x, y):
    def inner_1():
        return x + y
    def inner_2():
        return x - y
    print(inner_1() + inner_2())

# Example usage:
print("Example 2 - inner_func:")
inner_func(8, 3)
print()  # For better readability in the output

# 3. lunch_lady — Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)

# Example usage:
print("Example 3 - lunch_lady:")
lunch_lady("Alice", "Pizza")
lunch_lady("Bob")
print()  # For better readability in the output

# 4. sum_n_product — Accepts two integers and returns both the sum and the product.

def sum_n_product(x, y):
    return x + y, x * y

# Example usage:
print("Example 4 - sum_n_product:")
result = sum_n_product(5, 4)
print(result)
print()  # For better readability in the output

# 5. alias_arb_args — Should be arb_args but assigned an alias.

alias_arb_args = arb_args

# Example usage:
print("Example 5 - alias_arb_args:")
alias_arb_args(100, 200, 300)
print()  # For better readability in the output

# 6. arb_mean — Accepts any number of integers and prints their average.

def arb_mean(*args):
    total = 0
    for a in args:
        total += a
    print(total / len(args))

# Example usage:
print("Example 6 - arb_mean:")
arb_mean(4, 8, 15, 16, 23, 42)
print()  # For better readability in the output

# 7. arb_longest_string — Accepts any number of strings and returns the longest one.

def arb_longest_string(*args):
    long = 0
    longest = ""
    for a in args:
        if len(a) > long:
            long = len(a)
            longest = a
    return longest

# Example usage:
print("Example 7 - arb_longest_string:")
print(arb_longest_string("apple", "banana", "cherry", "blueberry"))
