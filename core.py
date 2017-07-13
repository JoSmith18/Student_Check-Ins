from disk import loadcheckin, valid_student


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
    times = []
    for item in checkin:
        if  item[0] == day:
            times.append(item)
    return times

def check_student(student):
    checkin = loadcheckin()
    times = []
    for item in checkin:
        if  item[1] == student:
            times.append(item)
    return times
 
def verifystudents(name):
    return name in valid_student()
        
            