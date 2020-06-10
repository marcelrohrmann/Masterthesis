expression = list()


with open("C:/Users/spacefactory/Desktop/Marcel/expressions.txt", "r", encoding='utf-8-sig') as f:
    for line in f:
        expression.append(line)

expression.sort()
print(expression)