#Decorators
'''
Implementing decorators in different
functions
'''
def decor(func):#1st decorator
    '''
    main function calling another function
    '''
    def wrap():
        '''
        wraping up function
        '''
        print("====================")
        func()
        print("====================")
    return wrap

def admin_route(func):#2nd decorators
    '''
    function for admin
    '''
    def wrap():
        name = str(input("Enter your password  "))
        if str(name) == 'admin':
            print("welcome admin")
            func()
        else:
            print("Wrong password")
    return wrap

def guest_route(func):
    '''
    function for guest
    '''
    def wrap():
        name = str(input("Enter your password  "))
        if str(name) == 'guest':
            print("welcome guest")
            func()
        else:
            print("Wrong password")
    return wrap

@decor#1st decorator implemented here
def welcome():
    '''
    function for welcoming
    '''
    print("hello world")

@admin_route#2nd decorator implemented here
def admin():
    '''
    function for admin previledge
    '''
    print("Nice to be back admin")

@guest_route#3rd decorator implemented here
def guest():
    '''
    function for guest previledge
    '''
    print("Nice to be back guest")

@decor#1st decorator implemented here
def bye():
    '''
    function for goodbye
    '''
    print("Goodbye")

#calling all the function here
decor(welcome())#1st function
admin_route(admin())#2nd function
guest_route(guest())#3rd functiom
decor(bye())#4th function
