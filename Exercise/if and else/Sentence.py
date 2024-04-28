sentence=input("Enter the sentence:")
#I_came_to_computer_lab ----------> I came to computer lab
#he_came_to_computer_lab.then_he_went_to_home_.after_that_he_had_dinner
sentence=(sentence.replace("_"," "))
sentence=(sentence.replace("he", "she"))
print(sentence)

phone_number=input('Enter your phone number:')
#0764230420------->+94764230420
print(phone_number.replace("0","+94",1))

phone_number_new1="+94"+phone_number.removeprefix("0")
print(phone_number_new1)