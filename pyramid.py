def print_pyramid(n):
    for i in range(n):
        # Print leading spaces to center the stars
        print(" " * (n - i - 1), end="")
        # Print stars for the current row
        print("*" * (2  i + 1))

# Example: A pyramid of height 5
print_pyramid(5)
