def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
number=int(input("enter a number to find factorial : \n"))
print(f"Factorial of {number} (iterative):", fact(number))
