library(dplyr)
library(ggplot2)
library(KoNLP)
library(NIADic)
library(wordcloud2)

data = read.csv("/Users/dbdudghks/Desktop/filtered_trade2021.csv")

data
str(data)
table(is.na(data$key))
# NA 값 3개
table(is.null(data$key))

table(is.na(data$value))
table(is.null(data$value))
# Null 값 없음

data$key <- trimws(data$key,which="both",whitespace = "[\t\n\r]")
#data <- sort(data$value,decreasing = T)
data <- arrange(data,desc(value))
data
wordcount_2 <- data %>% group_by(key) %>% summarise(total=sum(value)) %>% arrange(desc(total))
wordcount_2
ggplot(data=wordcount_2,aes(x=key,y=total,reorder(-total)))+geom_col()+
  theme(text=element_text(size=12,family="AppleGothic"))+coord_flip()

wordcloud2::wordcloud2(data=wordcount_2,fontFamily="AppleGothic",backgroundColor="Black",color="random-light")


#====================================================================================
KoNLP::useNIADic()
data_1 <- readLines("/Users/dbdudghks/Desktop/tradeNews_2021.txt")

data_2 <- sapply(data_1,extractNoun,USE.NAMES = F)
head(data_2)
data_3 <- unlist(data_2)
head(data_3)

file.create("text.txt")
writeLines(data_3,"/Users/dbdudghks/Desktop/text.txt",sep="\n")


#====================================================================================

datas = read.csv("/Users/dbdudghks/Desktop/2.csv")

datas
str(datas)
table(is.na(datas$key))
# NA 값 3개
table(is.null(datas$key))

table(is.na(datas$value))
table(is.null(datas$value))
# Null 값 없음

datas$key <- trimws(datas$key,which="both",whitespace = "[\t\n\r]")
#data <- sort(data$value,decreasing = T)
datas <- arrange(datas,desc(value))
datas
wordcount_2 <- datas %>% group_by(key) %>% summarise(total=sum(value)) %>% arrange(desc(total))
wordcount_2
ggplot(datas=wordcount_2,aes(x=key,y=total,reorder(-total)))+geom_col()+
  theme(text=element_text(size=12,family="AppleGothic"))+coord_flip()

wordcloud2::wordcloud2(data=wordcount_2,fontFamily="AppleGothic",backgroundColor="Black",color="random-light")
20