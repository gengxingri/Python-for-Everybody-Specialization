# Other short code for ex_11.1
import re
print(sum([int(num) for num in re.findall('[0-9]+', open('regex_sum_1466060.txt').read())]))
