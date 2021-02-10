import datetime as dt
from urllib.request import urlopen
import urllib.request
import ssl


def datecheck(period1,period2):
    p1 = str(period1)
    p2 = str(period2)
    dateCal = int(p1)-int(p2)

    if dateCal>=0:
        print("*** period1 has to be smaller than period2 ***")
        print("- period1 :",period1," / period2 :",period2,"-")
        print(" ")
        print("The process is stopped")
        exit()

    period_1 = dt.datetime.strptime(p1,"%Y%m%d").date()
    period_2 = dt.datetime.strptime(p2,"%Y%m%d").date()

    batch = period_2-period_1
    batch_1 = str(batch).split()[0]
    print(batch_1,"days(str)")
    return batch_1

def url(period1,days):
    oneDay = 86400
    stUrl = 1546300800  # 2019/01/01
    stDate = 20190101
    first = period1

    if int(first) < stDate:
        dateCal = int(datecheck(first, stDate))
        first = stUrl-(oneDay*dateCal)
    else:
        dateCal = int(datecheck(stDate,first))
        first = stUrl+(oneDay*dateCal)

    #first = 1577836800  # 2020/01/01

    day = int(days)
    second = int(first + (day*oneDay))

    return first, second


while True:
    print("**To stop process, input 'stop'**")
    period1 = input("Period1(YYYYMMDD):")
    if period1=="stop":
        exit()
    period2 = input("Period2(YYYYMMDD):")
    if period2=="stop":
        exit()


    days = int(datecheck(period1,period2))

    first,second = url(period1,days)

    context = ssl._create_unverified_context()

    url = "https://query1.finance.yahoo.com/v7/finance/download/CL=F?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true".format(first, second)
    savename = "/Users/dbdudghks/Desktop/Crude_Oil.csv"

    # Date, Open, High, Low, Close, Adj Close, Volume
    fileURL = urllib.request.urlopen(url,context=context).read()

    with open(savename,mode="wb") as f:
        f.write(fileURL)