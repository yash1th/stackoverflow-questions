def applyRules(char, rules):
    modified = char
    for rule in rules:
        r = rule.split(':')
        table = str.maketrans({r[0]:r[1]})
        modified = modified.translate(table)
    return modified

print(applyRules('abdecbc',['b:c','c:d']))


# def applyRules(string, rules):
#     mapping = str.maketrans(dict(x.split(':') for x in rules))

#     while True:
#         new = string.translate(mapping)
#         if string == new:
#             break
#         string = new

#     return new
