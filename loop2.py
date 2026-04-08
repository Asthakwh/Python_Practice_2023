correct_password = input("Enter password you want to save:")
#correct_password = "python123"
attempts = 3
print("check your pasword")
while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left.")
else:  # Runs if loop completes without 'break'
    print("Account locked!")