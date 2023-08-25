"""
write a protram to return the factorial of n using recursion
"""


"""
Time COmplexity = O(n)
Space Complexity = O(n) -> this is bacause o fthe stack space 
"""
def factorial_recursion(n):
    if n<=1:
        return 1

    return n*factorial_recursion(n-1)



print(factorial_recursion(5))