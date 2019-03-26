#
import datetime
import time

def date_str_to_ts(a_shit):
    """ 1548509506  ->  2019-01-26 21:31:46 """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a_shit))


print datetime.datetime.now()

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print time.strftime('%Y-%m-%d', time.localtime(time.time()))
#
#
#
#
# print int(time.mktime(time.strptime('2019-02-21 23:59:59','%Y-%m-%d %H:%M:%S')))
#
#
#
# print int(time.mktime(time.strptime('2019-02-21','%Y-%m-%d')))
# print int(time.mktime(time.strptime('2019-02-22','%Y-%m-%d')))
#
# def get_day_ts_range(day):
#     day_begin = int(time.mktime(time.strptime(day, '%Y-%m-%d')))
#     day_end = day_begin + 3600 * 24 -1
#     print day_begin
#     print day_end
#
# get_day_ts_range('2019-02-22')
# print time.strftime('%Y-%m-%d', time.localtime(time.time()))
# import datetime
# def get_date_from_datestr(date_str):
#
#     try:
#         print type(datetime.datetime.strptime(startDate, '%Y-%m-%d'))
#         return datetime.datetime.strptime(startDate, '%Y-%m-%d')
#     except ValueError:
#         return None
#
# startDate = "2018-2-11"
# a=get_date_from_datestr(startDate)
# startDate = "2018-2-13"
# b=get_date_from_datestr(startDate)
#
# print (b - a).days
#
#
#
# while a <= b:
#     print str(a)
#     print type(str(a.date()))
#     a = a + datetime.timedelta(days=1)
#
