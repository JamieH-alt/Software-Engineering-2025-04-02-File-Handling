# TODO: Open "student_data.txt" in read mode
with open("student_age.txt", "r") as file:
    student_dict = {}
    for i in file:
        text = i.split(", ")
        student_dict[text[0]] = int(text[1])
    print(student_dict)
    # TODO: Create dictionary student_dict 

    # TODO: For each line, split line into name and age (separated by comma)

        # TODO: Store in the dictionary with the name as the key and age as the value

# TODO: Print the dictionary
