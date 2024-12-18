def initials(full_name):
    initial=""
    if (len(full_name) == 0):
        return
    first_middle_last = full_name.split(" ")
    for name in first_middle_last:
        initial=initial+name[0].upper()+"."
    return initial
                
full_name="Gayathri Rajesh Valiyaparambil"
print(f"Initals generated: {initials(full_name)}")
