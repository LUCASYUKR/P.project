import csv

txt = open("/Users/dbdudghks/Desktop/1.txt", "r")  # txt 파일은 hadoop 에서 wordcount 된 파일을 가정함
lines = txt.readlines()

txt_filtered = open("/Users/dbdudghks/Desktop/2.csv", "wt", newline="", encoding='UTF-8')
writer_csv = csv.writer(txt_filtered)
fields = ["key", "value"]
writer_csv.writerow(fields)

Current_word = None
Current_count = 0
for line in lines:
    line_split = line.split("\t")  # key,value 생성

    find_point = line_split[0].find(".")  # "." 필터링
    if line_split[0].find(".")>0:
        line_split[0] = line_split[0][:find_point]

    find_comma = line_split[0].find(",")  # "," 필터링
    if line_split[0].find(",")>0:
        line_split[0] = line_split[0][:find_comma]

    find_double = line_split[0].find("'")  # "'" 필터링
    if line_split[0].find("'")>0:
        line_split[0] = line_split[0][:find_double]

    find_n_0 = line_split[0].find("\n")  # 특수문자 필터링 5
    if line_split[0].find("\n"):
        line_split[0] = line_split[0][:find_n_0]

    find_n_1 = line_split[0].find("\t")  # 특수문자 필터링 5
    if line_split[0].find("\t"):
        line_split[0] = line_split[0][:find_n_1]

    find_single = line_split[0].find("\"")  # " " " 필터
    if line_split[0].find("\"")>0:
        line_split[0] = line_split[0][:find_single]

    find_open = line_split[0].find("(")  # "(" 필터링
    if line_split[0].find("(")>0:
        line_split[0] = line_split[0][:find_open]

    find_close = line_split[0].find(")")  # ")" 필터링
    if line_split[0].find(")") > 0:
        line_split[0] = line_split[0][:find_close]

    find_special = line_split[0].find("”")  # 특수문자 ” 필터링
    if line_split[0].find("”")>0:
        line_split[0] = line_split[0][:find_special]

    find_special2 = line_split[0].find("…")  # 특수문자 … 필터링
    if line_split[0].find("…") > 0:
        line_split[0] = line_split[0][:find_special2]

    find_special3 = line_split[0].find("\"")  # 특수문자 필터링 2
    if line_split[0].find("\"") == 0:
        line_split[0] = line_split[0][find_special3+1:]

    find_special4 = line_split[0].find("\'")  # 특수문자 필터링 3
    if line_split[0].find("\'") == 0:
        line_split[0] = line_split[0][find_special4 + 1:]

    find_special5 = line_split[0].find("-")  # 특수문자 필터링 4
    if line_split[0].find("-") == 0:
        line_split[0] = line_split[0][find_special5 + 1:]

    find_n = line_split[1].find("\n")  # 특수문자 필터링 5
    if line_split[1].find("\n"):
        line_split[1] = line_split[1][:find_n]

    find_special6 = line_split[0].find("“")  # 특수문자 필터링 6
    if line_split[0].find("“") == 0:
        line_split[0] = line_split[0][find_special6 + 1:]

    find_special7 = line_split[0].find("1")  # 특수문자 필터링 6
    if line_split[0].find("1") > 0:
        line_split[0] = line_split[0][:find_special7]

    find_connect = line_split[0][-2:]  # 2자 조사 필터링
    if line_split[0][-2:] == "되는" or \
            line_split[0][-2:] == "했다" or \
            line_split[0][-2:] == "에서" or \
            line_split[0][-2:] == "부터" or \
            line_split[0][-2:] == "대로" or \
            line_split[0][-2:] == "적인" or \
            line_split[0][-2:] == "으로" or \
            line_split[0][-2:] == "보다" or \
            line_split[0][-2:] == "까지" or \
            line_split[0][-2:] == "한다" or \
            line_split[0][-2:] == "에도" or \
            line_split[0][-2:] == "하고" or \
            line_split[0][-2:] == "들이" or \
            line_split[0][-2:] == "들은" or \
            line_split[0][-2:] == "하는" or \
            line_split[0][-2:] == "하다" or \
            line_split[0][-2:] == "에는" or \
            line_split[0][-2:] == "됐다" or \
            line_split[0][-2:] == "되고" or \
            line_split[0][-2:] == "하며" or \
            line_split[0][-2:] == "하고" or \
            line_split[0][-2:] == "됐다" or \
            line_split[0][-2:] == "되고" or \
            line_split[0][-2:] == "한다" or \
            line_split[0][-2:] == "이다" or \
            line_split[0][-2:] == "하기" or \
            line_split[0][-2:] == "했고" or \
            line_split[0][-2:] == "처럼" or \
            line_split[0][-2:] == "했고" or \
            line_split[0][-2:] == "하되" or \
            line_split[0][-2:] == "해야" or \
            line_split[0][-2:] == "됐던" or \
            line_split[0][-2:] == "하게" or \
            line_split[0][-2:] == "된다" or \
            line_split[0][-2:] == "했고" or \
            line_split[0][-2:] == "들을" or \
            line_split[0][-2:] == "되나" or \
            line_split[0][-2:] == "했던" or \
            line_split[0][-2:] == "했고" or \
            line_split[0][-2:] == "되며" or \
            line_split[0][-2:] == "해야" or \
            line_split[0][-2:] == "했음" or \
            line_split[0][-2:] == "들을" or \
            line_split[0][-2:] == "하기" or \
            line_split[0][-2:] == "였고" or \
            line_split[0][-2:] == "됐던" or \
            line_split[0][-2:] == "라고" or \
            line_split[0][-2:] == "에게" or \
            line_split[0][-2:] == "과는" or \
            line_split[0][-2:] == "들에" or \
            line_split[0][-2:] == "되면" or \
            line_split[0][-2:] == "에서" or \
            line_split[0][-2:] == "으로" or \
            line_split[0][-2:] == "한다" or \
            line_split[0][-2:] == "하면" or \
            line_split[0][-2:] == "받고" or \
            line_split[0][-2:] == "까지" or \
            line_split[0][-2:] == "에만":
        line_split[0] = line_split[0][:-2]
                                            # 1자 조사 필터링
    if line_split[0][-1:] == "는" or \
            line_split[0][-1:] == "를" or \
            line_split[0][-1:] == "은" or \
            line_split[0][-1:] == "로" or \
            line_split[0][-1:] == "와" or \
            line_split[0][-1:] == "이" or \
            line_split[0][-1:] == "도" or \
            line_split[0][-1:] == "에" or \
            line_split[0][-1:] == "을" or \
            line_split[0][-1:] == "에" or \
            line_split[0][-1:] == "되" or \
            line_split[0][-1:] == "과" or \
            line_split[0][-1:] == "의" or \
            line_split[0][-1:] == "며" or \
            line_split[0][-1:] == "가" or \
            line_split[0][-1:] == "의" or \
            line_split[0][-1:] == "적" or \
            line_split[0][-1:] == "될" or \
            line_split[0][-1:] == "된" or \
            line_split[0][-1:] == "돼" or \
            line_split[0][-1:] == "중" or \
            line_split[0][-1:] == "것" or \
            line_split[0][-1:] == "인" or \
            line_split[0][-1:] == "하":
        line_split[0] = line_split[0][:-1]

                                             # 3자 조사 필터링
    if line_split[0][-3:] == "하겠다" or \
            line_split[0][-3:] == "되더라" or \
            line_split[0][-3:] == "했는데" or \
            line_split[0][-3:] == "하면서" or \
            line_split[0][-3:] == "하려면" or \
            line_split[0][-3:] == "했다면" or \
            line_split[0][-3:] == "되더라" or \
            line_split[0][-3:] == "되면서" or \
            line_split[0][-3:] == "하도록" or \
            line_split[0][-3:] == "되면서" or \
            line_split[0][-3:] == "적으로" or \
            line_split[0][-3:] == "하겠다" or \
            line_split[0][-3:] == "시키기" or \
            line_split[0][-3:] == "때문에" or \
            line_split[0][-3:] == "으로써" or \
            line_split[0][-3:] == "됐지만" or \
            line_split[0][-3:] == "했으나" or \
            line_split[0][-3:] == "하고자" or \
            line_split[0][-3:] == "하려면" or \
            line_split[0][-3:] == "했다고" or \
            line_split[0][-3:] == "하는지" or \
            line_split[0][-3:] == "하다고" or \
            line_split[0][-3:] == "하지만" or \
            line_split[0][-3:] == "하거나" or \
            line_split[0][-3:] == "되도록" or \
            line_split[0][-3:] == "한다면" or \
            line_split[0][-3:] == "이지만":
        line_split[0] = line_split[0][:-3]

                                          # 4자 조사 필터링
    if line_split[0][-4:] == "함으로써" or \
            line_split[0][-4:] == "하겠다고" or \
            line_split[0][-4:] == "해왔다고":
        line_split[0] = line_split[0][:-4]

    try:
        count = int(line_split[1])  # 문자열로 가져온 숫자를 정수형으로 캐스팅
    except ValueError:
        continue

    if Current_word == line_split[0]:  
        Current_count += count 
    else:
        Current_count = count
        Current_word = line_split[0]

        if Current_word:
            result = [[str(Current_word), str(Current_count)]]
            if Current_word != "" and len(Current_word) >= 2:
                writer_csv.writerows(result)
           

if Current_word == line_split[0]:  
    result = [[str(Current_word), str(Current_count)]]
    if Current_word != "" and len(Current_word) >= 2:
        writer_csv.writerows(result)

txt.close()
txt_filtered.close()


