total= lambda hora, precio: hora * precio if hora <=40 else 40 * precio + (hora - 40) * 1.5 * precio

# def calculo(hora, precio):
#     if hora <= 40 :
#         total = hora * precio  
#     else:
#         total = 40 * precio + (hora - 40) * 1.5 * precio    
#     return(total)

x= 0
while (x >= 0): 
 try:    
    x = input("Introducir las horas trabajadas: ")
    x = float(x)
    #print(type(x))
 
    if  type(x)==float:
         if x > 0:
            x = float(x)
            break 
         elif x < 0:    
            print("---Introduci un valor positivo--- \nVamos de nuevo \n")
            x=0                         
 except:
        print("---Introduce un valor numerico---\n")
        x=0
        
y=0       
while (y >= 0): 
 try:    
    y = input("\nIntroducir el precio por hora trabajada: ")
    y = float(y)
    #print(type(y))
 
    if  type(y)==float:
         if y > 0:
            y = float(x)
            break 
         elif y < 0:    
            print("---Introduci un valor positivo--- \nVamos de nuevo \n")
            y=0                         
 except:
        print("---Introduce un valor numerico---\n")
        y=0    
    
        

#Total = calculo(x,y)

print(f"\nEl total a pagar es ${total(x,y)}")
