def solution(arr):
    answer=0
    arr=sorted(arr)
    for i in range(len(arr)-1):  # 유클리드 알고리즘 활용(?!)
        arr1 = arr.pop(-1)
        arr2 = arr.pop(-1)
        while True:
            arr3 = arr1%arr2
            if arr3 == 0:
                answer=arr2
                arr.append(arr2)
                break
            else:
                arr1=arr2
                arr2=arr3

    # arr 모든수의 곱 / answer
