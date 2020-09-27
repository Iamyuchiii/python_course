# def calender(month,day,s_day):
#     month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
#                   'november', 'december']
#     days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days_of_week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
#     weeks = ""
#     print ("      " + month)
#     for w in days_of_week:
#         weeks += w + "\t"
#     print (weeks)
#     # for w in days_of_week:
#     #     print (w, end="\t")
#     # print("\n")
#     print ("\t" * (s_day - 1), end = "\t")
#     # print("\t" * (s_day - 1), end= "\t")
#     # days = ""
#     # for i in range(1, day + 1):
#     #     if (i + s_day) % 7 == 0:
#     #         days += str(i) + "\n"
#     #     else:
#     #         days += str(i) + "\t"
#     # print (days)
#     for i in range(1, day+1):
#         if (i+s_day) % 7 != 0:
#             print (i, end = "\t" )
#         else:
#             print (i)
#
# mon_year = "September 2018"
# calender(mon_year,30, 6)

"""
Calender 2
"""
def calender2 (month, year):
    normal = {'january':31, 'february':28, 'march':31, 'april':30, 'may':31, 'june':30, 'july':31, 'august':31, 'september':30, 'october':31,
                  'november':30, 'december':31}
    leap = {'january':31, 'february':29, 'march':31, 'april':30, 'may':31, 'june':30, 'july':31, 'august':31, 'september':30, 'october':31,
                  'november':30, 'december':31}
    pattern = {'january':0, 'february':3, 'march':3, 'april':6, 'may':1, 'june':4, 'july':6, 'august':2, 'september':5, 'october':0,
                  'november':3, 'december':5}
    days_of_week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    p_century = [0,6,4,2]
    # printing the weeks
    weeks = ""
    print ("     " + month, year)
    for w in days_of_week:
        weeks += w + "\t"
    print (weeks)


    # Identifying the leap year
    leap_year = False
    if year%4 == 0 and year%400 == 0:
        leap_year = True
    elif year%100 == 0:
        leap_year = False
    elif year%4 == 0:
        leap_year = True
    else:
        leap_year = False
    # Identifying the starting day
    # This is the correct way
    # century = (year - 1)//100 +1
    year_code = 0
    month_code = 0
    century = year // 100
    n_pattern = (int(century/4)+5) * p_century
    for i in range(century):
        if i == century-1:
            year_code += n_pattern[i+2]
    for key in pattern.keys():
        if month == key:
            month_code += pattern[key]
    s_day = 1 + (year - century*100)
    s_day2 = s_day + int((year - century*100)/4)
    s_day3 = s_day2 + month_code + year_code
    s_day4 = s_day3%7

    if leap:
        day = leap[month]
        print("\t" * (s_day4 - 1), end="\t")
        for i in range(1, day+1):
            if (i+s_day4) % 7 != 0:
                print (i,  end = "\t")
            else:
                print (i)
    else:
        day = normal[month]
        print("\t" * (s_day4 - 1), end="\t")
        for i in range(1, day+1):
            if (i+s_day4) % 7 != 0:
                print (i, end = "\t" )
            else:
                print (i)

calender2("october", 2021)