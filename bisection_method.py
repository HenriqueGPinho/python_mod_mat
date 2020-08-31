# from __future__ import division


# def funcao(x0):
#   return x0**4 - 3*x0**3 + 3

# def bis(a, b, tol, n): # interval [a,b], tolerance, max number of iterations
#   f0 = funcao(a)
#   f1 = funcao(b)
#   i = 1

#   while ((abs(funcao(a)) > tol) and (abs(funcao(b)) > tol) and (i <= n)):
#     if (abs(a - b) < tol):
#       root = (a + b)/2
#       average = (a + b)/2
#       f2 = funcao(average)

#       if (f0*f2 < 0):
#         b = average
#         f1 = funcao(average)
#       else:
#         a = average
#         f0 = funcao(average)

#       i = i + 1

#       if (i > n):
#         print('there was no convergence')
#         if (abs(funcao(a)) < tol):
#           root = a
#         else:
#           root = b


# bis(0, 2, .01, 20)

# Defining Function
def f(x):
  return x**4 - 3*x**3 + 3

# Implementing Bisection Method
def bisection(x0,x1,e):
  step = 1
  print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
  condition = True
  while condition:
    x2 = (x0 + x1)/2
    print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

    if f(x0) * f(x2) < 0:
      x1 = x2
    else:
      x0 = x2
    
    step = step + 1
    condition = abs(f(x2)) > e

  print('\nRequired Root is : %0.8f' % x2)


# Input Section
x0 = input('First Guess: ')
x1 = input('Second Guess: ')
e = input('Tolerable Error: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

#Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
  print('Given guess values do not bracket the root.')
  print('Try Again with different guess values.')
else:
  bisection(x0,x1,e)
