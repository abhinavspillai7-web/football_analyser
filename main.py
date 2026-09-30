import validation
while True:
    inp1=input("enter team formation(format:defenders–midfielders–forwards):")
    inp1=inp1.strip()
    result=validation.validate_formations(inp1)
    if result==True:
        print("valid formation")
        break
    else:
        print("invalid formation")
