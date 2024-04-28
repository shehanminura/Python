#AND

if 7>6 and 5>4 :
    print('and')

if 7>6 and 8>9:
    print('and2')

if 8>9 and 5>3:
    print('and3')

if 6>7 and 7>9:
    print('and4')


    #OR

if 7 > 6 or 5 > 4:
        print('or1')

if 7 > 6 or 8 > 9:
        print('or2')

if 8 > 9 or 5 > 3:
        print('or3')

if 6 > 7 or 7 > 9:
        print('or4')

      #NOT

if not 7==3:
    print('not1')
if not 7>3:
    print('not2')


if 7>6 and 8>5 and 4>2 :
    print('3*and')          #RUN

if 7>6 or 8>5 or 4>2:
    print('3*or')        #RUN

if 7>6 and  8>5 and 1>2:
    print('and ,2 True')        #NO RUN

if 7>6 or 8>5 or 1>2 :
    print('or ,2 True')

if 7>6 and 8>5 or 1>2 :
    print('and=True or false')

if 7>6 or 8>5 and 1>2:
    print('or= True and False')

if 7>8 and 8>5 or 5>2 :
    print('and = false or True ')

if 7>8 or 8>5 and 5>2 :
    print(' or=true and true ')

if 7>8 or 8>5 and 1>2 :
    print('or = true and false')

if 7>8 or 8>5 and not 5>2:
    print('or=true and not true')

if not 7>8 and 8>5 and 5>2 :
    print('not false,and true and true')



if 7 == 8 and 7 > 8 or 4 == 4:
    print('false and false or true = true ')

if 7 == 8 and (7 > 8 or 4 == 4):
    print('flase and (false or true =true )=false')



if 7>8 or( 6>5 and 1>2):
    print('false or (True and False = false )')

if 7>8 and 4>2 or 1>2 and 5>2:
    print('False and True = False,False or true = true ,true and true = true')

if (7>8 and 4>2) or (3>2 and 5>2):
    print(' False or true = true')









