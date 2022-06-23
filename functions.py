def authenticate(request):
    if(request["login"] == "admin" and request["password"] == "manojadmin"):
        return {"message": "success"}
    else:
        return {"message": "failure"}

