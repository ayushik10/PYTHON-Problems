# def abc(a, b, c, d=10, e=20)

def show(a, b, c):
    print(a)
    print(b)
    print(c)

# show("Hello", "Hii", "ByeBye")
# show(b="Hello", c="Hii", a="ByeBye")

def display(a, b, c, d="Python", e="course"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

# display("hello", "world", "python", e="ayushi")

# print("ayushi", "kumari", "is", "a", "BCA", "Student")
    
def show(a, b, c, *args, d=10, **kwargs):
    print(a)
    print(args)
    print(d)
    print(c)
    print(kwargs)

show(1,2,3, "python", d=100, name="ayushi")