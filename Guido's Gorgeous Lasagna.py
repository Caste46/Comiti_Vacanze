EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(min):
    """Calculate the bake time remaining.
 
   Function that takes the actual minutes the lasagna has been in the oven as
   an argument and returns how many minutes the lasagna still needs to bake
   based on the `EXPECTED_BAKE_TIME`.
   """
    return EXPECTED_BAKE_TIME - min
    
def preparation_time_in_minutes(num_stra):
    """Calculate the preparation time.
 
    This function takes an integer representing the number of layers added to the dish,
    calculating preparation time using a time of 2 minutes per layer added.
    """
    return num_stra * PREPARATION_TIME
    
def elapsed_time_in_minutes(num_stra, min):
    """Calculate the elapsed time.
 
    This function takes two integers representing the number of lasagna layers and the time already spent baking
     and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(num_stra) + min
