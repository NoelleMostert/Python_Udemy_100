while True:
    notes = []
    psw = input("Enter new password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("Password must contain a digit")
    if not any(i.isupper() for i in psw):
        notes.append("Password must contain a capital letter")
    if not len(psw) >= 5:
        notes.append("Password must be at least 5 characters long")
    if len(notes) == 0: 
        print("Password is fine")
        break
    else:
        for note in notes:
            print(note)