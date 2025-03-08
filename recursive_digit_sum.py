# We define super digit of an integer  using the following rules:

# Given an integer, we need to find the super digit of the integer.
# If  has only  digit, then its super digit is .
# Otherwise, the super digit of  is equal to the super digit of the sum of the digits of
def superDigit(n, k):
    # Write your code here
    def calculate_digit(n):
        if n < 10:
            return n
        n = sum(int(i) for i in str(n))
        return calculate_digit(n)

    total = sum(int(num) for num in n)
    new_n = total * k
    return calculate_digit(int(new_n))
