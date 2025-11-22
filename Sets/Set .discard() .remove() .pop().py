# Given Code
n = int(input())
s = set(map(int, input().split()))
# Answer
n_command = int(input())

for i in range(n_command):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    if command[0] == "remove":
        s.remove(int(command[1]))
    if command[0] == "discard":
        s.discard(int(command[1]))
        
print(sum(s))