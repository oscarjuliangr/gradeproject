vaa=" "
def arn_dec(respuesta_string):
    global vaa
    if len(respuesta_string) != 10:
        LB = 0
    else:
        r_bin2 = str(bin(int(respuesta_string)))
        r_bin = r_bin2[2:34]
        #.print("Cadena binaria: ")
        #.print(r_bin)
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
        return(LB,vaa)
        
        
def invertir_numero(n):
        numero = 0
        while n != 0:
            numero = 10*numero+n % 10
            n //= 10
        return numero

def switch(LB,DATA):        

    def Magnetic_Heading(): #14
        ## proceso
        global vaa
        print("Magnetic Heading Data: ")
        p = int(DATA,2)
        #.print(p)
        p1 = len(DATA)
        #.print(p1)
        vaa=str(p)
        
    
    def Magnetic_Heading2(): #320
        ## proceso
        global vaa
        print("Magnetic Heading Data: ")
        vaa='no_data'
            
    def Pitch_angle(): #324
        ## proceso
        global vaa
        print("Pitch Angle Data: ")
        #.print(int(DATA))
        pdata = int(str(invertir_numero(int(DATA))),2)
        #.print(pdata)
        vaa=str(pdata)

    def Roll_Angle(): #325
        ## proceso
        global vaa
        print("Roll Angle Data: ")
        vaa="no_data"

    def Body_Pitch_Rate(): #326
        ## proceso
        global vaa
        print("Body Pitch Rate Data: ")
        vaa="no_data"

    def Body_Roll_Rate(): # 327
        ## proceso
        global vaa
        print("Body Roll Rate Data: ")
        vaa="no_data"

    def Body_Yaw_Rate(): # 330
        ## proceso
        global vaa
        print("Body Yaw Rate Data: ")
        vaa="no_data"

    def Body_Longitudinal_Acceleration(): #331
        ## proceso
        global vaa
        print("Body Longitudinal Acceleration Data: ")
        vaa="no_data"

    def Body_Lateral_Acceleration(): #332
        ## proceso
        global vaa
        print("Body Lateral Acceleration Data: ")
        vaa="no_data"

    def Body_Normal_Acceleration(): #333
        ## proceso
        global vaa
        print("Body Normal Acceleration Data: ")
        vaa="no_data"

    def Inertial_Pitch_Rate(): #336
        ## proceso
        global vaa
        print("Inertial Pitch Rate Data: ")
        vaa="no_data"

    def Inertial_Roll_Rate(): #337
        ## proceso
        global vaa
        print("Inertial Roll Rate Data: ")
        vaa="no_data"

    def Inertial_Yaw_Rate(): #340
        ## proceso
        global vaa
        print("Inertial Yaw Rate Data: ")
        vaa="no_data"

    def Vertical_Acceleration(): #364
        ## proceso
        global vaa
        print("Vertical Acceleration Data: ")
        vaa="no_data"

    def Along_Heading_Acceleration(): #375
        ## proceso
        global vaa
        print("Along Heading Acceleration Data: ")
        vaa="no_data"

    def Cross_Heading_Acceleration(): #376
        ## proceso
        global vaa
        print("Cross Heading Acceleration Data: ")
        vaa="no_data"

    def Altitude(): #203
        ## proceso
        global vaa
        print("Altitude Data: ")                                            
        #.print(DATA)
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
        #.print(fts)
        vaa=fts

    def Baro_Corrected(): #204
        ## proceso
        global vaa
        print("Baro Corrected Data: ")
        vaa="no_data"

    def Mach(): #205
        ## proceso
        global vaa
        print("Mach Data: ")
        vaa="no_data"

    def Computed_Airspeed(): #206
        ## proceso
        global vaa
        print("Computed Airspeed Data: ")
        vaa="no_data"

    def Max_Allowable_Airspeed(): #207
        ## proceso
        global vaa
        print("Max. Allowable Airspeed Data: ")
        vaa="no_data"

    def True_Airspeed(): #210
        ## proceso
        global vaa
        print("True Airspeed Data: ")
        vaa="no_data"
                                            
    def Total_Air_Temp(): #211
        ## proceso
        global vaa
        print("Total Air Temp Data: ")
        vaa="no_data"

    def Altitude_Rate(): #212
        ## proceso
        global vaa
        print("Altitude Rate Data: ")
        vaa="no_data"

    def Impacted_Pressure(): #215
        ## proceso
        global vaa
        print("Impacted Pressure Data: ")
        vaa="no_data"

    def Static_Pressure(): #217
        ## proceso
        global vaa
        print("Static Pressure Data: ")
        vaa="no_data"

    def Baro_corrected_altitude(): #220
        ## proceso
        global vaa
        print("Baro corrected altitude Data: ")
        vaa="no_data"
        

    def True_Airspeed2(): #230
        ## proceso
        global vaa
        print("True Airspeed 2 Data: ")      
        #DATA = '10101100101'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))                
        DATAA = float(D1+D2+D3)
        DATAA1 = str(DATAA)+' Knots'        
        print(DATAA1)
        vaa=DATAA1

    def Total_Air_Temp(): #231
        ## proceso
        global vaa
        print("Total Air Temp Data: ") 
        DATA = '00000100101'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))                
        DATAA = float(D1+D2+D3)
        DATAA1 = str(DATAA)+' Dec. C'        
        print(DATAA1)
        vaa=DATAA1

    def Static_Air_Temp(): #233
        ## proceso
        global vaa
        print("Static Air Temp Data: ")
        vaa="no_data"

    def Corrected_Angle_of_Attack(): #241
        ## proceso
        global vaa
        print("Corrected Angle of AttackData: ")
        vaa="no_data"

    def Total_Pressure(): #242
        ## proceso
        global vaa
        print("Total Pressure Data: ")
        vaa="no_data"

    def Distance_to_go_Data(): #1
        ## proceso
        global vaa
        print("Distance to go Data: ") 
        #DATA = '0100111010100000100'
        D1 = str(int(DATA[0:3],2))    
        D2 = str(int(DATA[3:7],2))        
        D3 = str(int(DATA[7:11],2))        
        D4 = str(int(DATA[11:15],2))        
        D5 = str(int(DATA[15:19],2))        
        DATAA = float(D1+D2+D3+D4+'.'+D5)
        DATAA1 = str(DATAA)+' NM'        
        #.print(DATAA1)
        vaa=DATAA1
    def Time_to_go_Data(): #2
        ## proceso
        global vaa
        print("Time to go Data: ") 
        #DATA = '001010001010011'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))        
        D4 = str(int(DATA[11:15],2))
        DATAA = float(D1+D2+D3+'.'+D4)
        DATAA1 = str(DATAA)+' Min'        
        #.print(DATAA1)
        vaa=DATAA1

    def Ground_Speed(): #12
        ## proceso
        global vaa
        print("Ground Speed Data: ") 
        DATA = '00001100101000'
        D1 = str(int(DATA[0:3],2))
        D2 = str(int(DATA[3:7],2))
        D3 = str(int(DATA[7:11],2))        
        D4 = str(int(DATA[11:15],2))
        DATAA = float(D1+D2+D3+D4)
        DATAA1 = str(DATAA)+' Knots'        
        #.print(DATAA1)
        vaa=DATAA1

    def Selected_Course(): #100
        ## proceso
        global vaa
        print("Selected Course Data: ")
        vaa="no_data"

    def Desired_Track(): #114
        ## proceso
        global vaa
        print("Desired Track Data: ")
        vaa="no_data"

    def Cross_Track(): #116
        ## proceso
        global vaa
        print("Cross Track Data: ")
        vaa="no_data"

    def Horizontal_Command_Signal(): #121
        ## proceso
        global vaa
        print("Horizontal Command Signal Data: ")
        vaa="no_data"

    def Universal_Time_Coordinate(): #125
        ## proceso
        global vaa
        print("Universal Time Coordinate Data: ")    
        #DATA = '0010101010001010101'
        D1 = str(int(DATA[0:3],2))    
        D2 = str(int(DATA[3:7],2))        
        D3 = str(int(DATA[7:11],2))        
        D4 = str(int(DATA[11:15],2))        
        D5 = str(int(DATA[15:19],2))        
        DATAA = float(D1+D2+D3+D4+'.'+D5)
        DATAA1 = str(DATAA)+' Hr'        
        #.print(DATAA1)
        vaa=DATAA1

    def Distance_to_go(): #251
        ## proceso
        global vaa
        print("Distance to go Data: ")
        vaa="no_data"

    def Time_to_go(): #252
        ## proceso
        global vaa
        print("Time to go Data: ")
        vaa="no_data"

    def Present_Position_Latitude(): #310
        ## proceso
        global vaa
        print("Present Position Latitude Data: ")
        vaa="no_data"

    def Present_Position_Longitude(): #311
        ## proceso
        global vaa
        print("Present Position Longitude Data: ")
        vaa="no_data"

    def Selected_Course(): #312
        ## proceso
        global vaa
        print("Ground Speed Data: ")
        vaa="no_data"

    def Track_Angle_True(): #313
        ## proceso
        global vaa
        print("Track Angle - True Data: ")
        vaa="no_data"

    def Wind_Speed(): #315
        ## proceso
        global vaa
        print("Wind Speed Data: ")
        vaa="no_data"

    def Wind_Direction_True(): #316
        ## proceso
        global vaa
        print("Wind Direction Data: ")
        vaa="no_data"

    def Drift_Angle(): #321
        ## proceso
        global vaa
        print("Drift Angle Data: ")
        vaa="no_data"

    def default():
        global vaa
        vaa="no_data"
        pass

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
    


