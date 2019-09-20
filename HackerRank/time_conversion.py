s = input()

horas = int(s[:2])
tam = len(s) - 2

if s[-2] == 'P':
    if horas != 12:
        horas = horas+12
    resp = str(horas) + s[2:tam]
else:
    if horas < 10:
        horas = "0" + str(horas)
    elif horas == 12:
        horas = "00"
    resp = horas + s[2:tam]



print(resp)