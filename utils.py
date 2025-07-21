"""
Este archivo contiene utilidades comunes que se pueden usar en el proyecto  
"""
def time_to_minute(time : str )-> int:
    pass
    """converts a time string in the format HH:MM:SS to the total number of minutes.
        Args: time (str): a string representing time in the formt
        returns:
        int: the total number of minutes. if the input string is not in the correct 
        format wor cantains invalid numbers, the function will return 0
        
    """
    try:
        hours, minutes, seconds = map(int, time.split(':'))
        total_minutes = hours * 60 + minutes + seconds /60
        return round(total_minutes)
    except ValueError:
        return 0
    