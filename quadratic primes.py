def is_prime(n): #returns true if n is prime otherwise false
    if n < 0:
        return False #debatable but works for this use case
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def get_primes(n): #returns the primes below n as an array
    primes = []
    for i in range(1, n):
        if is_prime(i):
            primes.append(i)
    return primes

#quadratics in the form of n^2+an+b are returned in the form [[a1, b1], [a2, b2], [a3, b3], ...]
#abs(a) < bound and abs(b) <= bound
#b is of course necessarily a prime number
def find_quadratics(bound):
    b_terms = get_primes(bound + 1)
    quadratics = []
    for a in range(-1 * bound + 1, bound):
        for b in b_terms:
            quadratics.append([a, b])
    return quadratics


#we compare each quadratic starting at n = 0, storing the "winner"
#the winner should be the one which returns the greatest number of subsequent primes
def compare_quadratics(quadratics):
    n = 0
    best_quadratic = []
    max_term = 0
    best_quadratic_max_term = 0
    output = 0
    for quadratic in quadratics:
        a, b = quadratic
        n = 0
        while True:
            output = n**2 + a*n + b
            if not is_prime(output):
                break
            n += 1
            if n >= best_quadratic_max_term:
                best_quadratic_max_term = n
                if best_quadratic != quadratic:
                    best_quadratic = quadratic
    return [best_quadratic, best_quadratic_max_term]



#This mess of if statements works so it doesn't matter that it's bad
upper_bound = input("This program finds quadratics in the form n^2 + an + b that generate primes\nenter the upper bound for abs(a, b): ")
if upper_bound.isdigit():
    upper_bound = int(upper_bound)
    print("\nGenerating...")
    solution = compare_quadratics(find_quadratics(upper_bound))
    best_quadratic = solution[0]
    max_term = solution[1]
    text = "\nThe best quadratic within the given bounds is n^2 "
    if best_quadratic[0] > 0:
        text += "+"
    elif best_quadratic[0] == 1:
        text += "n "
    elif best_quadratic[0] == -1:
        text += "-n"
    else:
        text += f"{best_quadratic[0]}n"
    if best_quadratic[1] < 0:
        text += " - "
    else:
        text += " + "
    text += str(best_quadratic[1])
    print(text + f" which generates {max_term} consecutive prime numbers")
else:
    print("Enter a whole number next time buckaroo")

input()