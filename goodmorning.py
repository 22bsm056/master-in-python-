import time
timestamp=time.strftime('H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)
current_hour = int(time.strftime('%H'))
if 6<current_hour>12:
    print("hello shubham  good morning")
elif 12<=current_hour>18:
    print("hello shubham goofd afternoon")
else:
    print("good night bye sweet dream")