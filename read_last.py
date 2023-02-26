# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file 
# и выводить на печать построчно последние строки в количестве lines (на всякий случай 
# проверим, что задано положительное целое число). 

# реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину 
# (или список слов, если таковых несколько)

def read_last(lines_count, filename):
    if lines_count <= 0:
        return
    with open(filename,"r",encoding="UTF-8") as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.strip(),lines))
        all_lines = len(lines)
        lines_count = min(lines_count,all_lines)
        for i in range(lines_count):
            print(lines[all_lines-lines_count+i])
            # print(lines[-i-1]) # выведет в обратном порядке

def longest_words(filename):
    res = list()
    max_len = 0
    with open(filename,"r",encoding="UTF-8") as file:
        lines = file.read().splitlines()
        for line in lines:
            words = line.split(" ")
            for word in words:
                current_Len = len(word)
                if current_Len > max_len:
                    res.clear()
                    res.append(word)
                    max_len = current_Len
                elif current_Len == max_len:
                    res.append(word)
    print("Самые длинные слова: ", *res)
                    



input_lines = int(input("ВВедите количество строк: "))
read_last(input_lines,"article.txt")
longest_words("article.txt")