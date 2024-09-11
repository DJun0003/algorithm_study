def solution(nums):
    total = len(set(nums))    
    return total if total < len(nums)//2 else len(nums)//2 