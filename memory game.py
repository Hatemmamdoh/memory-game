def cls():
    return("\n"*50)
chars = [ "A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J"]
import random
random.shuffle(chars)
p1s = 0
p2s = 0

numbers =[ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "11" , "12" , "13" , "14" , "15" , "16" , "17" , "18" , "19" , "20" ] 
numbers2 =  [ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "11" , "12" , "13" , "14" , "15" , "16" , "17" , "18" , "19" , "20" ]
ns = []
ts = 0
turn = 1
while ts < 10 :
 if turn %2 == 1 :
   for i in numbers2 :
    print ( i,end=' ')
   print (" ")
   print ( "player#1 - score " , p1s ) 
   x = int ( input ( " player1 : "))
   while True :
     if x in (ns) :
      x = int ( input (" This number had alredy taken please enter another number : "))
     else :
      break
   while True :
     if x > 20 or x < 1 :
      x = int(input(" Please Enter another number from 1:20 "))
     else :
      break
   y = int ( input ( " player1 : "))
   while True :
     if y in (ns) :
      y = int ( input (" This number had alredy taken please enter another number : "))
     else :
      break  
   while True :
     if y > 20 or y < 1 :
      y = int( input( " Please Enter another number from 1 to 20 "))
     else : 
      break
   numbers[x-1] = chars[x-1]
   numbers[y-1] = chars[y-1]
   if chars [ x-1 ] == chars [ y-1 ] :
    numbers [ x-1 ] = "*"
    numbers [ y-1 ] = "*"
    numbers2 [ x-1 ] = "*"
    numbers2 [ y-1 ] = "*"
    ns.append(x)
    ns.append(y)
    p1s = p1s + 1         
    ts =ts+1
   for i in numbers : 
    print ( i,end=' ' )
   if chars [ x-1 ] != chars [ y-1 ] :
    numbers [ x-1 ] = x
    numbers [ y-1 ] = y
   import time
   time.sleep(5)
   print (cls())
 else  :
    for i in numbers2 :
     print ( i,end=' ')
    print (" ") 
    print ( "player#2 - score" , p2s )
    n = int ( input ( " player2 : "))
    while True :
     if n in (ns) :
      n = int ( input (" This number had alredy taken please enter another number : "))
     else :
      break   
    while True :
     if n > 20 or n < 1  :
      n = int(input(" please Enter another number from 1 : 20 "))
     else :
      break  
    m = int ( input ( " player2 : "))
    while True :
     if n in (ns) :
      n = int ( input (" This number had alredy taken please enter another number : "))
     else :
      break  
    while True :
     if m > 20 or m < 1 :
      m = int(input(" Please Enter another number from 1 : 20"))
     else :
      break
    numbers[n-1] = chars[n-1]
    numbers[m-1] = chars[m-1]
    if chars [ m-1 ] == chars [ n-1 ] :
     numbers [ n-1 ] = "*"
     numbers [ m-1 ] = "*"
     numbers2 [ n-1 ] = "*"
     numbers2 [ m-1 ] = "*"
     ts = ts + 1
     p2s = p2s + 1
     ns.append(n)
     ns.append(m)
    for i in numbers : 
     print ( i,end=' ' )
    if chars [ n-1 ] != chars [ m-1 ] :
     numbers [n-1] = n
     numbers [m-1] = m    
    import time
    time.sleep(5)
    print(cls())
 turn = turn + 1
 print ("")
if p1s > p2s :
 print ( " Congratulation , player 1 the winner ")
if p1s < p2s :
 print ( " Congratulation , player 2 the winner ")    
