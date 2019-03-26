def cubeRoot(x):
    guess = None
    for i in range(abs(x)):
        if i**3 >= abs(x):
            guess = i
            break
    if guess**3 > abs(x):
        return None
    else:
        if x < 0:
            guess = -guess
    return guess

def approximateCube(x):
    guess, epsilon, increment = 0.0, 0.1, 0.01
    while abs(guess**3-x) > epsilon and (guess < x):
        guess += increment
    if abs(guess**3-x) > epsilon:
        return None
    else:
        return guess

print(cubeRoot(-27))
print(approximateCube(27))
