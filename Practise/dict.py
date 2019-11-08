phonebook = {}
phonebook["john"] = 9936969455
phonebook["jack"] = 9568745896
phonebook["jain"] = 9745862178
print(phonebook)

print("******************")
marklist = {}
marklist["ajay"] = 88,77,99,55
marklist["anu"] = 55,77,100,36
marklist["baby"] = 69,52,33,95
print(marklist)
print("***************************")

phonebook = {"john" : 9874563217, "jill" : 9632587413}
for name , number in phonebook.items():
    print("phone number of %s is %d" % (name,number))
    print("**************************")

student = {"sarath" : 23, "sandeep" : 33 }
for name , number in student.items():
    print("Age of %s is %d" % (name,number))
print("****************************")

###########REMOVING A VALUE############

marklist = {
    "sarath" : 9638521475,
    "akil" : 7412589639,
    "aji" : 8522147963
}
del marklist["sarath"]
print(marklist)
print("*********************************")

phonebook = {
    "john" : 852963147,
    "jack" : 852369874,
    "jill" : 987456321
}
phonebook["jake"] = 147852369
del phonebook["jill"]
if "jake" in  phonebook:
    print("jake is listed in the phonebook")
if "jill" not in phonebook:
    print("jill is not listed in the phonebook")
