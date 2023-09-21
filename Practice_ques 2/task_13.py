class calculator:
    
    @staticmethod
    def add(x,y):
        print('addition of',x ,'and',y, 'is:',x+y)

    @staticmethod
    def sub(x,y):
        print('substraction of',x ,'and',y, 'is:',x-y)

    @staticmethod
    def mul(x,y):
        print('multiplication of',x ,'and',y, 'is:',x*y)

    @staticmethod
    def div(x,y):
        print('division of',x ,'and',y, 'is:',round(x/y))

calculator.add(4,2)
calculator.sub(4,2)
calculator.mul(4,2)
calculator.div(4,2)