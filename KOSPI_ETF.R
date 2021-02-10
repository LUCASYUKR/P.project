library(dplyr)
library(ggplot2)

data = read.csv("/Users/dbdudghks/Desktop/KOSPI_ETF.csv")

str(data)

KOSPI_ETF_Price <- data %>% group_by(Date) %>% select(Date,Close,Volume) %>% summarise(mean=mean(Close))

KOSPI_ETF_Price

ggplot(data=KOSPI_ETF_Price, aes(x=Date,y=mean,group=1))+geom_line(size=1,color="red",linetype="twodash")+
  ggtitle("KOSPI ETF Rate Period 2017.02 ~ 2021.02")+xlab("Time")+
  ylab("Close Price")

KOSPI_ETF_TOTAL_Amount = data %>% group_by(Date) %>% select(Date,Total_Amount) %>%
  summarise(mean = mean(Total_Amount))
KOSPI_ETF_TOTAL_Amount

ggplot(data = KOSPI_ETF_TOTAL_Amount, aes(x=Date,y=mean,group=1))+geom_line(color="blue",linetype="twodash")+
  ggtitle("KOSPI ETF Total Amount Period 2017.02~2021.02")+xlab("Time")+ylab("Total Amount")
