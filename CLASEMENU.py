class Menu():
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            3:self.op3,
            4:self.op4
        }
    def opcion(self,op,a,b):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>3):
            func()
        else:
            func(a,b)
    def op1(self,a,b):
        suma=a+b
        print(a)
        print(b)
        print(suma)
    def op2(self,a,b):
        resta=a-b
        print(a)
        print(b)
        print(resta)
    def op3(self,a,b):
        mayor=a>b
        print(a)
        print(b)
         
    def op4(self,a,b):
        a=FechaHora(24,1,2001,12,40,30)
        b=FechaHora(10,6,2010,14,20,30)
        suma=a+b
        print(a)
        print(b)
        print(suma)
        print("---------")
        resta=a-b
        print(a)
        print(b)
        print(resta)
        print("---------")
        mayor=a>b
        print(a)
        print(b)
        print(mayor)