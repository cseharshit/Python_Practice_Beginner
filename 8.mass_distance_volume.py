def calculate_mass():
    d,v= map(float,input("Enter Density and Volume: ").split())
    return d*v  

def calculate_density():
    m,v= map(float,input("Enter Mass and Volume: ").split())
    return m/v

def calculate_volume():
    m,d= map(float,input("Enter Mass and Density: ").split())
    return m/d

if __name__=='__main__':
    choice=input("What would you like to calculate - \nm/M for Mass\nd/D for Density\nv/V for Volume\n")
    if choice in 'mM':
        print(calculate_mass())
    elif choice in 'dD':
        print(calculate_density())
    elif choice in 'vV':
        print(calculate_volume())
    else:
        print('Invalid Choice')