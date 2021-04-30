from clase import FechaHora
from CLASEMENU import Menu
if __name__ == "__main__":
    dia=input("Ingresar dia: ")
    mes=input("Ingresar mes:  ")
    año=input("Ingresar año: ")
    h=input("ingresar hora: ")
    m=input("Ingresar minutos: ")
    s=input("Ingresar segundos: ")
    if(any(chr.isdigit() for chr in dia)== False):
        print("error al ingresar dia")
        dia=input("Ingresar dia: ")
    if(any(chr.isdigit() for chr in mes)== False):
        print("error al ingresar mes")
        mes=input("Ingresar mes:  ")
    if(any(chr.isdigit() for chr in año)== False):
        print("error al ingresar año")
        año=input("Ingresar año: ")
    if(any(chr.isdigit() for chr in h)== False):
        print("error al ingresar hora")
        h=input("ingresar hora: ")
    if(any(chr.isdigit() for chr in m)== False):
        print("error al ingresar minutos")
        m=input("Ingresar minutos: ")
    if(any(chr.isdigit() for chr in s)==False):
        print("error al ingresar segundos")
        s=input("Ingresar segundos: ")
    a=FechaHora(int(dia),int(mes),int(año),int(h),int(m),int(s))
    print("---------------------------------------------------------")
    dia=input("Ingresar dia: ")
    mes=input("Ingresar mes:  ")
    año=input("Ingresar año: ")
    h=input("ingresar hora: ")
    m=input("Ingresar minutos: ")
    s=input("Ingresar segundos: ")
    if(any(chr.isdigit() for chr in dia)== False):
        print("error al ingresar dia")
        dia=input("Ingresar dia: ")
    if(any(chr.isdigit() for chr in mes)== False):
        print("error al ingresar mes")
        mes=input("Ingresar mes:  ")
    if(any(chr.isdigit() for chr in año)== False):
        print("error al ingresar año")
        año=input("Ingresar año: ")
    if(any(chr.isdigit() for chr in h)== False):
        print("error al ingresar hora")
        h=input("ingresar hora: ")
    if(any(chr.isdigit() for chr in m)== False):
        print("error al ingresar minutos")
        m=input("Ingresar minutos: ")
    if(any(chr.isdigit() for chr in s)==False):
        print("error al ingresar segundos")
        s=input("Ingresar segundos: ")
    b=FechaHora(int(dia),int(mes),int(año),int(h),int(m),int(s))
    MenU=Menu()
    op=None
    while(op!=5):
        print("|------------------------------------------------------|")
        print("|1 para: sumar los objetos ingresados                  |")
        print("|2 para: restar los objetos ingresados                 |")
        print("|3 para: ver cual objeto es mayor                      |")
        print("|4 para:test                                           |")
        print("|------------------------------------------------------|")
        op=int(input("ingresar opcion: "))
        MenU.opcion(op,a,b)