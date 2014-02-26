import datetime
import pdb
__author__ = 'kristof'

print('Hello Python'.center(60, '!'))

l = ['abcdefg', 'a b c d', 'a_b_c_d', '1234567', '123 456', 'aaaaaaa']
print(l)
print(' '.join(map(lambda x: str(str(x).isalpha()), l)))

s = 'Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.'
print(s.replace(' ', '_'))
print('_'.join(s.split(' ')))
print(s.replace('t', 'b'))
print(s.replace('r', 'l'))

s = 'Dear {name}, this is the final reminder for the payment of {amount}.\n' \
    'Please pay the amount of {amount} on our account as soon as possible.\n' \
    'We expect {amount} to be payed before {date}'

d = datetime.datetime.today()
d += datetime.timedelta(10)

def amount(x):
    return '€{credit:.2f}'.format(credit=x)

print(s.format(name='Kristof', amount=amount(234.56), date=d.strftime('%d, %b %Y')))
pdb.set_trace()
print(s.format(name='Mark', amount=amount(1290.56), date=d.strftime('%d, %b %Y')))
print(s.format(name='Patrick', amount=amount(23234.56), date=d.strftime('%d, %b %Y')))