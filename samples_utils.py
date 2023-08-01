import utils.pytool_utils as pyutils

# test demo
yr = pyutils.profit_to_year_rate(7.73, 1000, 90)
output_str = 'year rate: {:.3}%'.format(yr * 100)
print(output_str)

mon = pyutils.year_rate_to_profit(0.03135, 1000, 90) # 3.1%
output_str = 'days profit: {:.3}'.format(mon)
print(output_str)
