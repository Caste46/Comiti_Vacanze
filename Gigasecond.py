from datetime import timedelta
gigasecond = timedelta(seconds = 10 ** 9)
def add(date):
    '''
    Restituisce una data a un gigasecondo dalla data indicata
    '''
    return date + gigasecond
    
