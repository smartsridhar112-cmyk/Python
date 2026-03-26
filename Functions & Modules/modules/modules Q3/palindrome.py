def is_palindrone(value):
    s=str(value)
    s=s.replace("","").lower()
    return s==s[::-1]
