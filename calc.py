def add(a,b):
      return a+b
def sub(a,b):
       return a-b
def mul(a,b):
       return a*b
def div(a,b):
    return a/b
print("select operation:")
print("1.Add")
print("2.sub")
print("3.Mul")
print("4.div")

while True:
      choice=input("enter choice(1/2/3/4):")
      if choice in('1','2','3','4'):
            try:
                  num1=float (input("enter first no:"))
                  num2=float (input("enter second no"))
            except ValueError:
                  print("invalid input plz enter valid no:")
                  continue
            if choice=='1':
                  print(num1,"+",num2,"=",add(num1,num2))  
            elif choice=='2':
                  print(num1,"-",num2,"=",sub(num1,num2)) 
            elif choice=='3':
                  print(num1,"*",num2,"=",mul(num1,num2)) 
            elif choice=='4':
                  print(num1,"/",num2,"=",div(num1,num2)) 
            next_cal=input("do you want next calculations(yes or no):")
            if next_cal=="no":
                  break
            else:
                  print("invalid input")