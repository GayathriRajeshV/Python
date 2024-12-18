def check_speed():
    speed=int(intput("Enter the speed="))
    if speed <=70:
        print("OK")
    elif speed >=70:
        point=(speed-70)//5
    if point >12:
        print("License suspended")
check_speed()
