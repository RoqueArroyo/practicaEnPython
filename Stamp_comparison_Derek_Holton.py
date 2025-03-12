# Este programa sirve para ver desde qué cantidad podemos formar una estampa, con dos tipos
# de estampas de valores a y b respectivamente (con a y b primos relativos y positivos)
a = int(input("Ingrese el valor de la primera estampa: "))
b = int(input('Ingrese el valor de la segunda estampa: '))
m = min([a,b])
M = max([a,b])

if a<=0 or b<=0:
    print("Estamos trabajando con estampas, no hay estampas de valor negativo")
elif a%b==0 or b%a==0:
    print("Los números a comparar tienen que ser primos relativos")
else:
    i = 0 #contador que va a ir aumentando el número con el que trabajemos
    min_times = False #depende de la variable counter, que cuenta cuantos números consecutivos se pueden formar
    fail = False
    counter = 0 #hace que min_times se vuelva True cuando cuenta una cantidad de m números consecutivos formados 
    success = False

    if (m+i+1)%m==0 or (m+i+1)%M==0:
        counter = 1
        while (not min_times) and (not fail):
            match = False

            j = 1
            while (m+i+1)-(m*j)>0:
                if ((m+i+1)-(m*j))%M == 0:
                    match = True
                    break
                j += 1
            
            if match == True:
                counter += 1
            else:
                counter = 0
                i = 0
                Fail = True
                break
            
            if counter == m:
                min_times = True
        
        if fail == False:
            print('Los numeros empiezan desde el ',m)
            success = True


    elif ((M+i+1)%m==0 or (M+i+1)%M==0) and (not success):
        fail = False
        counter = 1
        while (not min_times) and (not fail):
            match = False

            j = 1
            while (M+i+1)-(m*j)>0:
                if ((M+i+1)-(m*j))%M == 0:
                    match = True
                    break
                j += 1
            
            if match == True:
                counter += 1
            else:
                counter = 0
                i = 0
                Fail = True
                break
            
            if counter == m:
                min_times = True

        if fail == False:
            print('Los numeros empiezan desde el ',M)
            success = True       


    elif ((m+M+i)%m==0 or (m+M+i)%M==0) and (not success): 
        counter = 1
        while not min_times:
            match = False

            j = 1
            while (m+M+i)-(m*j)>0:
                if ((m+M+i)-(m*j))%M == 0:
                    match = True
                    break
                j += 1
            
            if match == True:
                counter += 1
            else:
                counter = 0
            
            if counter == m:
                min_times = True
                i-=1
            i+=1    

        if fail == False:
            print('Los numeros empiezan desde el ',m + M + i - (m - 1))    
    