def average(array):
    # Answer
    distinct_heights = set(array)
    avg = sum(distinct_heights) / len(distinct_heights)
    return avg
# Given Code
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)