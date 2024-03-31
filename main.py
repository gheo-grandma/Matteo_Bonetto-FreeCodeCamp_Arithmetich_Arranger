# This entrypoint file to be used in development. Start by reading README.md
#from pytest import main

from arithmetic_arranger import arithmetic_arranger

# Default string 
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# With results
print(arithmetic_arranger(["78 + 645", "38 - 236", "90 + 216", "8088 + 4895"], True))




#Testing Errors

# Too many problems
print(arithmetic_arranger(["1 + 1", "1 + 1", "1 + 1", "1 + 1", "1 + 1", "1 + 1"]))

# Only digits
print(arithmetic_arranger(["1 + A"]))

# Wrong operator
print(arithmetic_arranger(["1 * 1"]))

# Operands too long
print(arithmetic_arranger(["11111 + 1"]))

# Run unit tests automatically
#main(['-vv'])