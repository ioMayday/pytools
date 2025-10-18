import utils.pytool_utils as pyutils


if __name__ == "__main__":
    # test demo
    yr = pyutils.profit_to_year_rate(7.73, 1000, 90)
    output_str = 'year rate: {:.3}%'.format(yr * 100)
    print(output_str)

    mon = pyutils.year_rate_to_profit(0.03135, 1000, 90) # 3.1%
    output_str = 'days profit: {:.3}'.format(mon)
    print(output_str)

    res = profit_to_year_rate(0.24, 6155, 1)
    print("\n")
    print(res)

    res = year_rate_to_profit(0.06, 5000, 21)
    print("\n")
    print(res)

    res = calc_dcf_total(10, 10, 0.06) # output: 78.01
    print("\n")
    print(res)
