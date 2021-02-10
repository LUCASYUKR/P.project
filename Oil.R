library(dplyr)
library(ggplot2)


data = read.csv("/Users/dbdudghks/Desktop/Crude_Oil_2.csv")

str(data)
table(is.na(data$Low))
# FALSE 1021

summary(data)

boxplot(data$Close)
# For checking price flow, need to left all stock data

Crud_Oil <- data %>% group_by(Date) %>% select(Date,Close) %>%
  summarise(mean=mean(Close))
Crud_Oil

ggplot(data = Crud_Oil,aes(x=Date,y=mean,group=1))+geom_line(linetype="twodash")+
  xlab("Time")+ylab("Crud Oil Price")+ggtitle("Crud Oil Price Period 2017.01 ~ 2021.02")
