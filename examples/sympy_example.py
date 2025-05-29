import sympy as sp  # Import Biblioteki SymPy z aliasem sp

# Tworzymy symbole matematyczne x, y, z
x, y, z = sp.symbols('x y z')

# Definiujemy wyrażenie symboliczne
expr = x**2 + 2*x + 1

# Wypisujemy wyrażenie
print("Wyrażenie:", expr)

# Upraszczamy wyrażenie
simplified = sp.simplify(expr)
print("Uproszczone:", simplified)

# Rozwijamy wyrażenie z potęgi
expanded = sp.expand(simplified)
print("Rozwinięte:", expanded)

# Liczymy pochodną wyrażenia względem x
derivative = sp.diff(expr, x)
print("Pochodna:", derivative)

# Całkujemy wyrażenie względem x (całka nieoznaczona)
integral = sp.integrate(expr, x)
print("Całka nieoznaczona:", integral)

# Całka oznaczona od 0 do 1
definite_integral = sp.integrate(expr, (x, 0, 1))
print("Całka oznaczona 0 do 1:", definite_integral)

# Rozwiązujemy równanie expr = 0 względem x
solutions = sp.solve(expr, x)
print("Rozwiązania równania:", solutions)

# Tworzymy macierz 2x2
A = sp.Matrix([[1, 2], [3, 4]])
print("Macierz A:")
sp.pprint(A)  # Ładny wydruk macierzy

# Obliczamy wyznacznik macierzy
det = A.det()
print("Wyznacznik macierzy A:", det)

# Obliczamy macierz odwrotną
A_inv = A.inv()
print("Odwrotność macierzy A:")
sp.pprint(A_inv)

# Obliczamy granicę sin(x)/x gdy x → 0
limit_expr = sp.limit(sp.sin(x)/x, x, 0)
print("Granica sin(x)/x gdy x->0:", limit_expr)

# Tworzymy rozwinięcie funkcji exp(x) w szereg Taylora do 4 rzędu
taylor = sp.series(sp.exp(x), x, 0, 5)
print("Szereg Taylora dla exp(x):")
print(taylor)

# Podstawiamy x=2 do wyrażenia
value = expr.subs(x, 2)
print("Wartość wyrażenia dla x=2:", value)

# Konwertujemy wynik na wartość numeryczną (float)
numeric = sp.N(value)
print("Wynik numeryczny:", numeric)

# Definiujemy wyrażenie trygonometryczne
trig_expr = sp.sin(x)**2 + sp.cos(x)**2

# Upraszczamy wyrażenie (tożsamość trygonometryczna)
simplified_trig = sp.simplify(trig_expr)
print("Uproszczenie sin^2(x) + cos^2(x):", simplified_trig)
