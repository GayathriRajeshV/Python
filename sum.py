def speed(speed):
    if speed<=70:
        print("ok")
    elif speed>=70:
        point=(speed-70)//5
        print("you Have Got Demerit Point",point)
    if point>=12:
        print("Licience Suspended")
speed(650)
point=2

