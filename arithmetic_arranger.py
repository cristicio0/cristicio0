def arithmetic_arranger ( problems, val= False ):

    first_operand=[]
    second_operand=[]
    sign=[]
    arranged_problems=''

    for problem in problems:
        x=problem.split()
        first_operand.append(x[0])
        second_operand.append(x[2])
        sign.append(x[1])
    operands=first_operand + second_operand
    for i in operands:
        if len(i)>4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems
        if not i.isdigit():
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
    for i in sign:
        if i != "+" and i != "-":
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
    if len(problems)>5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    line1=''
    line2=''
    line3=''
    line4=''
    for i in range(len(first_operand)):
        if len(first_operand[i]) > len(second_operand[i]):
            line1= line1 + " " * 2 + first_operand[i]+ " "*4
            line2= line2 + sign[i] + " " * (len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i] + " "*4
        else:
            line1= line1 + " " * (len(second_operand[i]) - len(first_operand[i])+2) + first_operand[i]+ " "*4
            line2= line2 + sign[i] + " " + second_operand[i]+ " "*4

        line3= line3 + "-" * (max(len(first_operand[i]), len(second_operand[i])) + 2) + " "*4
        result=''
        result= str(eval(first_operand[i]+sign[i]+second_operand[i]))
        if len(result) > max(len(first_operand[i]), len(second_operand[i])):
            line4= line4 + result + " "*5
        else:
            line4= line4 + " " * (max(len(first_operand[i]), len(second_operand[i]))-len(result)+1)+ result+ " "*5

    if val:
        arranged_problems= line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n " + line4.rstrip()
    else:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    return arranged_problems



