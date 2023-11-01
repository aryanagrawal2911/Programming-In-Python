def grade(m):

    if 90 <= m <= 100:
        print('A')
        
    elif 70 <= m <= 89:
        print('B')
        
    elif 50 <= m <= 69:
        print('C')
        
    elif 40 <= m <= 49:
        print('D')
        
    else:
        print('F')
        
marks = float(input())
assert 0 <= marks <= 100
grade(marks)