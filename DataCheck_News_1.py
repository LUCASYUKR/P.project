from konlpy.tag import Okt
from konlpy.utils import pprint
from konlpy.tag import Kkma
from konlpy.tag import Hannanum
import multiprocessing


method = input("select Method(Okt,Kkma,Hannanum):")

if method == "Okt":
    method = "Okt"

elif method == "Kkma":
    method = "Kkma"

elif method == "Hannanum":

    han = Hannanum()
input_path = input("input path(txt):")
output_path = input("output path(txt):")
f = open(output_path, "w", -1, "utf-8", newline="")
o = open(input_path)
text = o.readlines()

def count(text,method):

    for text in text:
        if method == "Okt":
            okt = Okt()
            text = okt.nouns(text)
        elif method == "Kkma":
            kkma = Kkma()
            text = kkma.nouns(text)
        elif method == "Hannanum":
            method = "Hannanum"
            text = han.nouns(text)
        # text = text.strip()
        # text = okt.nouns(text)
        for i in range(len(text)):
            if len(text[i]) >= 2:
                print(text[i])
                if text[i][-4:] == "함으로써" or \
                        text[i][-4:] == "하겠다고" or \
                        text[i][-4:] == "해왔다고":
                    text[i] = text[i][:-4]

                if text[i][-3:] == "하겠다" or \
                        text[i][-3:] == "되더라" or \
                        text[i][-3:] == "했는데" or \
                        text[i][-3:] == "하면서" or \
                        text[i][-3:] == "하려면" or \
                        text[i][-3:] == "했다면" or \
                        text[i][-3:] == "되더라" or \
                        text[i][-3:] == "되면서" or \
                        text[i][-3:] == "하도록" or \
                        text[i][-3:] == "되면서" or \
                        text[i][-3:] == "적으로" or \
                        text[i][-3:] == "하겠다" or \
                        text[i][-3:] == "시키기" or \
                        text[i][-3:] == "때문에" or \
                        text[i][-3:] == "으로써" or \
                        text[i][-3:] == "됐지만" or \
                        text[i][-3:] == "했으나" or \
                        text[i][-3:] == "하고자" or \
                        text[i][-3:] == "하려면" or \
                        text[i][-3:] == "했다고" or \
                        text[i][-3:] == "하는지" or \
                        text[i][-3:] == "하다고" or \
                        text[i][-3:] == "하지만" or \
                        text[i][-3:] == "하거나" or \
                        text[i][-3:] == "되도록" or \
                        text[i][-3:] == "한다면" or \
                        text[i][-3:] == "이지만":
                    text[i] = text[i][:-3]

                if text[i][-2:] == "되는" or \
                        text[i][-2:] == "했다" or \
                        text[i][-2:] == "에서" or \
                        text[i][-2:] == "부터" or \
                        text[i][-2:] == "대로" or \
                        text[i][-2:] == "적인" or \
                        text[i][-2:] == "으로" or \
                        text[i][-2:] == "보다" or \
                        text[i][-2:] == "까지" or \
                        text[i][-2:] == "한다" or \
                        text[i][-2:] == "에도" or \
                        text[i][-2:] == "하고" or \
                        text[i][-2:] == "들이" or \
                        text[i][-2:] == "들은" or \
                        text[i][-2:] == "하는" or \
                        text[i][-2:] == "하다" or \
                        text[i][-2:] == "에는" or \
                        text[i][-2:] == "됐다" or \
                        text[i][-2:] == "되고" or \
                        text[i][-2:] == "하며" or \
                        text[i][-2:] == "하고" or \
                        text[i][-2:] == "됐다" or \
                        text[i][-2:] == "되고" or \
                        text[i][-2:] == "한다" or \
                        text[i][-2:] == "이다" or \
                        text[i][-2:] == "하기" or \
                        text[i][-2:] == "했고" or \
                        text[i][-2:] == "처럼" or \
                        text[i][-2:] == "했고" or \
                        text[i][-2:] == "하되" or \
                        text[i][-2:] == "해야" or \
                        text[i][-2:] == "됐던" or \
                        text[i][-2:] == "하게" or \
                        text[i][-2:] == "된다" or \
                        text[i][-2:] == "했고" or \
                        text[i][-2:] == "들을" or \
                        text[i][-2:] == "되나" or \
                        text[i][-2:] == "했던" or \
                        text[i][-2:] == "했고" or \
                        text[i][-2:] == "되며" or \
                        text[i][-2:] == "해야" or \
                        text[i][-2:] == "했음" or \
                        text[i][-2:] == "들을" or \
                        text[i][-2:] == "하기" or \
                        text[i][-2:] == "였고" or \
                        text[i][-2:] == "됐던" or \
                        text[i][-2:] == "라고" or \
                        text[i][-2:] == "에게" or \
                        text[i][-2:] == "과는" or \
                        text[i][-2:] == "들에" or \
                        text[i][-2:] == "되면" or \
                        text[i][-2:] == "에서" or \
                        text[i][-2:] == "으로" or \
                        text[i][-2:] == "한다" or \
                        text[i][-2:] == "하면" or \
                        text[i][-2:] == "받고" or \
                        text[i][-2:] == "까지" or \
                        text[i][-2:] == "에만":
                    text[i] = text[i][:-2]

                if text[i][-1:] == "는" or \
                        text[i][-1:] == "를" or \
                        text[i][-1:] == "은" or \
                        text[i][-1:] == "로" or \
                        text[i][-1:] == "와" or \
                        text[i][-1:] == "이" or \
                        text[i][-1:] == "도" or \
                        text[i][-1:] == "에" or \
                        text[i][-1:] == "을" or \
                        text[i][-1:] == "에" or \
                        text[i][-1:] == "되" or \
                        text[i][-1:] == "과" or \
                        text[i][-1:] == "의" or \
                        text[i][-1:] == "며" or \
                        text[i][-1:] == "가" or \
                        text[i][-1:] == "의" or \
                        text[i][-1:] == "적" or \
                        text[i][-1:] == "될" or \
                        text[i][-1:] == "된" or \
                        text[i][-1:] == "돼" or \
                        text[i][-1:] == "중" or \
                        text[i][-1:] == "것" or \
                        text[i][-1:] == "인" or \
                        text[i][-1:] == "하":
                    text[i] = text[i][:-1]
                text[i] = text[i].strip()
                f.write(text[i]+"\n")
                print("입력완료")

if __name__ == "__main__":
    if method:
        pass
    if input_path:
        pass
    if output_path:
        pass
    print("confirm the information")
    proc = multiprocessing.Process(target=count, args=(text,method,))
    proc.start()
    proc.join()
    print("Multiprocessing terminated")
    f.close()






