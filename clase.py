class FechaHora(object):
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __min=0
    __seg=0
    def __init__(self,dia=1,mes=1,año=2021,hora=0,min=0,seg=0):
        if(hora>=0 and hora<24 and min>=-1 and min<=60 and seg>-1 and seg<=60 and mes>0 and mes<13):
            if((año%400==0) or (año%100==0 and año%4==0)):
                mesbisiestos=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                mesbisiestos=[31,28,31,30,31,30,31,31,30,31,30,31]
            if(dia<=mesbisiestos[mes-1] and dia>0):
                self.__dia=dia
                self.__mes=mes
                self.__año=año
                self.__hora=hora
                self.__min=min
                self.__seg=seg
            else:
                print("dia mal ingresado")
        
    def __str__(self):
        return'<dia,mes,año,hora,min,seg>={}/{}/{} {}:{}:{}'.format(self.__dia,self.__mes,self.__año,self.__hora,self.__min,self.__seg)
    def getdia(self):
        return self.__dia
    def getmes(self):
        return self.__mes
    def getaño(self):
        return self.__año
    def gethora(self):
        return self.__hora
    def getmin(self):
        return self.__min
    def getseg(self):
        return self.__seg
    def __add__(self,otro):
        año=self.__año + otro.getaño()
        hora=self.__hora + otro.gethora()
        minutos=self.__min + otro.getmin()
        segundos=self.__seg + otro.getseg()
        mes=self.__mes + otro.getmes()
        dia=self.__dia + otro.getdia()
        if((año%400==0) or (año%100==0 and año%4==0)):
            mesbisiestos=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            mesbisiestos=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(segundos > 60):
            segundos=segundos - 60
            minutos+=1
        if(minutos > 60):
            minutos-=60
            hora+=1
        if(hora > 24):
            hora-=24
            dia+=1
        if(mes > 12):
            mes-=12
            año+=1
        if(dia > mesbisiestos[mes-1]):
            dia-=mesbisiestos[mes-1]
            mes+=1
            if(mes > 12):
                mes-=12
                año+=1
        return FechaHora(dia,mes,año,hora,minutos,segundos)      
        #return FechaHora(self.__dia+otro.getdia(),self.__mes+otro.getmes(),self.__año+otro.getaño(),self.__hora+otro.gethora(),self.__min+otro.getmin(),self.__seg+otro.getseg()) 
    def __sub__(self,otro):#f
        año=self.__año - otro.getaño()
        hora=self.__hora - otro.gethora()
        minutos=self.__min - otro.getmin()
        segundos=self.__seg - otro.getseg()
        mes=self.__mes - otro.getmes()
        dia=self.__dia - otro.getdia()
        if((año%400==0) or (año%100==0 and año%4==0)):
            mesbisiestos=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            mesbisiestos=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(segundos <= 0):
            segundos+=60
            minutos-=1
        if(minutos <= 0):
            minutos +=60
            hora -= 1  
        if(hora <= 0):
            hora+=24
            dia-=1
        if mes <= 0:
            año-=1
            mes+=12    
        if dia < 0:
            mes-=1
            if(mes <= 0 ):
                mes+=12
                año-=1
            dia+=mesbisiestos[mes-1]
        return FechaHora(dia,mes,año,hora,minutos,segundos)

        #return FechaHora(self.__dia-otro.getdia(),self.__mes-otro.getmes(),self.__año-otro.getaño(),self.__hora-otro.gethora(),self.__min-otro.getmin(),self.__seg-otro.getseg())
    def __gt__(self,otro):
        dia=self.__dia > otro.getdia()
        mes=self.__mes > otro.getmes()
        año=self.__año > otro.getaño()
        hora=self.__hora > otro.gethora()
        minutos=self.__min > otro.getmin()
        segundos=self.__seg > otro.getseg()
        print(dia,mes,año,hora,minutos,segundos)
        