
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
    """日收益到年利率计算
    year_rate: 年利率
    invest: 本金
    day:    投入天数
    return: 投入天数对应实际收益
    """
    year_profit = year_rate * invest
    profit = year_profit / CONST_YEAR_DAYS * day
    return profit
