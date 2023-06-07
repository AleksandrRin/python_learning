friends = ['ivan', 'oleg', 'petr', 'nikolai']

print(f'{friends[0].title()} приходи ко мне в гости')
print(f'{friends[1].title()} приходи ко мне в гости')
print(f'{friends[2].title()} приходи ко мне в гости')
print(f'{friends[3].title()} приходи ко мне в гости')

friends[-1] = 'stas'
print(f'{friends} новые гости')

print(f'{friends[0].title()} обещал прийти в гости')
print(f'{friends[1].title()} обещал прийти в гости')
print(f'{friends[2].title()} обещал прийти в гости')
print(f'{friends[3].title()} обещал прийти в гости')

a = friends.pop(0)
print(f'{a.title()} не сможет прийти')
print(f'{friends.pop().title()} тоже не прийдет')
friends.pop()
print(friends)
del friends[0]
print(friends)