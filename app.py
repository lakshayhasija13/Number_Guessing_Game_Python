import random
def ngg() :
  print("Welcome to the Number Guessing Game !")
  print("Guess a number between 1 and 100")

  num = random.randint(1,100)

  a = 0

  while True :
    g = int(input())
    a = a + 1

    if g == num :
      print("Congratulations ! You guess the right number",num,"in",a,"attempts")
      break
    elif g < num :
      print(g,"is smaller than the correct number")
    elif g > num :
      print(g, "is higher than the correct number")
    elif (g == g + 1) or (g == g - 1) :
      print(g, "is closer to the correct number")
    else :
      break

if __name__ == "__main__":
    ngg()
