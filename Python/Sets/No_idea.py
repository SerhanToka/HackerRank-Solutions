# No Code Given
# Answer Below
input()
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness = 0

for x in array:
    if x in set_a:
        happiness += 1
    if x in set_b:
        happiness -= 1
        
print(happiness)