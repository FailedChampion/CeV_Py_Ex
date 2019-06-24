import time

localtime = time.localtime()
timelocal = time.strftime('%m/%d/%Y, %H:%M:%S', localtime)

print(time.strftime('%B\n%A %D'))
print(time.strftime('%H:%M:%S'))

print('\n')


print(timelocal)