A = {'dog', 'cat', 'fish', 'frog'}
B = {1, 2, 3, 4, 5, 6}

f = {('dog', 1), ('cat', 1), ('frog', 5), ('fish', 4)}

print('Domain A')
print(A)
print('Codomain B')
print(B)

print('Graph of the function')
print(f)

for element in f:
    print(element)

for element in f:
    print(element[0])

for element in f:
    print(element[1])


def is_injective(A, B, f):
    for element in f:
        b = element[1]
        for other in f:
            if other != element:
                bprime = other[1]
                if b == bprime:
                    return False
    return True


check1 = is_injective(A, B, f)
if check1:
    print('Function f is injective')
else:
    print('Function f is not injective')

f = {('dog', 1), ('cat', 2), ('frog', 5), ('fish', 4)}

check2 = is_injective(A, B, f)
if check2:
    print('Function f is injective')
else:
    print('Function f is not injective')
