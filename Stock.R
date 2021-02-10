library(dplyr)
library(ggplot2)


data <- read.csv("/Users/dbdudghks/Desktop/stock_S&P_2.csv")

# checking data
str(data)
summary(data)
table(is.na(data$Open))

# null -> NA
data$Open <- ifelse(data$Open == "null",NA,data$Open) 
data$High <- ifelse(data$High == "null",NA,data$High)
data$Low <- ifelse(data$Low == "null",NA,data$Low)
data$Close <- ifelse(data$Close == "null",NA,data$Close)
data$Adj.Close <- ifelse(data$Adj.Close == "null",NA,data$Adj.Close)
data$Volume <- ifelse(data$Volume == "null",NA,data$Volume)
table(is.na(data$Open))
"
FALSE
  275    
  -> in Python, already null data was filtered and deleted
"
# str -> date, numeric
#data$Date <- as.Date(data$Date)
data$Open <- as.numeric(data$Open)
data$High <- as.numeric(data$High)
data$Low <- as.numeric(data$Low)
data$Close <- as.numeric(data$Close)
data$Adj.Close <- as.numeric(data$Adj.Close)
data$Volume <- as.numeric(data$Volume)
str(data)
data

# -------------------------------------------------------------------------


stock_close <- data %>% group_by(Date) %>% select(Date,Close) %>% summarise(mean = mean(Close))
stock_close

ggplot(data=stock_close,aes(x=Date,y=mean,group=1))+geom_line(linetype="twodash",color="red")+
  xlab("Time")+ylab("Close stock price")+ggtitle("S&P Stock Price Period 2017.01 ~ 2021.02")

