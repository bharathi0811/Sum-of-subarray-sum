array=list(map(int,input("Enter the Array Elements: ").split()))
class SumSubarray:
    @staticmethod
    def sum_subarray_(array):
        n = len(array)
        l = []
        for i in range(n):
            for j in range(i, n):
                l.extend([array[i:j + 1]])
        flat_list = []
        for m in l:
            flat_list.extend(m)
        sum_ = 0
        for k in flat_list:
            sum_ += k
        return sum_
obj = SumSubarray()
print(obj.sum_subarray_(array))





