def checkEmail(email):

    if email.count('@') != 1:
        return "ErrorF"


    user, domain = email.split('@')


    if len(user) < 3:
        return "ErrorU"
    if ".." in user or not all(c.isalnum() or c == '.' for c in user):
        return "ErrorU"


    if len(domain) < 3:
        return "ErrorD"
    if ".." in domain or not all(c.isalnum() or c == '.' for c in domain):
        return "ErrorD"

    return "Valid"

