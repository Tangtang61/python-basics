names = ['Fred', 'John', 'Sue', 'Sam', 'Alex', 'Angela']
found = False
for name in names:
    print(name)
    if name[0] == 'A':
        found = True

if found:
    print("""At least one name starts with an 'A' """)
