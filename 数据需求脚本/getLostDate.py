import datetime


def get_lost_date(dates):
    # 去重
    even_dates = list(set(dates))
    # 排序
    even_dates.sort()
    # 转成date型
    even_dates = [datetime.datetime.strptime(each_date, '%Y-%m-%d').date() for each_date in even_dates]
    # 拿到首尾两天
    start_date = even_dates[0]
    end_date = even_dates[len(even_dates)-1]
    # 存放完整的每一天
    full_dates = []
    while start_date <= end_date:
        every_date = start_date.strftime('%Y-%m-%d')
        full_dates.append(every_date)
        start_date += datetime.timedelta(days=1)
    # 再转回去
    even_dates = [str(each_date) for each_date in even_dates]
    # 求差集
    rest_dates = [rest_date for rest_date in full_dates if rest_date not in even_dates]
    return rest_dates
