# No Code Given
# Answer Below
test_cases = int(input())

for _ in range(test_cases):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)