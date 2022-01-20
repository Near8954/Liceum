a = ''


def print_without_duplicates(message):
    global a
    if message != a:
        print(message)
        a = message
        

