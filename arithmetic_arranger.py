def arithmetic_arranger(input, display = True):
    if not display: return None
    
    if (len(input) > 5): 
        return "Error: Too many problems."
    
    line1 = list()
    line2 = list()
    line3 = list()
    line4 = list()
    for item in input:
        first_number = item.split()[0]
        operator = item.split()[1]
        second_number = item.split()[2]
        
        if operator not in ["+", "-"]: return "Error: Operator must be '+' or '-'."
        if not (first_number.isdigit() and second_number.isdigit()): 
            return "Error: Numbers must only contain digits."
        if max(len(first_number), len(second_number)) > 4: 
            return "Error: Numbers cannot be more than four digits."

        if (len(first_number) >= len(second_number)):
            second_spaces = len(first_number) - len(second_number)
            first_spaces = 0
        else:
            first_spaces = len(second_number) - len(first_number)
            second_spaces = 0
        first_line = " "*4 + " "*first_spaces + first_number
        second_line = " "*2 + operator + " " + " "*second_spaces + second_number
        dashes_num = max(len(first_number), len(second_number)) + 2
        third_line = " "*2 + "-"*dashes_num
        if operator == "+":
            result = int(first_number) + int(second_number)
        else:
            result = int(first_number) - int(second_number)
        result_spaces = dashes_num - len(str(result))
        fourth_line = " "*2 + " "*result_spaces + str(result)

        line1.append(first_line)
        line2.append(second_line)
        line3.append(third_line)
        line4.append(fourth_line)

    line1 = "    ".join(line1)
    line2 = "    ".join(line2)
    line3 = "    ".join(line3)
    line4 = "    ".join(line4)
    return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    


