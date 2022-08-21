import time

time_list = [7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20]
time_hour = time.localtime().tm_hour


if time_hour in time_list:
    print("存在")
