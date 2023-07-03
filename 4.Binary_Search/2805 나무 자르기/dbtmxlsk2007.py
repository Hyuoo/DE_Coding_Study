N,M = map(int, input().split())    
H = list(map(int, input().split())) 

start = 0
end = max(H)

def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start+end)//2 
        tot = 0
        
        for i in arr:
            if i > mid:
                tot += i - mid
            
        if tot >= target:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
            
    return result

print(binary_search(H, M, start, end))
