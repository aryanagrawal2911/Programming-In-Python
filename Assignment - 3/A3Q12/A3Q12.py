def pattern_a(n):

     for i in range(1, n + 1):

         for j in range(1, i + 1):

             print(j, end = '\t')

         print()

pattern_a(5)
print()
print()


def pattern_b(n): 
    
     for i in range(1, n + 1):
        
         print('\t' * (n - i), end = '')

         if i == 1:
            
             s = str(i)
            
         else:

             s = (f'{i}\t{s}\t{i}')
            
         print(s)

pattern_b(4)
print()
print()


def pattern_c(n):

     for i in range(n, 0, -1):

         for j in range(i, 0, -1):

             print(j, end = '\t')

         print()

pattern_c(5)
print()
print()


def pattern_d(n):
    
     for i in range(1, n + 1):
        
         print(f'{i}\t' * i)

pattern_d(5)
print()
print()


def pattern_e(n):
    
     for i in range(1, n + 1):
        
         print('\t' * (i - 1), end  = '')

         for j in range(i, n + 1):
            
             print(j, end = '\t')
            
         print()

pattern_e(5)
print()
print()


def pattern_f(n):  

     for i in range(1, n + 1):

         if (i == 1) or (i == n):
            print('*\t' * n)

         else:

             print('*', ('\t' * (n - 1)) + '*')

pattern_f(7)
print()
print()


def pattern_g(n):
    
     for i in range(n):
        
         print('*\t' * n)

pattern_g(7)
print()
print()


def pattern_h(n):
    
     for i in range(1, n + 1):

         j = (2 * i) - 1

         print(('\t' * (n - i) + ('*\t' * j)))

pattern_h(4)
print()
print()


def pattern_i(n):

    j = (2 * n) - 1

    for i in range(n, 0, -1):

        k = n - i

        if i == n:
            print('*\t' * j)

        elif i == 1:
            print('\t' * (n - 1) + '*')

        else:
            print('\t' * k + '*', '\t' * (j - (2 * k) - 1) + '*')
    
pattern_i(4)
print()
print()


def pattern_j(n):
    
     for i in range(n, 0, -1):
        
         print(('\t' * (n - i)) + ('*\t' * ((2 * i) - 1)))

pattern_j(5)
print()
print()


def pattern_k(n):
    
     def k1n():
        
         print('\t' * (n - 1), '*')
        
     def krn(i):
        
         j = (2 * i) - 2
         print(('\t' * (n - i)) + ('*') + ('\t' * j) + ('*'))
        
     for i in range(1, n + 1):
        
         m = (n // 2) + 1
        
         if (i == 1) or (i == n):
            
             k1n()
            
         elif i > m:
            
             krn((n + 1) - i)
            
         else : krn(i)
        
         print()

pattern_k(7)
print()
print()


def pattern_l(n):
    
    for i in range(1, n + 1):

        j = (n // 2) + 1

        if i <= j:
        
            print(('\t' * abs(j - i) + ('*\t' * ((2 * i) - 1))))
        
        else:
        
            print(('\t' * abs(j - i) + ('*\t' * ((2 * abs(n + 1 - i)) - 1))))
            
        print()
        

pattern_l(7)
print()
print()


def pattern_m(n):
    
    for i in range(n):
        
        print(('\t' * i) + ('$\t' * (n - i)))

pattern_m(5)
print()
print()


def pattern_n(n):
    
    for i in range (1, n + 1):
        
        print(('\t' * (n - i)) + ('#\t' * i))

pattern_n(5)
print()
print()
