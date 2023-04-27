from equation import equation

def entry (coeff):
    try:
        response = input(f'{coeff} = ')
        number = float(response)
        return number
    except:
        print(f'Error. Expected a valid real number, got {response} instead')
        return entry(coeff)

def main():
    a, b, c = entry('a'), entry('b'), entry('c')
    if a:
        return equation(a, b, c)
    else:
        print('a cannot be 0')
        return main()