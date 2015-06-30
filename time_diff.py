import sys
from datetime import datetime

test_cases = open(sys.argv[1], 'r')
t_fmt = '%H:%M:%S'

for test in test_cases:
    times = test.split()
    if times[0] > times[1]:
        diff = datetime.strptime(times[0], t_fmt) - datetime.strptime(times[1], t_fmt)
        str_t = str(diff)
        hours, minutes, seconds = map(int, str_t.split(':'))
        print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
    else:
        diff = datetime.strptime(times[1], t_fmt) - datetime.strptime(times[0], t_fmt)
        str_t = str(diff)
        hours, minutes, seconds = map(int, str_t.split(':'))
        print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))

test_cases.close()
