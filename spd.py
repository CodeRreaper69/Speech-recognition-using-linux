import os

print("WELCOME TO OFFLINE TEXT TO SPEECH RECOGNITION")
print("\n")
while True:
      n = input("""Enter the text to be spoken\n
(Enter underscore '_' instead of space e.g- "Hi_World") :\n
""")
      r = int(input("Enter Rate of speech (-100 to 100) : "))
      p = int(input("Enter pitch rate(-100 to 100) : "))
      os.system(f"spd-say {n} -r {r} -p {p}")
      c = input("Continue? (y/n):")
      if c in ["y","Y"]:
         pass
      else:
         exit()

