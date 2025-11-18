def print_formatted(number):
    width = len(bin(number)[2:]) # finding binary length
    for i in range(1, number + 1):
        # finding decimal, octal, hexadecimal, binary values and adjusting them to right 
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        
        print(f"{decimal} {octal} {hexadecimal} {binary}")

# Given Code
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)