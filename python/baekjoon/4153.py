while True:
    arr = list(map(int,input().split()))
    if arr[0]==0 and arr[1]==0 and arr[2]==0:
        break
    arr.sort()
    if pow(arr[0],2)+pow(arr[1],2)==pow(arr[2],2):
        print("right")
    else:
        print("wrong")

