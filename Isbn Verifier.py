def is_valid(isbn):
    isbn = isbn.replace("-", "")
    isbn = isbn.replace("X", "10")
    
    if(isbn.isdigit() == False or len(isbn) < 10):
        return False
    check = (int(isbn[0]) * 10 + int(isbn[1]) * 9 + int(isbn[2]) * 8 + 
            int(isbn[3]) * 7 + int(isbn[4]) * 6 + int(isbn[5]) * 5 + 
            int(isbn[6]) * 4 + int(isbn[7]) * 3 + int(isbn[8]) * 2 + 
            int(isbn[9:]) * 1)
    if(check % 11 == 0):
        return True
    else:
        return False