x = 10
# def show():
#     global x
#     x += 5
#     print(x)
def show():
    y='local'
    print(x)
    print(y)

# def outer():
#     x='local'

#     def inner():
#         print(x)
    
#     inner()
#     print(x)

# outer()

show()
print(x)
# print(y)