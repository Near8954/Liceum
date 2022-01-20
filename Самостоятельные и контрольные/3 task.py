road = input().split('_')
who = input().split('+')
d = dict()
a = []
for i in range(len(road)):
    if len(set(road[i]).intersection(set(who[i]))) >= 2:
        print(f'{road[i].title()}: {who[i]}')
