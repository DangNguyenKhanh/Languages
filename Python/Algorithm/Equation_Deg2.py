import math

def equation_deg_2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('Equation have many solutions...')
            else:
                print('Equation has no solutions')
        else:
            print('Equation have 1 solution:', -c / b)
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            print('Equation has no solutions')
        elif delta == 0:
            print('Equation have 1 solution:', -b/(2*a))
        else:
            print('Equation have 2 solutions:')
            print('x1:', (-b - math.sqrt(delta)) / (2 * a))
            print('x2:', (-b + math.sqrt(delta)) / (2 * a))
