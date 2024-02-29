hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.
hour_term = (hour + ((mins + dura)//60)) % 24
min_term = (mins + dura) % 60 

print("El evento termina a las " + str(hour_term) + ":" + str(min_term))