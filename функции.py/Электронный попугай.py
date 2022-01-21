a = []


def parrot(phrase):
    if phrase not in a:
        a.append(phrase)
    else:
        print(phrase)