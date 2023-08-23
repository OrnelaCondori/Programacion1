fecha = input("Ingrese día y fecha en formato  dia, DD/MM : ")
print(fecha[0: fecha.find(",")])

dia_sem = fecha[0 : fecha.find(",")]
dia = fecha[fecha.find(" ")+1 : fecha.find("/")]
mes = fecha[fecha.find("/")+1 : ]
dia_sem = dia_sem.lower()
print (dia_sem)

if(((dia_sem !="lunes") and (dia_sem !="martes") and (dia_sem !="miercoles") and (dia_sem !="jueves") and (dia_sem !="viernes")) or( dia>32 ) or (mes >12)):
    print("La fecha ingresada es incorrecta, vefifique que el día ingresado no sea fin de semana ni mayor a 31, o que el mes no sea mayor a 12")
else:
    print("Fecha ingresada correctamente")
    if (dia_sem == "lunes" or dia_sem=="martes" or dia_sem=="miercoles"):
        hubo_examen = print ("¿Hubo examen? para SI ingrese 1 , para NO ingrese 2")
        if (hubo_examen == "1"):
            aprobados = int(input("Cuantos alumnos aprobaron: "))
            desaprobados = int(input("Cuantos desaprobaron: "))
            porc_apro = aprobados /(aprobados+desaprobados)*100
            print(f"El porcentaje de aprobados es {porc_apro}%")
        else:
            print("No hubo examenes")
    elif (dia_sem == "jueves"):
        asistencia= print("Indique el procentaje de asistencia (sin porcentaje): ")
        if(asistencia >50 ):
            print("Asistio la mayoria")
        else:
            
    else:
        print("falta lo del viernes")
        