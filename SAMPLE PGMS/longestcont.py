# def longestcontinuos(arr):
#     st = set()
#     for i in range(len(arr)):
#         st.add(arr[i])
#     # print(st)    


# arr = [100,200,1,2,3,4]
# longestcontinuos(arr)






def longestSuccessiveElements(a):
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set()
    # put all the array elements into set
    for i in range(n):
        st.add(a[i])
    print(st)
    # Find the longest sequence
    for it in st:
        # if 'it' is a starting number
        if it - 1 not in st:
            # find consecutive numbers
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

a = [6,100, 200,0, 1, 2, 3, 4,5]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)

