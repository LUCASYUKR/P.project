from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import ssl


context = ssl._create_unverified_context()

# 2021/01/05 Index 비어있는 것 처리 해야 함  -> 완료
# 2021/01/07 문단 간 띄어쓰기 제거  -> 완
# 2021/01/07 Index 가 더 이상 없는 경우 예외처리 필요함
# 2021/01/07 하둡 wordcount or 데이터 분석을 위한 데이터 몰아 생성 로직 필요함
select = input("2020/02~2020/12 : 1\n 2021/01~ : 2\n")

if select == "1":
    index = 56682
    #61519
    close = True
elif select =="2":
    index = 61520
    close = False

pageCheck = urlopen("https://www.kita.net/cmmrcInfo/cmmrcNews/cmmrcNews/cmmrcNewsDetail.do?pageIndex=2&nIndex=61520&sSiteid=1&searchReqType=detail&searchCondition=TITLE&searchStartDate=&searchEndDate=&categorySearch=&searchKeyword=", context=context)
pageSoup = BeautifulSoup(pageCheck, "html.parser")
titleCheck = pageSoup.find("title")

if pageCheck:
    while True:

        if close == True:
            if index > 61519:
                print("New Crawling untill 2020/12 finished")
                exit()

        html = urlopen("https://www.kita.net/cmmrcInfo/cmmrcNews/cmmrcNews/cmmrcNewsDetail.do?pageIndex=1&nIndex="+str(index)+"&sSiteid=6&searchReqType=detail&searchCondition=TITLE&searchStartDate=&searchEndDate=&categorySearch=&searchKeyword=", context=context)
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.findAll(align="center")
        text = bsObj.findAll("div", {"align": "justify"})
        allText = title + text

        try:
            replaceStr = str(title[0].get_text()).replace("/","")

            if replaceStr.find("?"):
                replaceStr = replaceStr.replace("?", "")
                f = open("/Users/dbdudghks/Desktop/tradeNews.txt", "a", -1, "utf-8", newline="")  # Mac os root
            # /Users/dbdudghks/Desktop/news
            # if replaceStr.find("/"):
             #  replaceStr1 = replaceStr.replace("/", "-")
              # f = open("C:/Users/dbdud/Desktop/news/" + replaceStr1 + ".txt", "w", -1, "utf-8")
            else:
                f = open("/Users/dbdudghks/Desktop/tradeNews.txt", "a", -1, "utf-8", newline="")  # Mac os root

            print("-", title[0].get_text(), "-" + "\n")
            timeCheck = datetime.datetime.now()
            f.write("-" + title[0].get_text() + "-" + " <" + str(timeCheck) + ">")
            for textList in text:
                print(textList.get_text())
                f.write(str(textList.get_text()) + "\n")
            f.close()
            index = index + 1
        except IndexError:
            index = index + 1
            pass


else:
    print("==최근 뉴스까지 전부 크롤링 되었습니다.==")
    print("      ==프로그램을 종료합니다.==")
    exit()