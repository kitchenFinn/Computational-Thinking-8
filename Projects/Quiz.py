#Beginning
Smart_Points = 0
Dumb_Points = 0

#Middle: Questions
answer = input("Would you rather A) Not eat fruit for a week or B) Only eat fruit for a week or finn is cool?")
if answer == "a" or "A":
        Smart_Points += 1
elif answer == "finn is cool":
        Smart_Points += 283
else:
        Dumb_Points += 1.5


#2

answer = input("Would you rather A) play soccer with MEsSI or B) Play basketball with Michael Jordan?")
if answer == "a" or "A":
        Smart_Points += 1
elif answer == "finn is cool":
        Smart_Points += 283
else:
        Dumb_Points += 1

#3
answer = input("Would you rather A) Learn Brazilian or B) Learn a secret language that only your friends and family know or C) Learn Russian?")
if answer == "b" or "B":
        Smart_Points += 1
elif answer == "c" or "C":
        Smart_Points += .5
else:
        Dumb_Points += 1
        Smart_Points = 0


#4
answer = input("Would you rather A) Get five snickers bars or B) Get ten Snickers bars?")
if answer == "b" or "B":
        Smart_Points += 1
else:
        Dumb_Points += 1

#5
answer = input("Would you rather A) Be able to do a back flip or B) Get tons of money ?")
if answer == "a" or "A":
        Smart_Points += 1
else:
        Dumb_Points += 1

#End: determine results
if Smart_Points >= Dumb_Points:
        print ("Nice job!")
if Smart_Points == Dumb_Points:
        print ("You are pretty bad.")
if Smart_Points <= Dumb_Points:
        print ("You failed!")


#if Smart_Points == Dumb_Points+3:
        print ("You are very smart")
#if Smart_Points >= Dumb_Points+2 and Smart_Points < Dumb_Points+3:
#if Smart_Points >= Dumb_Points+1 and Smart_Points < Dumb_Points+2:
#        print ("You are kinda smart")
#if Smart_Points == Dumb_Points+.5:
 #       print ("You are one question away from being stupid")
#if Smart_Points == Dumb_Points:
#        print ("You are kinda dumb")
#if Smart_Points+.5 == Dumb_Points:
#        print ("You are more stupid than smart")
#if Smart_Points+1 < Dumb_Points and Smart_Points+2 > Dumb_Points:
#        print ("You are pretty stupid")
#if Smart_Points+2 < Dumb_Points and Smart_Points+3 > Dumb_Points:
#        print ("You are very dumb")
#if Smart_Points+3 < Dumb_Points:
#        print ("You failed")