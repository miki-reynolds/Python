def filter_solutions():    
    data = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            student = line.split(";")
            data.append(student)    

    for student in data:
        if "+" in student[1]:
            operands = student[1].split("+")
            if int(operands[0]) + int(operands[1]) == int(student[2]):
                line = f"{student[0]};{student[1]};{student[2]}"
                with open("correct.csv", "r+") as new_file_1:
                        for lines in new_file_1.read().split():
                            if line == lines:
                                break
                        else:
                            new_file_1.write(line + "\n")
                # with open("correct.csv", "a") as new_file:
                #     new_file.write(line+"\n")
        


        
        #     else:
        #         line = f"{student[0]};{student[1]};{student[2]}"
        #         with open("incorrect.csv", "a") as new_file:
        #             new_file.write(line+"\n")
    
        # if "-" in student[1]:
        #     operands = student[1].split("-")
        #     if int(operands[0]) - int(operands[1]) == int(student[2]):
        #         line = f"{student[0]};{student[1]};{student[2]}"
        #         with open("correct.csv", "a") as new_file:
        #             new_file.write(line+"\n")
        #     else:
        #         line = f"{student[0]};{student[1]};{student[2]}"
        #         with open("incorrect.csv", "a") as new_file:
        #             new_file.write(line+"\n")
    
    

# filter_solutions()
