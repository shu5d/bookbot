def get_book_text(path):
    num_words = 0
    with open(path) as f:
        book = f.read()
    words = book.split()
    for i in words:
        num_words += 1
    return num_words

def letter(text):
    with open(text) as f:
        book = f.read()
    dic = {}
    words = book.lower()
    for letter in words:
        dic[letter] = 0
    for letter in words: 
        dic[letter] += 1
    return dic

def sort_on(dict):
    return dict["num"]

def fmlsort(dic):
    list = []
    for i in dic: 
        if i.isalpha()== True:
            list.append({"char":i,"num":dic[i]})
    list.sort(reverse=True, key=sort_on)
    return list