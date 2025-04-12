# The walrus operator := allows you to assign a value to a variable as part of an expression.
# It's especially useful when you want to avoid repeating a function call or expression.

# Example 1: Assign and compare in one line
# Without walrus operator:
n = len(my_list)
if n > 5:
    print(f"List is too long ({n} elements)")

# With walrus operator:
if (n := len(my_list)) > 5:
    # Here, 'n' gets assigned the value of len(my_list) within the if condition itself
    print(f"List is too long ({n} elements)")

# Example 2: Reading input until a condition is met
# Without walrus:
while True:
    user_input = input("Enter something (or 'exit'): ")
    if user_input == 'exit':
        break
    print(f"You entered: {user_input}")

# With walrus:
while (user_input := input("Enter something (or 'exit'): ")) != 'exit':
    # Assigns input to 'user_input' and checks the condition in one line
    print(f"You entered: {user_input}")

# Note:
# - Walrus operator is available only in Python 3.8 and above.
# - It improves performance and readability when used appropriately.
