i = 1
d={"exit"}
e={"+"}
f={"-"}
g={"*"}
h={"/"}
val=0
result=0
result=int(result)

i=0
while i not in d:
  sign =input("Enter your sign: ")
  val1 = input("Enter your value: ")

  val=float(val1)
  def cal(sign):

            if sign==d:
                result=result+val
            elif sign=="-":
                result=result-val
            elif sign=="*":
                result=result*val
            elif sign=="/":
                result=result/val
            

                print(result)
        func=switcher.get(sign,lambda :'Invalid')
        return func()

  i = input("Enter your next step: ")
  i += 1
