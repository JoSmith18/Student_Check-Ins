from disk import loadcheckin


def check_day(checkin, day):
    '''
    >>> check_day([], '2017-07-12')
    []
    >>> check_day([['2017-07-12', 'name', 'time']], '2017-07-12')
    [['2017-07-12', 'name', 'time']]
    >>> check_day([['2017-07-12', 'name', 'time']], '2017-07-13')
    []
    >>> check_day([['2017-07-12', 'name', 'time'], ['2017-07-12', 'James', 'time']], '2017-07-12')
    [['2017-07-12', 'name', 'time'], ['2017-07-12', 'James', 'time']]
    >>> check_day([['2017-07-12', 'name', 'time'], ['2017-07-12', 'James', 'time'], ['2017-07-13', 'name', 'time']], '2017-07-12')
    [['2017-07-12', 'name', 'time'], ['2017-07-12', 'James', 'time']]
    '''
    times = ''
    for item in checkin:
        if  item[0] == day:
            times += ' - '.join(item) + '\n'
    return times

def check_student(checkin, student):
    """
    >>> check_student([], 'student')
    []
    >>> check_student([['2017-07-12', 'name', 'time']], 'name')
    [['2017-07-12', 'name', 'time']]
    >>> check_student([['2017-07-12', 'student', 'time']], 'name')
    []
    >>> check_student([['2017-07-12', 'name', 'time'], ['2017-07-13', 'name', 'time']], 'name')
    [['2017-07-12', 'name', 'time'], ['2017-07-13', 'name', 'time']]
    >>> check_student([['2017-07-12', 'name', 'time'], ['2017-07-12', 'James', 'time'], ['2017-07-13', 'name', 'time']], 'name')
    [['2017-07-12', 'name', 'time'], ['2017-07-13', 'name', 'time']]
    """
    times = ''
    for item in checkin:
        if  item[1] == student:
            times += ', '.join(item) + '\n'
    return times
 
def verifystudents(validstudent, name):
    """
    >>> verifystudents(['Asia Green', 'Tae', 'John'], 'Nate')
    False
    >>> verifystudents(['Asia Green', 'Tae'], 'Tae')
    True
    >>> verifystudents(['Trey'], 'trey')
    False
    >>> verifystudents(['Superman', 'Batman', 'Flash', 'Wonderwoman', 'Cyborg', 'Aquaman'], 'Hulk')
    False
    >>> verifystudents(['adf'], 'adf')
    True
    """
    if name in validstudent:
        return True
    else:
        return False


        
            