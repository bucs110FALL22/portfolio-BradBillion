import random
score = 0
playing = True
while playing == True:
  num = random.randint(1, 11)
  guessing = True
  print("New Number Generated, Guess the Number!")
  while guessing == True:
    for i in range(4):
      if i == 3:
        print("Out of Guesses... You Lose!")
        print("Your Score was: " + str(score))
        guessing = False
        playing = False
        break
      else:
        guess = int(input("Guess " + str(i+1) + ": "))
        if guess > num:
          print("Too High!")
        if guess < num:
          print("Too Low!")
        if guess == num:
          print("Correct!")
          score+=1
          guessing = False
          break
