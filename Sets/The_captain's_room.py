# No Code Given
# Answer Below
K = int(input())

room_list = list(map(int, input().split()))
unique_rooms = set(room_list)
captain_room = (sum(unique_rooms) * K - sum(room_list)) // (K - 1)

print(captain_room)