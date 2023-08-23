fecha = input("Ingrese día y fecha en formato  dia, DD/MM : ")
print(fecha[0: fecha.find(",")])

dia_sem = fecha[0 : fecha.find(",")]
dia = int(fecha[fecha.find(" ")+1 : fecha.find("/")]) 
mes = int(fecha[fecha.find("/")+1 : ]) 
dia_sem = dia_sem.lower()

if dia_sem !="lunes" and dia_sem !="martes" and dia_sem !="miercoles" and dia_sem !="jueves" and dia_sem !="viernes" or dia>32  or mes >12:
    print("La fecha ingresada es incorrecta")
else:
    print("Fecha ingresada correctamente")
    if dia_sem == "lunes" or dia_sem=="martes" or dia_sem=="miercoles":
        hubo_examen = input("¿Hubo examen? SI/NO ")
        hubo_examen = hubo_examen.upper()
        if hubo_examen == "SI":
            aprobados = int(input("Cuantos alumnos aprobaron?: "))
            desaprobados = int(input("Cuantos desaprobaron?: "))
            porc_apro = aprobados /(aprobados+desaprobados)*100
            print(f"El porcentaje de aprobados es {porc_apro}%")
        else:
            print("No hubo examenes")
    elif dia_sem == "jueves":
        print("Hubo práctica hablada")
        asistencia= int(input("Indique el procentaje de asistencia : %"))
        if(asistencia > 50 ):
            print("Asistio la mayoria")
        else:
            print("no asistió la mayoría")
    else:
        if dia==1 and mes==1 or mes==7: 
            print("Inglés para viajeros")
            print("Comienzo de nuevo ciclo")
            alumnos = int(input("Ingrese la cantidad de alumnos: "))
            arancel = float(input("Indique el arrancel por alumno $"))
            ingre_total = alumnos*arancel
            print(f"El ingreso total correspondiente a {alumnos} alumnos es ${ingre_total}")
