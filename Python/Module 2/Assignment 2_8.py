# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

def squirrel_play(num,is_status):
    if (num > 60 and num < 90) and is_status :
        print("If")
        return "True"
    elif (num > 60 and num < 100) and is_status:
        print("Elif")
        return "True"
    else:
        print("Else")
        return "False"

num = int(input("Enter temperature = "))
is_status = bool(input("Enter status = "))

result = squirrel_play(num,is_status)

print(str(result))
