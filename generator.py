from random import choice

characters = ["a","b","ç","c","d","e","f","g","ğ","h","i","ı","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","w","x","A","B","C","Ç","D","E","F","G","Ğ","H","İ","I","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","W","X","0","1","2","3","4","5","6","7","8","9","!","-","_","?","=","*","'","$","#",".",",","@","+","/","<",">","(",")","½","£","%","|"]

print ("How Many Characters Should Your Password Be : ")
passwordlength = int(input())

password = ""

for i in range(passwordlength):
    password += str(choice(characters))

print(password)
