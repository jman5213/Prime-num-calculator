from time import perf_counter

currentPrime=3
calcThru=int(input("Num: "))
currentNum=currentPrime
if calcThru <= 2:
  print("invalid input!")

else:
  timeA=perf_counter()

  while currentNum <= calcThru:
    if currentNum%2!=0:
      print(currentNum,"is not even")
      for i in range(3,int((currentNum-1)/2),2):
        print("trying to divide",currentNum,"by",i)
        if currentNum%i == 0:
          currentNum+=2
          print("breaking @ "+str(currentNum-2))
          break
        print("Didn't break @",str(currentNum),"divided by",i)
        currentPrime=currentNum
    currentNum+=2

  timeB=perf_counter()
  print("Num:".ljust(len("CurrentNum: ")," "),currentPrime)
  print("Time:".ljust(len("CurrentNum: ")," "),str(timeB-timeA))
  print("CurrentNum: ",currentNum)
  