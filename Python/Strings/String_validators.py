# Given Code
if __name__ == '__main__':
    s = input()
    # Answer
    print(any(c.isalnum() for c in s)) # c is for character, we are searching any alphanumerical c in every s
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))