# Initialize a list to be an empty list (this list will store the test scores we will read from the file)
# Ask the user for a file name and open the file for reading
# For each line in the file
# Convert the test score in the current line to a number (since we need numeric data)
# Add the test score to the list (either using append or insert, up to you)
# Close the file
# Sort the list using the built in python function sort 
# if the list length is odd 
# median gets assigned the middle value of that sequence (i.e., the element at position list_length divided by 2)
# otherwise
# val1 gets the value at index list_length divided by 2 
# val2 gets the value at index list_length divided by 2 – 1 
# median gets assigned the average of val1 and val2 (i.e., val1 + val2 / 2)
# print the median to the shell (not to a file)


list1 = []
myfile = input("Enter the name of your file: ")
testfile = open(myfile.strip(), "r")
for ele in list1:
    list1.append(int(ele))
testfile.close()
list1.sort()
list1_len = len(list1)
if list1_len% 2 !=0:
    median == list1(list1_len // 2)
else:
    val1 = list1_len // 2
    val2 = (list1_len // 2) - 1
    median = (list[val1] + list1[val2]) / 2
print(median)