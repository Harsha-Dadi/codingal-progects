CAMERA = 1
MICROPHONE = 2
STORAGE = 4
LOCATION = 8

Allowed_apps= ["codingal app","math app","science app","reading app"]
restricted_apps= ["gaming app","shopping app","social media app"]

student_name=input("Enter your name: ").lower()
requested_app=input("Enter your requested app: ").lower()

print("-----Identity operator check-----")

if type(student_name) is str:
    print("the students name is stored as a text")

if type(requested_app) is not int:
    print("the requested app is not stored as a number")

print("-----Membership operators check-----")

if requested_app in Allowed_apps:
    print(requested_app,"is an approved student app")
else:
    print(requested_app,"is not and approved app")

if requested_app not in restricted_apps:
    print(requested_app,"is not in the restricted list")
else:
    print("Access denied because app is restricted")

print("-----App Permission Settings-----")

student_permissions=CAMERA|MICROPHONE|STORAGE
print("Permission Values:",student_permissions)
print("Permission Bits:", bin(student_permissions))

if student_permissions & CAMERA:
    print("Camera permission:Enabled")
if student_permissions & MICROPHONE:
    print("Microphone permission:Enabled")
if student_permissions & STORAGE:
    print("Storage permission:Enabled")
if student_permissions & LOCATION:
    print("Location permission:Enabled")
else:
    print("Location permission:Disabled")

print("-----Bit shift demontration-----")
next_permission=CAMERA << 1

print("Camera bit:",bin(CAMERA))
print("After left shift:",bin(next_permission))

previous_permission=STORAGE >> 1

print("Storage bit:",bin(STORAGE))
print("After right shift:",bin(previous_permission))

print("-----Final Access result-----")

if requested_app in Allowed_apps and requested_app not in restricted_apps:
    print("Access Granted to", requested_app)
else:
    print("Access Denied to ",requested_app)