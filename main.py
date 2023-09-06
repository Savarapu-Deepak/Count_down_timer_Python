import time

my_Time = int(input('Enter Time in Minutes : '))

for i in range(my_Time * 60, 0, -1):
    secs = i % 60
    mins = int(i / 60) % 60
    hrs = int(i / 3600)
    print(f'{hrs:02}:{mins:02}:{secs:02}')
    time.sleep(1)

print('STOP....TIMES..UP')

