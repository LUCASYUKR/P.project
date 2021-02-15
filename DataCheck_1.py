import csv

select = input("Select the data format <Oil, Stock>\n")
if select == "Stock":
    f = open("/Users/dbdudghks/Desktop/stock_S&P.csv","r",newline="")
    write = open("/Users/dbdudghks/Desktop/stock_S&P_2.csv","w",newline="")
elif select == "Oil":
    f = open("/Users/dbdudghks/Desktop/Crude_Oil.csv", "r", newline="")
    write = open("/Users/dbdudghks/Desktop/Crude_Oil_2.csv", "w", newline="")

CsvFile = csv.reader(f, delimiter=",")

# ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
date = []
open = []
high = []
low = []
close = []
adjClose = []
volume = []

for rows in CsvFile:
    date.append(rows[0][:7])
    open.append(rows[1])
    high.append(rows[2])
    low.append(rows[3])
    close.append(rows[4])
    adjClose.append(rows[5])
    volume.append(rows[6])


print("date:",date)
print("open:",open)
print("high:",high)
print("low:",low)
print("close:",close)
print("adjclose:",adjClose)
print("volume",volume)


writeCSV = csv.writer(write)

for i in range(0,len(date)):
    if close[i] == "null":
        pass
    else:
        writeCSV.writerows([[date[i],open[i],high[i],low[i],close[i],adjClose[i],volume[i]]])

write.close()
f.close()
