# Sydney Ani PID: 1869076
user_password = input()

# Replace characters based on the key
password_strength = user_password.replace('i', '!').replace('a', '@').replace('m', 'M').replace('B', '8').replace('o', '.')

# Append "q*s" to the end
strong_password = password_strength + 'q*s'

print(strong_password)
