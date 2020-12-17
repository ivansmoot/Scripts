from datetime import datetime, timedelta


def get_lost_date(dates):
    """返回一个日期列表里所有的缺省日期

    给到一个无序且有重复值的日期list，去重排序后取到最大最小两天，返回这段时间内没有包含在list里的日期
    :param
        dates:一个日期list，需要确保里面的值都是可转date的

    :return
        rest_dates:也是一个日期list，值都是str，例如['2020-12-17']
    """
    # 去重
    even_dates = list(set(dates))
    # 排序
    even_dates.sort()
    # 转成date型
    even_dates = [datetime.strptime(each_date, '%Y-%m-%d').date() for each_date in even_dates]
    # 拿到首尾两天
    start_date = even_dates[0]
    end_date = even_dates[len(even_dates)-1]
    # 存放完整的每一天
    full_dates = []
    # 找到缺的日期
    while start_date <= end_date:
        every_date = start_date.strftime('%Y-%m-%d')
        full_dates.append(every_date)
        start_date += timedelta(days=1)
    # 再转回去
    even_dates = [str(each_date) for each_date in even_dates]
    # 求差集
    rest_dates = [rest_date for rest_date in full_dates if rest_date not in even_dates]
    return rest_dates
