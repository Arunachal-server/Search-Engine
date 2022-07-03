import json
import os

def authenticate(request):
    if(request["login"] == "admin" and request["password"] == "manojadmin"):
        return {"message": "success"}
    else:
        return {"message": "failure"}

def writeparameters(request):
    FILE_NAME="parameters.json"
    if os.path.exists(FILE_NAME):
        f=open(FILE_NAME,"r")
        data=json.load(f)
        if "secretkey" in data:
            secretkey=data["secretkey"]
            if "secretkey" in request:
                if(request["secretkey"] == secretkey):
                    f=open(FILE_NAME,"w")
                    json.dump(request,f)
                    return {"status": "request accepted, secret key matched, parameters updated"}
                else:
                    return {"status": "request accepted, secret key mismatched, parameters not updated"}
            else:
                return {"status": "request accepted, secret missing, parameters not updated"}
        else:
            with open(FILE_NAME, 'w+') as outfile:
                json.dump(request, outfile)
                return {"status": "success, parameters updated, secret key not present in existing file"}
    else:
        with open(FILE_NAME, 'w+') as outfile:
            json.dump(request, outfile)
        return {"status": "success, parameters created"}