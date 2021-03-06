from pony.orm import *
from decimal import Decimal


db = Database()


########################################################################

class StockInfo(db.Entity):
    id = PrimaryKey(int, auto=True)
    stockId = Required(str)
    name = Required(str)
    industry = Required(str)

########################################################################


class StockDetail(db.Entity):
    id = PrimaryKey(int, auto=True)
    stockId = Required(str)
    yearSeason = Optional(str)
    revenue = Optional(Decimal)
    profitAfterTax = Optional(Decimal)
    grossMargin = Optional(Decimal)
    operatingIncome = Optional(Decimal)
    profitAfterTaxPercentage = Optional(Decimal)
    roe = Optional(Decimal)
    eps = Optional(Decimal)

########################################################################


class StockDividend(db.Entity):
    id = PrimaryKey(int, auto=True)
    stockId = Required(str)
    year = Optional(str)
    cashDividends = Optional(Decimal)
    stockDividends = Optional(Decimal)
    totalDividends = Optional(Decimal)


########################################################################
class DailyExchangeInfo(db.Entity):
    id = PrimaryKey(int, auto=True)
    stockId = Required(str)
    name = Required(str)
    dividendYield = Optional(Decimal)
    year = Optional(str)
    dividendYield = Optional(Decimal)
    pERatio = Optional(Decimal)
    pBRatio = Optional(Decimal)
    financialReportSeason = Optional(str)
    closingPrice = Optional(Decimal)
    upDownPrice = Optional(Decimal)
