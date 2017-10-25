class BinarySearch:

    def binary_search_iterative(self, a, key):
        low = 0
        high = len(a) - 1

        while low <= high:
            mid = low + ((high-low)//2)

            if a[mid] == key:
                return mid

            if a[mid] > key:
                high = mid-1
            else:
                low = mid-1

        return -1


alist = [54,26,93,17,77,31,44,55,20]
alist.sort()
print(alist)
bs = BinarySearch()
print("Key -> ", bs.binary_search_iterative(alist, 77))
