from scipy import optimize
def f(x):
  return (x**2 - 1)  # only one real root at x = 1
sol = optimize.brentq(f,a=0,b=3)
print sol
