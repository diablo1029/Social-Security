import random
from random import randint

sum = 10
while sum > 0:
    sum -= 1
    gender = randint(0,1)
    first_names = [["Richard", "Jacob", "David", "Henry", "Andrew", "Charles", "Stephen", "Gregory", "George", "Chance", "Shayne", "Shaun", "Shawn", "Drake", "Daniel", "Hugh", "Rodger"], 
                ["Jessica", "Jasmine", "Shayla", "Marissa", "Cheryl", "Hannah", "Alexandra", "Sarah", "Samantha", "Kelsey", "Keesha", "Kristy", "London", "McCall", "Aspen", "Leah", "Denice", "Kelly"]]
    f_name = random.choice(first_names[gender])
    middle_init = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    m_init = random.choice(middle_init)
    last_names = ["Rogerson", "Jackson", "McClure", "Quigley", "Hendrickson", "King", "Cooper", "Willson", "Martin", "Thompson", "Ryan", "Roberts", "Chapplin", "McNeff", "McLeary", "McDonald", "Jacobson", "Richardson", "Maclaroy"]
    l_name = random.choice(last_names)
    height = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    hair_color = ["BRO","BLK","BLD","UNK","GRY"]
    eye_color = ["BLU","BRO","HAZ","GRN"]
    DOB_month = randint(1,12)
    DOB_day = randint(1,30)
    DOB_year = randint(1947,2001)
    print (f_name+" "+m_init+" "+l_name)
    print (DOB_month,"/",DOB_day,"/",DOB_year, sep = '')
    if gender == 0:
        print ("Sex: M")
    else :
        print ("Sex: F")

    if gender == 0:
        ft = randint(5,6)
        if ft == 5:
            print (height[5],"'-",height[randint(6,11)],'"', sep = '')
        else :
            print (height[6],"'-",randint(0,3),'"', sep = '')
    else :
        print (height[5],"'-",height[randint(0,11)],'"', sep = '')
    if gender == 0:
        lbs = randint(140,250)
        print (lbs,"lb",sep = '')
    else :
        lbs = randint(110,220)
        print (lbs,"lb",sep = '')    
    print ("Eyes:",eye_color[randint(0,3)])
    if DOB_year < 1960:
        print ("Hair:",hair_color[randint(0,4)],"\n")
    else :
        print ("Hair:",hair_color[randint(0,2)],"\n")