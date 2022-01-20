def print_long_words(text):
    text = text.lower()
    gl = 0
    gl_all = [ 'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я', 'a', 'e', 'i', 'o', 'u', 'y']
    word = ''
    for i in text:
        if i.isalpha():
            word += i
            if i in gl_all:
                gl += 1
        else:
            if gl >= 4:
                print(word)
            gl = 0
            word = ''
print_long_words('Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.')