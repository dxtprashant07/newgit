def findunion(arr1, arr2):
    s = set()
    union = []
    for i in arr1:
        s.add(i)
    for i in arr2:
        s.add(i)
    for i in s:
        union.append(i)
    return union  # or return None
def main():
    arr1 = [2,3,4,5,6,7,8]
    arr2 = [1,2,3,4,5]
    union = findunion(arr1,arr2)
    print("the union is ", union)
if __name__ == '__main__':
    main()
