def equation_solver(a,b,c):
    discriminant = b**2 - (4*a*c)

    if discriminant > 0:
        root1 = (- b + (b**2 - (4*a*c))**(1/2))/(2*a)
        root2 = (- b - (b**2 - (4*a*c))**(1/2))/(2*a)
        return [root1, root2]
    elif discriminant == 0:
        root1 = - (b/(2*a))
        return [root1]
    elif discriminant < 0:
        return print("No real roots")

equation_solver(5,6,1)