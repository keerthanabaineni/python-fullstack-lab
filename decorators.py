# 1. The "Greeting" Decorator
# Create a decorator called @hello_decorator.

# Task: Before calling the function, it should print "Hello! I am about to run."
# Task: After the function finishes, it should print "Done! That was easy."
def hello_decorator(func):
    def wrapper():
        print("Hello! I am about to run.")
        func()
        print("Done! That was easy.")
    return wrapper 
@hello_decorator
def greet():
    print("Welcome to the world of Python!")
greet()
# 2. The "Result Doubler"
# Write a decorator called @double.

# Task: Take the result of a function (like a function that returns 5) and multiply it by 2.
# Test it: Decorate a function get_number() that returns 10. Calling it should now give you 20.
def double(func):
    def wrapper():
        result=func()
        return result*2
    return wrapper
@double
def getnumber():
    return 10
print(getnumber())
# 3. The "Angry Text" Decorator
# Create a decorator called @make_upper.

# Task: Take a function that returns a string (like "hello") and convert that string to all UPPERCASE.
# Test it: Decorate a function greet() that returns "welcome home". It should now return "WELCOME HOME".
def decorator(func):
    def wrapper():
        result=func()
        return result.upper()  
    return wrapper
@decorator
def greet():
    return 'hello'
print(greet())
# 4. The "Security Guard"
# Write a decorator called @check_password.

# Task: Inside the wrapper, ask the user for a password using input().
# Logic: If the password is "python123", call the original function. If not, print "Access Denied!" and don't run the function.
def check_password(func):
    def wrapper():
        s=input("Enter your password")
        if s=='python123':
            func()
        else:
         print("Access Denied!")
    return wrapper
@check_password
def sec():
    print("Security Guard")
sec()
# 5. Simple Counter
# Create a decorator called @announce.

# Task: Every time the decorated function is called, print "A function is being executed right now!"
# Test it: Apply this to a simple function that just prints "Working..." and call it three times in a row.
# Example Template for Students:
def announce(func):
    def wrapper():
        print("A function is being executed right now!")
        func()                                            
    return wrapper

@announce
def working():
    print("Working...")
working()
working()
working()



