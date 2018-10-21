```py
# hi, wang zhi jun
# sdfsdfsdf

def _is_leap_year(year):
    """判断闰年，返回1表示闰年

    year表示合法的年份，这里不再校验
    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

# test cases
# 2017 12 23 1, 2018 1 23 
# 2017 12 31 1, 2018 1 31
# 2020 1 30 1, 2020 2 29
# 2011 11 30 1, 2011 12 30
#############################
# long = 1, 3, 6, 12
def get_date(y, m, d, long=1):
    """返回正确的服务到期日

    y m d分别表示订购年月日，保证合法
    long 订购时长 单位月 合法值[1,3,6,12] 保证合法
    """
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # only long = 1 part.0
    y_add, rm = divmod(m+long, 12)# 0 12
    if y_add == 1 and rm == 0:
        y_add, rm = 0, 12
    ry = y + y_add
    
    # long = 1,3,6,12, 13, 15, … part.1
    # test case here
    # 2017 4 23 20, 2018 12 23
    # 2017 3 23 9, 2017 12 23
    a_year = (long + m - 1) // 12 # 1 
    rm = long + m  - a_year * 12 # 12
    ry = a_year + ry # 2018
    
    # part 2
    if rm != 2:
        if d == 31  and days_of_month[rm-1] == 30:
            return ry, rm, 30
        return ry, rm, d
    else:
        days_feb = 28 + _is_leap_year(ry)
        if d > days_feb:
            return ry, rm, days_feb
        return ry, rm, d

    # 月份 25~31  1，3，5 25  4 6 8 27
    # part 3 v1
    days_of_mon = dict(zip(
      range(1,13), [(24,24), (28,29), ----]))
    
    days_cur_mon = days_of_mon[rm][is_leap_year(ry)]

    if d > days_cur_mon:
      return ry, rm, days_cur_mon
    else:
      return ry, rm, d

    # part 3 v2.1
    days_of_mon = dict(zip(
      range(1,13), [(24,24), (28,29), ----]))
    
    days_cur_mon = days_of_mon[rm][is_leap_year(ry)]
    
    rd = (d, days_cur_mon)[d > days_cur_mon]
    return ry, rm, rd
  
    # part 3 v2.2
    days_of_mon = dict(zip(
      range(1,13), [24,28, ----]))
    
    days_cur_mon = days_of_mon[rm]
    
    if rm == 2 and _is_leap_year(ry):
      days_of_mon = 29
    
    rd = (d, days_cur_mon)[d > days_cur_mon]
    return ry, rm, rd
```
