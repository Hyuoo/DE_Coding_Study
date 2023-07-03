N = int(input()) 
cards = list(map(int, input().split()))

M = int(input()) 
compare = list(map(int, input().split()))
result = []
cards.sort()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2 
        
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

start = 0
end = len(cards)-1
for com in compare:
    result.append(binary_search(cards, com, start, end))

print(*result)
