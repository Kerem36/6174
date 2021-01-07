num = int(input("Enter a 4 digit number: "))
def sort(n):
    ns = []
    while n:
        ns.append(n%10)
        n //= 10
    n1, n2 = 0, 0
    i = 0
    while len(ns):
        n1 += max(ns)*10**(3-i)
        n2 += max(ns)*10**i
        ns.remove(max(ns))
        i += 1
    return n1, n2
def solve(n):
    n1, n2 = sort(n)
    nn = n1-n2
    yield f"{n1} - {n2} = {nn}"
    if nn < 1000:
        nn *= 10
    yield from solve(nn)
f = solve(num)
last = None
while True:
    new = next(f)
    print(new)
    if new.split()[-1] == last:
        break
    last = new.split()[-1]
