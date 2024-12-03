def checkMail(email):
    user, domain = email.split("@")
    if email.find("@") != 1:
        return "ErrorF"

    if len(user)<3 or user.find(".")==2:
        return "ErrorU"
    for a in user:
        if a.isalnum()==False:
            return "ErrorU"
    if len(domain)<3  or  domain.find(".")==2:
        return "ErrorD"
    for a in user:
        if a.isalnum()==False:
            return "ErrorU"



    return "Valid"