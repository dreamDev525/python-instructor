# Arithmetic

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calc(a, b, op, op_name):
    result = eval(f"{a}{op}{b}")
    print(f"{a}\t{op}\t{b}\t->\t{result}\t{op_name}".expandtabs(6))


calc(10, 4, "+", "Addition")
calc(10, 4, "-", "Subtraction")
calc(10, 4, "*", "Multiplication")
calc(10, 4, "/", "Division")
calc(10, 4, "//", "Floor division")
calc(10, 4, "**", "Exponentiation")
calc(10, 4, "%", "Modulus")

# 10    +     4     ->    14    Addition
# 10    -     4     ->    6     Subtraction
# 10    *     4     ->    40    Multiplication
# 10    /     4     ->    2.5   Division
# 10    //    4     ->    2     Floor division
# 10    **    4     ->    10000 Exponentiation
# 10    %     4     ->    2     Modulus
# 10    ^     4     ->    14    XOR

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
calc(1, 1, "^", "XOR")
calc(1, 0, "^", "XOR")
calc(0, 1, "^", "XOR")
calc(0, 0, "^", "XOR")

# 1     ^     1     ->    0     XOR
# 1     ^     0     ->    1     XOR
# 0     ^     1     ->    1     XOR
# 0     ^     0     ->    0     XOR

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
calc(10, 4, "^", "XOR")

# 10    ^     4     ->    14    XOR

# How to calculate this?
# 10  -> 1010
# 04  -> 0100
# XOR -> 1110 -> 14