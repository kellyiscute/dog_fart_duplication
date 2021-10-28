import re

if __name__ == "__main__":
    text1 = ""
    with open("text1.txt", "r") as f:
        text1 = f.read()
    text2 = ""
    with open("text2.txt", "r") as f:
        text2 = f.read()

    text1_sentenses = re.split(r"，|。|？", text1)
    text2_sentenses = re.split(r"，|。|？", text2)

    for i in range(text1_sentenses.__len__()):
        text1_sentenses[i] = text1_sentenses[i].strip().replace("123456", "")
    for i in range(text2_sentenses.__len__()):
        text2_sentenses[i] = text2_sentenses[i].strip().replace("java实习经历", "")

    text1_sentenses = set(text1_sentenses)
    text2_sentenses = set(text2_sentenses)
    intersect_result = text1_sentenses.intersection(text2_sentenses)
    print(text1.__len__(), text2.__len__(), intersect_result.__len__())
    for s in intersect_result:
        print(s)
