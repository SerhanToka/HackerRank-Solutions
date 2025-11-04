# Given code
if __name__ == '__main__':
    N = int(input())
# Answer
my_list = []

for i in range(N):
    command_line = input().split()
    if command_line[0] == "insert":
        my_list.insert(int(command_line[1]), int(command_line[2]))
    elif command_line[0] == "print":
        print(my_list)
    elif command_line[0] == "remove":
        my_list.remove(int(command_line[1]))
    elif command_line[0] == "append":
        my_list.append(int(command_line[1]))
    elif command_line[0] == "sort":
        my_list.sort()
    elif command_line[0] == "pop":
        my_list.pop()
    elif command_line[0] == "reverse":
        my_list.reverse()