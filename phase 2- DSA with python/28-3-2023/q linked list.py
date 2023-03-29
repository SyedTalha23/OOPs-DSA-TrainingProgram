'''Given a linked list of characters. Write a python function to return a new string that is created by appending all the 
characters given in the linked list as per the rules given below.
Rules:
Replace '*' or '/' by a single space
In case of two occurences of '' or '/', replace those two occurences of '' or '/', replace those two occurences by a single
space and convert the next character to upper case

Assume that
There will be not be more than two consecutives occurences of '*' or '/'
The linked list will always end with an alphabet   

Sample Input
A,n,,/,a,p,p,l,e,,a,/,d,a,y,,,k,e,e,p,s,/,,a,/,/,d,o,c,t,o,r,,A,w,a,y

Expected Output 
An apple a day keeps doctor away
'''