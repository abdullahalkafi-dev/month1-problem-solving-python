def two_sum_brute(nums: list[int], target: int) -> list[int]:
    """Brute-force"""
    length = len(nums)
    for i in range(length):
        for j in range (i+1,length):
            if nums[i]+nums[j]==target:
             return [i,j]
    raise ValueError("No valid pair found")

def two_sum_hash(nums: list[int], target: int) -> list[int]:
    """Hash map based"""
    index_num={}
    for i , num in enumerate(nums):
        complement=target-num
        if complement in index_num:
            return [index_num[complement],i]
        index_num[num]=i
    raise ValueError("No valid pair found")          
           
if __name__ == "__main__":
    print(two_sum_brute([2,7,11,15],13))
    print(two_sum_hash([2,7,11,15],13))