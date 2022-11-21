def getter(name):
    t = open('./game/data.txt').read()
    vars_string = t.split('\n')

    vars = {}

    for i in vars_string:
        s = i.split('=')
        vars[s[0]] = s[1]

    return vars[name]

def setter(name, value):
    t = open('./game/data.txt').read()
    s = (f'{t}\n{name}={value}')
    open('./game/data.txt', 'w').write(s)
    