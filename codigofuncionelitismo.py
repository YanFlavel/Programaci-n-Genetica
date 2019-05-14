import numpy as np
import matplotlib.pyplot as plt
import random

def funcion(x,y,num_cromosoma):
    x_bina=[int(j) for j in range(num_cromosoma)]
    x_bina=binario(x,num_cromosoma)
    x_real=[int(j) for j in range(num_cromosoma-1)]
    for i in range(len(x_real)):
        x_real[i]=x_bina[i+1]
    
    x_r=decimal(x_real)
    if x_bina[0]==0:
        x_r=x_r*-1

    y_bina=[int(j) for j in range(num_cromosoma)]
    y_bina=binario(y,num_cromosoma)
    y_real=[int(j) for j in range(num_cromosoma-1)]
    for i in range(len(y_real)):
        y_real[i]=y_bina[i+1]
    
    y_r=decimal(y_real)
    
    if y_bina[0]==0:
        y_r=y_r*-1
    
    if x_r<=2048 and x_r>=-2048:
        if y_r<=2048 and x_r>=-2048:
            x_r=x_r/1000
            y_r=y_r/1000
            return 100*(x_r*x_r-y_r*y_r)+(1-x_r)*(1-x_r)
        
        else:
            return 0
        
    else:
        return 0

    

    

cant_ini=10

poblacion_inicial=[int (j) for j in range(cant_ini)]
poblacion_inicial2=[int (j) for j in range(cant_ini)]

for i in range(cant_ini):
    poblacion_inicial[i]=random.randrange(2048)
    poblacion_inicial2[i]=random.randrange(2048)
    

ppc=0.7
poblacion_elite_por=0.1
pm=5
num_epocas=5
num_cromosoma=13
def binario(numero,num_cromosomas):
    bina=[int(i)for i in range(num_cromosomas)]
    
    for j in range(1,num_cromosomas): 
        bina[j]=0
    inte=num_cromosoma-1

    while numero>1:
        bina[inte]=int(numero%2)
        numero=numero/2
        inte=inte-1
    bina[inte]=int(numero)
    return bina

def decimal(bina):
    numero=0
    expo=1
    for i in range(len(bina)):
        numero=numero+bina[len(bina)-1-i]*expo
        expo=expo*2
    return numero
        

def ordenar(poblacion_inicial,poblacion_inicial2,num_cromosoma):
    for i in range(len(poblacion_inicial)):
        for j in range(len(poblacion_inicial)):
            #se evaluan los dos individuos x1 y x2 en la funcion
            if funcion(poblacion_inicial[i],poblacion_inicial2[i],num_cromosoma)>funcion(poblacion_inicial[j],poblacion_inicial2[j],num_cromosoma):
                temp=poblacion_inicial[i]
                poblacion_inicial[i]=poblacion_inicial[j]
                poblacion_inicial[j]=temp
                
                temp=poblacion_inicial2[i]
                poblacion_inicial2[i]=poblacion_inicial2[j]
                poblacion_inicial2[j]=temp
    return poblacion_inicial,poblacion_inicial2

def poblacion_elite(poblacion_inicial,porcentaje_elite,poblacion_inicial2):
    elit_4=[int(j) for j in range(int(len(poblacion_inicial)/(porcentaje_elite*100)))]
    elit_5=[int(j) for j in range(int(len(poblacion_inicial)/(porcentaje_elite*100)))]
    
    for i in range(int(len(poblacion_inicial)/(porcentaje_elite*100))):
        elit_4[i]=poblacion_inicial[i]
        elit_5[i]=poblacion_inicial2[i]
    return elit_4,elit_5
    

print("Poblacion Inicial")

def cruce(poblacion_inicial,ppc,num_cromosoma,pm,cant_ini):
    int_num_mutaciones=0
    poblacion=[int (j) for j in range(int(ppc*cant_ini)*2)]
    factor_mutante=random.randrange(int(ppc*cant_ini))
    for i in range(int(ppc*cant_ini)):
        pibot=random.randrange(num_cromosoma-1)
        parte1=binario(poblacion_inicial[random.randrange(int(ppc*cant_ini))],num_cromosoma)
     #   print("PADRE A")
      #  print(parte1)
        parte2=binario(poblacion_inicial[random.randrange(int(ppc*cant_ini))],num_cromosoma)
       # print("PADRE B")
        #print(parte2)
        
        binario_temporal=[int (tt) for tt in range(num_cromosoma)]
        binario_2=[int (tt) for tt in range(num_cromosoma)]
        for j in range(pibot):
            binario_temporal[j]=parte1[j]
            binario_2[j]=parte2[j]
        for j in range(int(pibot),int(len(parte1))):
            binario_temporal[j]=parte2[j]
            binario_2[j]=parte1[j]
        
        probabilidad=random.randrange(int(ppc*cant_ini))
        if probabilidad<=pm*(int(ppc*cant_ini)):
            int_num_mutaciones=int_num_mutaciones+1
            escoge_hijo=random.randrange(2)
            index=random.randrange(len(parte1))
            if escoge_hijo==0:
                if(binario_temporal[index]==0):
                    binario_temporal[index]=1
                else:
                    binario_temporal[index]=0
         #       print("Temp_> 1 ",binario_temporal)
            else:
                if(binario_2[index]==0):
                    binario_2[index]=1
                else:
                    binario_2[index]=0
          #      print("Temp_> 2 ",binario_2)
        #print("Hijo Temporal 1")
        #print(binario_temporal)
        #print("Hijo Temporal 2")
        #print(binario_2)
       
        #print("--------------------------")
        poblacion[i]=decimal(binario_temporal)
        poblacion[int(ppc*cant_ini)+i]=decimal(binario_2)
        
    #print("*************************\n",int_num_mutaciones,"\n*********************")
    return poblacion


def seleccion(p_original,p_cruce,p_elite,p_original_2,p_cruce_2,p_elite_2):
    p_total=[int (j) for j in range(len(p_original)+len(p_cruce))]
    p_total2=[int (j) for j in range(len(p_original)+len(p_cruce))]
    
    p_selecionado=[int (j) for j in range(len(p_original))]
    p_selecionado2=[int (j) for j in range(len(p_original))]
    
    for i in range(len(p_original)):
        p_total[i]=p_original[i]
        
    for i in range(len(p_original)):
        p_total2[i]=p_original_2[i]
        
        
    for i in range(len(p_original),len(p_original)+len(p_cruce)):
        p_total[i]=p_cruce[i-len(p_original)]
        
    for i in range(len(p_original),len(p_original)+len(p_cruce)):
        p_total[i]=p_cruce_2[i-len(p_original)]
        
    reduced,reduced1=ordenar(p_total,p_total2,num_cromosoma)



    for e4 in range(len(p_elite)):
        p_selecionado[e4]=p_elite[e4]
        
    for i in range (len(p_original)-len(p_elite)):
        p_selecionado[i+len(p_elite)]=reduced[i]
    
    
    for e4 in range(len(p_elite)):
        p_selecionado2[e4]=p_elite_2[e4]
        
    for i in range (len(p_original)-len(p_elite)):
        p_selecionado2[i+len(p_elite)]=reduced1[i]
        
        
        
        
    return p_selecionado,p_selecionado2
        
#bucle
poblacion_final=[float(i) for i in range(len(poblacion_inicial))]
poblacion_final2=[float(i) for i in range(len(poblacion_inicial))]


#Mostrar cromosomas de población
print("Estructura cromosomica, población Inicial")
for a in range(cant_ini):
    print(poblacion_inicial[a],"->",binario(poblacion_inicial[a],num_cromosoma))
    
print("-------------------")
print("Estructura cromosomica, población Inicial  2")
for a in range(cant_ini):
    print(poblacion_inicial2[a],"->",binario(poblacion_inicial2[a],num_cromosoma))
    


for k in range(num_epocas):
    print("\n\nEPOCA ",k+1)
    poblacion_inicial,poblacion_inicial2=ordenar(poblacion_inicial,poblacion_inicial2,num_cromosoma)
    
    elit_4,elit_5=poblacion_elite(poblacion_inicial,poblacion_elite_por,poblacion_inicial2)
    
    
    print("Poblacion Elite")
    for e4 in range (len(elit_4)):
        print(elit_4[e4],"->",binario(elit_4[e4],num_cromosoma))
    print("----------------")
    print("Poblacion Elite2")
    for e4 in range (len(elit_4)):
        print(elit_5[e4],"->",binario(elit_5[e4],num_cromosoma))
    p=cruce(poblacion_inicial,ppc,num_cromosoma,pm,cant_ini)
    p2=cruce(poblacion_inicial2,ppc,num_cromosoma,pm,cant_ini)
    
    poblacion_inicial,poblacion_inicial2=seleccion(poblacion_inicial,p,elit_4,poblacion_inicial2,p2,elit_5)
    print("Poblacion Final")
    for c in range(len(poblacion_inicial)):
        print(poblacion_inicial[c],"->",binario(poblacion_inicial[c],num_cromosoma))
    print("---------------------------")
    print("Angulos minimizadores")
    print(poblacion_inicial)
    print("Valor de la funcion con los valores")
    for i in range(0,len(poblacion_inicial)):
        x_bina=[int(j) for j in range(num_cromosoma)]
        x_bina=binario(poblacion_inicial[i],num_cromosoma)
        x_real=[int(j) for j in range(num_cromosoma-1)]
        for jj in range(len(x_real)):
            x_real[jj]=x_bina[jj+1]
        
        x_r=decimal(x_real)
        if x_bina[0]==0:
            x_r=x_r*-1
        else:
            print("fuera de rango")
    
        y_bina=[int(j) for j in range(num_cromosoma)]
        y_bina=binario(poblacion_inicial2[i],num_cromosoma)
        y_real=[int(j) for j in range(num_cromosoma-1)]
        for jj in range(len(y_real)):
            y_real[jj]=y_bina[jj+1]
        
        y_r=decimal(y_real)
        
        if y_bina[0]==0:
            y_r=y_r*-1
        else:
            print("fuera de rango")
        
        x_r=x_r/1000
        y_r=y_r/1000
        
       
       
        print(x_r,y_r," ->  100*(x1^2-x2^2) + (1-x1)^2  ",funcion(poblacion_inicial[i],poblacion_inicial2[i],num_cromosoma))

