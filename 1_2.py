# 1.Create a program to compare three numbers and find the bigger numbers.[topics covered: identified, variable, types, operator, if statement]
# 2. Write the above solution in a function which takes take numbers and return the bigger number[topic covered: function]

def num():
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    c = int(input("enter third number"))

    abc = []
    abc.append(a)
    abc.append(b)
    abc.append(c)

    return max(abc)


print(num())

