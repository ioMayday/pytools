
# 利率计算
CONST_YEAR_DAYS = 365.
def profit_to_year_rate(profit, invest, day):
    """
    日收益到年利率计算
    profit: 收益
    invest: 本金
    day:    投入天数
    return: 年利率收益
    """
    year_profit = profit / day * CONST_YEAR_DAYS
    year_rate = year_profit / invest
    return year_rate


def year_rate_to_profit(year_rate, invest, day):
    """年利率到日收益计算
    year_rate: 年利率
    invest: 本金
    day:    投入天数
    return: 投入天数对应实际收益
    """
    year_profit = year_rate * invest
    profit = year_profit / CONST_YEAR_DAYS * day
    return profit


def calc_dcf_total(profit, years, discount_rate):
    """dcf现金流计算
    profit: 年利润
    years:    投入年数
    discount_rate: 折现率
    return: 折现到现价
    """
    # 假设固定profit
    dcf = 0
    for i in range(years):
        dcf = dcf + profit / ((1 + discount_rate)**i)
    return dcf


