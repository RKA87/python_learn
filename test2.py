first_name="Rakesh"
last_name="Akuluru"

print("Reverse:", first_name[:])
print("Reverse First Name:", first_name[::-1])

input_elements=input("Enter comma seperated numbers:")
list_output=input_elements.split(",")
tuple_output=tuple(list_output)

print("list output:",list_output)
print("tuple output:",tuple_output)

exam_st_date = (11, 12, 2014)

print("Exam Standard Date: %i/ %i/ %i" %(exam_st_date))