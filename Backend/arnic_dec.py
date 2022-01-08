vaa=" "
dato = " "
def arn_dec(respuesta_string):
    global vaa, dato, SSM
    if respuesta_string=='0':
        return('no_data','no_data')
    
    if len(respuesta_string) != 10:
        LB = 0
    else:
        r_bin2 = str(bin(int(respuesta_string)))
        r_bin = r_bin2[2:34]    
        if len(r_bin) == 31:
            r_bin = "0" + r_bin
        P = r_bin[0]
        SSM = r_bin[0:2]
        DATA = r_bin[3:22]
        SDI = r_bin[22:24]
        LABEL = r_bin[24:32]        
        LB = int(str(int(LABEL[0:2],2)) + str(int(LABEL[3:5],2)) + str(int(LABEL[5:8],2)))    
        #.print("Label: ",LB)
        
        # test 
        switch(LB,DATA)
        #print(dato)
        print(vaa)        
        return(LB,vaa)
        
        
def invertir_numero(n):
        numero = 0
        while n != 0:
            numero = 10*numero+n % 10
            n //= 10
        return numero

def switch(LB,DATA):        
            
    def Pitch_angle(): #324
        ## proceso
        global vaa, dato
        dato = "Pitch Angle Data: "        
        pdata = int(str(invertir_numero(int(DATA))),2)        
        vaa=str(pdata)

    def Roll_Angle(): #325
        ## proceso
        global vaa, dato
        dato = "Roll Angle Data: "
        pdata = int(str(invertir_numero(int(DATA))),2)        
        vaa=str(pdata)        

    def Altitude(): #203
        ## proceso
        global vaa, dato
        dato = "Altitude Data: "                                                   
        #data = "0011001"
        DATA2 =  DATA[1:18]    #"00101001001000011"
        fts = str(int(DATA2,2)) + " fts" 
        zsint = DATA[7:9]
        """
        if zsint == "00":
            print("No Vertical Rate (Level Flight)")
        elif zsint == "01":
            print("Climbing")
        elif zsint == "10":
            print("Desending")
        else:
            print("No data")  
            """   
        vaa=fts

    def Computed_Airspeed(): #206 
        ## proceso
        # ejemplo 425 knots - 0110101001
        #DATA = "0110101001"
        global vaa, dato   
        A1 = str(invertir_numero(int(DATA)))
        DATA2 = str(invertir_numero(int(A1))) 
        knots = str(int(DATA2,2)) + " knots"    
        dato = "Computed Airspeed Data: "        
        vaa=knots

    def True_Airspeed(): #210
        ## proceso
        # ejemplo 565 knots - 01000110101000
        global vaa, dato
        #DATA = "0100011010100000000"
        A1 = str(invertir_numero(int(DATA)))
        DATA2 = str(invertir_numero(int(A1)))
        knots = str(int(DATA2,2)) + " knots"
        dato =  "True Airspeed Data: "
        vaa=knots

    """def True_Airspeed2(): #230
        ## proceso 
        # ejemplo de dato: 
        global vaa, dato
        dato = "True Airspeed 2 Data: "     
        #DATA = '10101100101'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))                
        DATAA = float(D1+D2+D3)
        DATAA1 = str(DATAA)+' Knots'        
        #print(DATAA1)
        vaa=DATAA1"""

    def Total_Pressure(): #217
        ## proceso
        global vaa, dato
        dato = "Total Pressure Data: "
        DATA2 =  DATA[1:18]    #"00101001001000011"
        fts = str(int(DATA2,2)) + " Fts/min" 
        vaa=fts

    def Heading(): #314 - 14 y el 320 # OK 320
        ## proceso
        global vaa, dato
        dato = "Heading Data: "
        A1 = str(invertir_numero(int(DATA)))
        DATA2 = str(invertir_numero(int(A1)))
        grades = str(int(DATA2,2)) + " °"        
        vaa=grades

    def Vertical_speed(): #104
        ## proceso
        global vaa, dato, SSM
        DATA = "010001000000000"
        dato = "Vertical speed Data: "
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))                
        D4 = str(int(DATA[11:15],2))  
        if SSM == "11":
            DATAA = float("-"+D1+D2+D3+D4)
        else:
            DATAA = float(D1+D2+D3+D4)
        DATAA1 = str(DATAA)+' Ft/Min'        
        #print(DATAA1)
        vaa=DATAA1        

    def Hour():
        global vaa, dato
        dato = "Hour Data: "
#        DATA2 =  DATA[1:18]    #"00101001001000011"
#        hr = str(int(DATA2,2))         
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))                
        D4 = str(int(DATA[11:15],2))  
        if SSM == "11":
            DATAA = float("-"+D1+D2+D3+D4)
        else:
            DATAA = float(D1+D2+D3+D4)
        DATAA1 = str(DATAA)+' s'        

        vaa=DATAA1
    
    def Latitude():
        global vaa, datos
        dato = "Latitude: "
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))                
        D4 = str(int(DATA[11:15],2))  
        DATAA = float(D1+D2+D3+D4)   
        DATA3 = DATAA
        vaa=DATA3


    def default():
        global vaa, dato
        vaa = "no_data"
        dato = "no_data"
        pass

    dict = {        
        210 : True_Airspeed, #3758096520       OK -| USsAR ESTA
        325 : Roll_Angle, #3758670037          OK
        324 : Pitch_angle, #1616969940         OK        
        203 : Altitude, #1611935875            OK
        206 : Computed_Airspeed, #1610612870   OK
        217 : Total_Pressure,  # OK ,217, 255,257, preguntar | USAR 217 por ahora
        320 : Heading, # OK 320 - Probar ejemplos | %Magnetic % 14 y 320
        104 : Vertical_speed, # OK - Probar, pues tiene las 2 formas de decodificación
        125 : Hour, 
        310 : Latitude,#230 : True_Airspeed2, # OK             OK
        
        
        
#       125 : Hora ## falta  -- posición 


    }
    dict.get(LB,default)()

