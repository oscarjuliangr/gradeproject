vaa=" "
dato = " "
def arn_dec(respuesta_string):
    global vaa, dato
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
        switch(LB,DATA)
        print(dato)
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
        vaa="no_data"

    def Altitude(): #203
        ## proceso
        global vaa, dato
        dato = "Altitude Data: "                                                   
        data = "0011001"
        fts = str(int(data,2)*100) + " fts" 
        zsint = DATA[7:9]
        if zsint == "00":
            print("No Vertical Rate (Level Flight)")
        elif zsint == "01":
            print("Climbing")
        elif zsint == "10":
            print("Desending")
        else:
            print("No data")        
        vaa=fts

    def Computed_Airspeed(): #206
        ## proceso
        global vaa, dato
        dato = "Computed Airspeed Data: "
        vaa="no_data"

    def True_Airspeed(): #210
        ## proceso
        global vaa, dato
        dato =  "True Airspeed Data: "
        vaa="no_data"

    def True_Airspeed2(): #230
        ## proceso
        global vaa, dato
        dato = "True Airspeed 2 Data: "     
        #DATA = '10101100101'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))                
        DATAA = float(D1+D2+D3)
        DATAA1 = str(DATAA)+' Knots'        
        print(DATAA1)
        vaa=DATAA1

    def Total_Pressure(): #242
        ## proceso
        global vaa, dato
        dato = "Total Pressure Data: "
        vaa="no_data"

    def default():
        global vaa, dato
        vaa = "no_data"
        dato = "no_data"
        pass

    dict = {        
        324 : Pitch_angle,
        325 : Roll_Angle,
        203 : Altitude,
        206 : Computed_Airspeed,
        210 : True_Airspeed,
        230 : True_Airspeed2, #OK
        242 : Total_Pressure,
        #314 : Heading,
        #360 : Vertical_speed,
    }
    dict.get(LB,default)()
    


