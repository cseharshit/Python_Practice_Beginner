import calendar

def check_leap_year(year):
    '''
    Check if a year is leap or not.
    '''
    return calendar.isleap(year)

def get_calendar(year):
    '''
    Fetches calendar for a year.
    '''
    return calendar.calendar(year)

def get_calendar_for_month(year,month):
    '''
    Fetches calendar of a particular month of a particular year.
    '''
    return calendar.month(year, month)

#Driver Code
if __name__=='__main__':
    choice=0
    while choice!=4:
        choice=int(input("Enter the choice:\n1. Check for Leap Year\n2. Get Calendar for a year\n3. Get Calendar for a particular month of a year\n4. Exit\n"))
        if (choice==1):    
            print (check_leap_year(int(input("Check for leap year: "))),"\n\n\n")
        elif(choice==2):
            print(get_calendar(int(input("Enter year: "))),"\n\n\n")
        elif(choice==3):
            y, m =map(int,input("Enter year and month (YYYY MM): ").split())
            print(get_calendar_for_month(y,m),"\n\n\n")
        elif(choice==4):
            exit()
        else: print("Invalid choice! Try again")