error = []
class Pass:
    def __init__(self):
        self.password()
    def password(self):
        str = input('Enter the password: ')
        self.error(str)
    def error(self,str):
        if len(str)>=8:
            a=b=c=d=0
            for i in str:
                if i.isupper():
                    a+=1
                elif i.islower():
                    b+=1
                elif i.isdigit():
                    c+=1
                elif i=='@' or i=='_' or i=='-':
                    d+=1
            if a<1:
                error.append('Contain at least one uppercase letter')
            if b<1:
                error.append('Contain at least one lowercase letter')
            if c<1:
                error.append('Contain at least one digit')
            if d<1:
                error.append('Contain at least one special character')
            if a>0 and b>0 and c>0 and d>0:
                print('Strong')
            else:
                print('Weak')
                print('Error:',error)
                self.password()
        else:
            print('Minimum 8 characters should be present')
            self.password()
obj = Pass()