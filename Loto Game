import random
counter = 0
gnum,r = [],[]
n = sorted(random.sample(range(1,40),7))
l = random.randint(1,7)
print("Welcome To LOTO Game!\nYou need to pick 7 numbers and choose your lucky number to double your prize.\nGood Luck!")
for g in range(7):
    guess = int(input("Lets pick number between 0-9: "))
    if 0 < guess <= 40:
        gnum.append(guess)
    else:
        print("Invalid input!")
        guess = int(input("Lets pick number between 0-9: "))
        gnum.append(guess)
    for i in range(7):
        if guess == n[i]:
            counter+=1
            r.append(n[i])
guess_l = int(input("Lets pick lucky number: (1-7) "))
gnum = sorted(gnum)
while(True):
    if gnum == n:
        if (gnum == n) and (guess_l == l):
            print("Your guess", gnum, "matches to LOTO", n, "\nYou Are MILLIONAIRE!")
            print("You guessed right the lucky number too", l, "and your prize doubled!!!")
            print("Your Prize is: 200,000,000 Million Dollars!")
            break
        print("Your guess",gnum,"matches to LOTO",n,"\nYou Are MILLIONAIRE!")
        print("Your Prize is: 100,000,000 Million Dollars!")
        break

    elif counter == 6:
        if (counter == 6) and (guess_l == l):
            print("You very lucky but not enough, You have", counter, "matches out of", len(n), "\nLoto numbers is:", n)
            print("You guessed right:", sorted(r))
            print("You guessed right the lucky number too", l, "and your prize doubled!!!")
            print("Your Prize is: 400,000,000 Million Dollars!")
            break
        print("You very lucky but not enough, You have",counter,"matches out of",len(n),"\nLoto numbers is:",n)
        print("You guessed right:",sorted(r))
        print("Your Prize is: 2,000,000 Million Dollars!")
        break

    elif counter == 5:
        if (counter == 5) and (guess_l == l):
            print("You very lucky but not enough, You have", counter, "matches out of", len(n), "\nLoto numbers is:", n)
            print("You guessed right:", sorted(r))
            print("You guessed right the lucky number too", l, "and your prize doubled!!!")
            print("Your Prize is: 4,000,000 Million Dollars!")
            break
        print("You very lucky but not enough, You have",counter,"matches out of",len(n),"\nLoto numbers is:",n)
        print("You guessed right:",sorted(r))
        print("Your Prize is: 2,000,000 Million Dollars!")
        break

    elif 1 <= counter > 5:
        print("You very lucky but not enough, You have",counter,"matches out of",len(n),"\nLoto numbers is:",n)
        print("You guessed right:",sorted(r))
        break
    else:
        print("You Lose!\nYour guess",gnum,",please try again!\nLoto numbers is:",n)
        break



