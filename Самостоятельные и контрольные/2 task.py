n = int(input())
Magic_signals = set()
Defence_grid = set()
Teleportation = set()
for i in range(n):
    s = int(input())
    if s % 10 == 0:
        Magic_signals.add(s)
    elif s % 2 != 0 and len(str(s)) <= 3:
        Defence_grid.add(s)
    elif s % 2 == 0 and s > 999 and s % 10 != 0:
        Teleportation.add(s)
print(f'Magic signals ({max(Magic_signals) * min(Magic_signals)}).')
print(f'Defence grid ({sum(Defence_grid)}).')
print(f'Teleportation ({len(Teleportation)}).')