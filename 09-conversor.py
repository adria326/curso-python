temperatura =  float(input("ingrese temperatura:"))
escala = input("es fahrenheit(f) o es celsius(c)?:").lower()

if escala == "f":
    celsius =(temperatura - 32) * 5/9
    print(celsius)
elif escala == "c":
    fahrenheit = temperatura * 1.8 + 32
    print(fahrenheit)
else:
    print("escala incorrecta")