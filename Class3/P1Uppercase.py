
text="CongRatUlations From Ram"

print(text.upper())                 #Convert to Uppercase
print(text.lower())                 #Convert to Lowercase
print(text.capitalize())            #1st letter caps            
print(text.title())                 #Each 1st word is Caps
t=str.maketrans("Ram","Har")            #Changing Letter,Maketrans()-Create Rules,Translate()-Apply Rules
results=text.translate(t)
print(results)             
