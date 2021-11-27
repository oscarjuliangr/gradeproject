#import serial
#puerto = "COM1" # tipico en windows X= un entero positivo
#baudrate = 57600 #(o el baudrate adecuado/usado en putty)
#ser = serial.Serial(port=puerto, baudrate=baudrate)
#respuesta_bytes = ser.read(11) # si sabes la cantidad de bytes recibidos, puedes especificarlo dentro de los parentesis.
# Transforma los bytes en string
#respuesta_string = respuesta_bytes.decode('utf-8')
#print(respuesta_string)

################# # trama a analizar: 3764437204


respuesta_string = int('3764437204')
if len(str(respuesta_string)) != 10:
    print("Error de digito")
    LB = 0
else:
    r_bin2 = str(bin(respuesta_string))
    r_bin = r_bin2[2:34]
    print("Cadena binaria: ")
    print(r_bin)
    if len(r_bin) == 31:
        r_bin = "0" + r_bin
        
    P = r_bin[0]
    SSM = r_bin[0:2]
    DATA = r_bin[3:22]
    SDI = r_bin[22:24]
    LABEL = r_bin[24:32]        
    LB = int(str(int(LABEL[0:2],2)) + str(int(LABEL[3:5],2)) + str(int(LABEL[5:8],2)))    

    def invertir_numero(n):
        numero = 0
        while n != 0:
            numero = 10*numero+n % 10
            n //= 10
        return numero
    print("Label: ")
    LB = 231
    print(LB)


def switch():        

    def Magnetic_Heading(): #14
        ## proceso

        print("Magnetic Heading Data: ")
        p = int(DATA,2)
        print(p)
        p1 = len(DATA)
        print(p1)
        
    def Magnetic_Heading2(): #320
        ## proceso
        print("Magnetic Heading Data: ")
            
    def Pitch_angle(): #324
        ## proceso
        print("Pitch Angle Data: ")
        print(int(DATA))
        pdata = int(str(invertir_numero(int(DATA))),2)
        print(pdata)

    def Roll_Angle(): #325
        ## proceso
        print("Roll Angle Data: ")

    def Body_Pitch_Rate(): #326
        ## proceso
        print("Body Pitch Rate Data: ")

    def Body_Roll_Rate(): # 327
        ## proceso
        print("Body Roll Rate Data: ")

    def Body_Yaw_Rate(): # 330
        ## proceso
        print("Body Yaw Rate Data: ")

    def Body_Longitudinal_Acceleration(): #331
        ## proceso
        print("Body Longitudinal Acceleration Data: ")                                

    def Body_Lateral_Acceleration(): #332
        ## proceso
        print("Body Lateral Acceleration Data: ")  

    def Body_Normal_Acceleration(): #333
        ## proceso
        print("Body Normal Acceleration Data: ")    

    def Inertial_Pitch_Rate(): #336
        ## proceso
        print("Inertial Pitch Rate Data: ")    

    def Inertial_Roll_Rate(): #337
        ## proceso
        print("Inertial Roll Rate Data: ")    

    def Inertial_Yaw_Rate(): #340
        ## proceso
        print("Inertial Yaw Rate Data: ")    

    def Vertical_Acceleration(): #364
        ## proceso
        print("Vertical Acceleration Data: ")    

    def Along_Heading_Acceleration(): #375
        ## proceso
        print("Along Heading Acceleration Data: ")    

    def Cross_Heading_Acceleration(): #376
        ## proceso
        print("Cross Heading Acceleration Data: ")    

    def Altitude(): #203
        ## proceso        
        print("Altitude Data: ")                                            
        print(DATA)
        # data = DATA[0:6]
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
        return fts,data

    def Baro_Corrected(): #204
        ## proceso
        print("Baro Corrected Data: ") 

    def Mach(): #205
        ## proceso
        print("Mach Data: ") 

    def Computed_Airspeed(): #206
        ## proceso
        print("Computed Airspeed Data: ") 

    def Max_Allowable_Airspeed(): #207
        ## proceso
        print("Max. Allowable Airspeed Data: ") 

    def True_Airspeed(): #210
        ## proceso
        print("True Airspeed Data: ") 
                                            
    def Total_Air_Temp(): #211
        ## proceso
        print("Total Air Temp Data: ") 

    def Altitude_Rate(): #212
        ## proceso
        print("Altitude Rate Data: ") 

    def Impacted_Pressure(): #215
        ## proceso
        print("Impacted Pressure Data: ") 

    def Static_Pressure(): #217
        ## proceso
        print("Static Pressure Data: ") 

    def Baro_corrected_altitude(): #220
        ## proceso
        print("Baro corrected altitude Data: ") 
        

    def True_Airspeed2(): #230
        ## proceso
        print("True Airspeed 2 Data: ")      
        #DATA = '10101100101'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))                
        DATAA = float(D1+D2+D3)
        DATAA1 = str(DATAA)+' Knots'        
        print(DATAA1)                                           

    def Total_Air_Temp(): #231
        ## proceso
        print("Total Air Temp Data: ") 
        DATA = '00000100101'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))                
        DATAA = float(D1+D2+D3)
        DATAA1 = str(DATAA)+' Dec. C'        
        print(DATAA1)          

    def Static_Air_Temp(): #233
        ## proceso
        print("Static Air Temp Data: ") 

    def Corrected_Angle_of_Attack(): #241
        ## proceso
        print("Corrected Angle of AttackData: ") 

    def Total_Pressure(): #242
        ## proceso
        print("Total Pressure Data: ") 

    def Distance_to_go_Data(): #1
        ## proceso        
        print("Distance to go Data: ") 
        #DATA = '0100111010100000100'
        D1 = str(int(DATA[0:3],2))    
        D2 = str(int(DATA[3:7],2))        
        D3 = str(int(DATA[7:11],2))        
        D4 = str(int(DATA[11:15],2))        
        D5 = str(int(DATA[15:19],2))        
        DATAA = float(D1+D2+D3+D4+'.'+D5)
        DATAA1 = str(DATAA)+' NM'        
        print(DATAA1)
        
    def Time_to_go_Data(): #2
        ## proceso
        print("Time to go Data: ") 
        #DATA = '001010001010011'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))        
        D4 = str(int(DATA[11:15],2))
        DATAA = float(D1+D2+D3+'.'+D4)
        DATAA1 = str(DATAA)+' Min'        
        print(DATAA1)

    def Ground_Speed(): #12
        ## proceso
        print("Ground Speed Data: ") 
        DATA = '00001100101000'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))        
        D4 = str(int(DATA[11:15],2))
        DATAA = float(D1+D2+D3+D4)
        DATAA1 = str(DATAA)+' Knots'        
        print(DATAA1)        

    def Selected_Course(): #100
        ## proceso
        print("Selected Course Data: ") 

    def Desired_Track(): #114
        ## proceso
        print("Desired Track Data: ") 

    def Cross_Track(): #116
        ## proceso
        print("Cross Track Data: ") 

    def Horizontal_Command_Signal(): #121
        ## proceso
        print("Horizontal Command Signal Data: ")       

    def Universal_Time_Coordinate(): #125
        ## proceso
        print("Universal Time Coordinate Data: ")    
        #DATA = '0010101010001010101'
        D1 = str(int(DATA[0:3],2))    
        D2 = str(int(DATA[3:7],2))        
        D3 = str(int(DATA[7:11],2))        
        D4 = str(int(DATA[11:15],2))        
        D5 = str(int(DATA[15:19],2))        
        DATAA = float(D1+D2+D3+D4+'.'+D5)
        DATAA1 = str(DATAA)+' Hr'        
        print(DATAA1)      

    def Distance_to_go(): #251
        ## proceso
        print("Distance to go Data: ")    

    def Time_to_go(): #252
        ## proceso
        print("Time to go Data: ")    

    def Present_Position_Latitude(): #310
        ## proceso
        print("Present Position Latitude Data: ")    

    def Present_Position_Longitude(): #311
        ## proceso
        print("Present Position Longitude Data: ")    

    def Selected_Course(): #312
        ## proceso
        print("Ground Speed Data: ")    

    def Track_Angle_True(): #313
        ## proceso
        print("Track Angle - True Data: ")   

    def Wind_Speed(): #315
        ## proceso
        print("Wind Speed Data: ")   

    def Wind_Direction_True(): #316
        ## proceso
        print("Wind Direction Data: ")   

    def Drift_Angle(): #321
        ## proceso
        print("Drift Angle Data: ")                                                                                     

    def default():    
        print("LABEL no encontrado")

    dict = {
        14  : Magnetic_Heading, #OK
        320 : Magnetic_Heading,
        324 : Pitch_angle,
        325 : Roll_Angle,
        326 : Body_Pitch_Rate,
        327 : Body_Roll_Rate,
        330 : Body_Yaw_Rate,
        331 : Body_Longitudinal_Acceleration,
        332 : Body_Lateral_Acceleration,
        333 : Body_Normal_Acceleration,
        336 : Inertial_Pitch_Rate,
        337 : Inertial_Roll_Rate,
        340 : Inertial_Yaw_Rate,
        364 : Vertical_Acceleration,
        375 : Along_Heading_Acceleration,
        376 : Cross_Heading_Acceleration,
        203 : Altitude,
        204 : Baro_Corrected,
        205 : Mach,
        206 : Computed_Airspeed,
        207 : Max_Allowable_Airspeed,
        210 : True_Airspeed,
        211 : Total_Air_Temp,
        212 : Altitude_Rate,
        215 : Impacted_Pressure,
        217 : Static_Pressure, 
        220 : Baro_corrected_altitude, 
        230 : True_Airspeed2, #OK
        231 : Total_Air_Temp, #OK
        233 : Static_Air_Temp,
        241 : Corrected_Angle_of_Attack,
        242 : Total_Pressure,
        1   : Distance_to_go_Data, #OK
        2   : Time_to_go_Data, #OK
        12  : Ground_Speed,
        100 : Selected_Course,
        114 : Desired_Track,
        116 : Cross_Track,
        121 : Horizontal_Command_Signal,
        125 : Universal_Time_Coordinate, #OK
        251 : Distance_to_go,
        252 : Time_to_go,
        310 : Present_Position_Latitude,
        311 : Present_Position_Longitude,
        312 : Ground_Speed,
        313 : Track_Angle_True,
        315 : Wind_Speed,
        316 : Wind_Direction_True,
        321 : Drift_Angle
        

    }
    dict.get(LB,default)()
switch()



