import os

print("WELCOME TO OFFLINE TEXT TO SPEECH RECOGNITION")
print("\n")

while True:
    n = input("""Enter the text to be spoken
(Separated with spaces):\n
""")
    # Replacing spaces with underscores
    n = n.replace(" ", "_")

    r = int(input("Enter Rate of speech (-100 to 100) : "))
    p = int(input("Enter pitch rate(-100 to 100) : "))

    os.system(f"spd-say {n} -r {r} -p {p}")

    c = input("Continue? (y/n):")
    if c.lower() in ["y", "yes"]:
        pass
    else:
        exit()
