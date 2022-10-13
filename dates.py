from datetime import datetime, date

# Se puede instalar el módulo pytz para trabajar con zonas horarias
import pytz

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("México date:", mexico_date)

# Fecha de mi computadora con milisegundos
my_time = datetime.now()

# Fecha de mi computadora, desde esta variable se puede acceder al año, mes y día
my_day = date.today()


print(my_time)
print(my_day)
print(my_day.year)
print(my_day.month)
print(my_day.day)

# Dar formato a la fecha, se pueden ir cambiando los parámetros del método strftime
my_latam_date = my_time.strftime("%d/%m/%Y")
print("Latam", my_latam_date)