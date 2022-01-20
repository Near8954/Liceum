def who_are_you_and_hello():
    name = input()
    while not(name.istitle() and name.isalpha() and name.count(' ') == 0):
        name = input()
    print(f'Привет, {name}!')
