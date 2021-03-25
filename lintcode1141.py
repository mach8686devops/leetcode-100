class Solution:
    """
    @param year: a number year
    @param month: a number month
    @return: Given the year and the month, return the number of days of the month.
    """

    def getTheMonthDays(self, year, month):
        # write your code here
        normal_days = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        unnormal_days = [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def leap_years(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        if leap_years(year) and month == 2:
            return unnormal_days[month]
        return normal_days[month]
