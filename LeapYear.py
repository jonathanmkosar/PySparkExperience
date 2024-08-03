
def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 > 0 or year % 400 == 0)


class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if month == 2:
            return 29 if is_leap(year) else 28
        if month in {4, 6, 9, 11}:
            return 30
        return 31
    
print(Solution().numberOfDays(2000,3))