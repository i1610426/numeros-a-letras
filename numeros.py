import math
unidades = ["cero", "uno", "dos" ,"tres" ,"cuatro" ,"cinco" ,
            "seis" ,"siete" ,"ocho" ,"nueve","diez"]

especiales = ["once", "doce","trece","catorce", "quince",
              "diezciseis", "diecisiete", "dieciocho", "diecinueve"]

especiales1 = ["veintiuno","veintidos", "veintitres","veinticuatro","veinticinco","veintiseis", "veintisiete",
           "veintiocho", "veintinueve"]

decenas = ["veinte", "treinta","cuarenta","cincuenta", "sesenta",
           "setenta", "ochenta", "noventa"]

        
num = int(input("Ingrese un numero entre 0-99: "))

if (num >=0 and num <11):
    print (unidades[num])

elif (num < 20):
    print (especiales[num-11])
      
elif (num >=21 and num <30):
    print (especiales1[num-21])
    
elif (num <100):
    
    unid = num% 10;
    dec = int(math.floor(num/10))
    if (unid == 0):
        print (decenas[dec-2]) 
    else:
        print (decenas[dec-2], "y" , unidades[unid])
else:
    print ("FUERA DE RANGO")


