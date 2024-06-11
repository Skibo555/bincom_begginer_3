# I create this function to handle the logic
def fib_seq(n):
    # I initialize the value of 'a' to 0, so the sequence will start as 0.
    a = 0
    b = 1
    """while the argument entered into the function is an int, and it's a positive int, 
    the loop keeps increasing until it reaches the the value of n"""
    while n > 0:
        # This prints the current value of a so the sequence starts from 0 for that's the initial value of n
        print(a)
        # This line updates the value of a and b to
        a, b = b, a + b
        n -= 1


fib_seq(30)
