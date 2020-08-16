# Matrices
# © 2020 by Granwyn Tan. All Rights Reserved.
# Created by Granwyn Tan on Mon, 23 Mar 2020.
# Developed by Granwyn Tan.
# Current Version: v4, 23 June 2020

print('''
Matrices
© 2020 by Granwyn Tan. All Rights Reserved.
Created by Granwyn Tan on Mon, 23 Mar 2020.
Developed by Granwyn Tan.
Current Version: v5, 21 July 2020
''')

mat_num = 1
list_RowsbyColumns = []
list_RowsAndColumns = []
list_new = []
list_new2 = []
RxC = []
list_Matrix = []
##row_num = 0
##column_num = 0
row_value = 0
row_val = 0
column_value = 0
column_val = 0
def matrix2(row, column):
    for r in range(row):
        list_new2.append([])
        for c in range(column):
            print("Row "+str(r+1)+", Column "+str(c+1)+":")
            inpu = input()
            while True:
                inpu2 = input("Save Value? [Y/N]: ")
                if inpu2.lower() == "n":
                    inpu = input("New Value: ")
                else:
                    break
            print()
            if inpu:
                if "." in inpu:
                    inpu = float(inpu)
                else:
                    inpu = int(inpu)
            else:
                inpu = 1
            list_new2[r].append(inpu)
    print("The matrix is:")
    for x in range(row):
        print(list_new2[x]) # Prints out the arrangement and format of matrix
    print()
            
def matrix1(row, column):
    for r in range(row):
        list_Matrix.append([])
        for c in range(column):
            print("Row "+str(r+1)+", Column "+str(c+1)+":")
            inp = input()
            # print(inp)
            while True:
                inpu1 = input("Save Value? [Y/N]: ")
                if inpu1.lower() == "n":
                    inp = input("New Value: ")
                    #print(inp)
                else:
                    break
            print()
            if inp:
                if "." in inp:
                    inp = float(inp)
                else:
                    inp = int(inp)
            else:
                inp = 1
            list_Matrix[r].append(inp)
    print("The matrix is:")
    for x in range(row):
        print(list_Matrix[x]) # Prints out the arrangement and format of matrix
    print()
            
print("Note: only x, X, *, by, BY or By is accepted\nDefault Values are 1 and Yes")
print()
input_type = input("Input Type (Simple [1] or Compact [2]): ")

while True:
    input_type_confirmation = input("Save Input Type? [Y/N]: ")
    if input_type_confirmation.lower() == "n":
        input_type = input("New Choice: ")
    else:
        break
print()
if "simple" in input_type.lower() or "compact" in input_type.lower() or "" == input_type or " " == input_type or "1" == input_type or "2" == input_type:
    if "simple" in input_type.lower() or "1" == input_type:
        print("Simple")
        print()
        # Can just have 2 inputs instead of having a symbol in between
        print("Matrix 1")
        row_value = input("No of rows: ")
        while True:
            row_value_confirmation = input("Save Number Of Rows? [Y/N]: ")
            if row_value_confirmation.lower() == "n":
                row_value = input("Number of Rows: ")
            else:
                break
        column_value = input("Number of Columns: ")
        while True:
            column_value_confirmation = input("Save Number Of Columns? [Y/N]: ")
            if column_value_confirmation.lower() == "n":
                column_value = input("Number of Columns: ")
            else:
                break
        print()
        if row_value:
            row_value = int(row_value)
        else:
            row_value = 1
        
        if column_value:
            column_value = int(column_value)
        else:
            column_value = 1
            
        matrix1(row_value, column_value)
            
    elif "compact" in input_type.lower() or "" == input_type or " " == input_type or "2" == input_type:
        if "" == input_type or " " == input_type:
            print("Set to Default: Compact")
        else:
            print("Compact")
        print()
        RowsbyColumns = input("Matrix 1: Number of rows x Number of columns: ")
        while True:
            RowsbyColumns_confirmation = input("Save Configuration? [Y/N]: ")
            if RowsbyColumns_confirmation.lower() == "n":
                RowsbyColumns = input("New Configuration: ")
            else:
                break
        print()
        if RowsbyColumns:
            if "x" == RowsbyColumns:
                print("Matrix Skipped")
                print()
                pass
            else:
                if "x" in RowsbyColumns:
                    list_RowsAndColumns = RowsbyColumns.split("x")
                elif "X" in RowsbyColumns:
                    list_RowsAndColumns = RowsbyColumns.split("X")
                elif "*" in RowsbyColumns:
                    list_RowsAndColumns = RowsbyColumns.split("*")
                elif "by" in RowsbyColumns:
                    list_RowsAndColumns = RowsbyColumns.split("by")
                elif "BY" in RowsbyColumns:
                    list_RowsAndColumns = RowsbyColumns.split("BY")
                elif "By" in RowsbyColumns:
                    list_RowsAndColumns = RowsbyColumns.split("By")
                row_value = int(list_RowsAndColumns[0])
                column_value = int(list_RowsAndColumns[1])
                matrix1(row_value, column_value)
        else:
            list_RowsAndColumns.append(1)
            list_RowsAndColumns.append(1)
            row_value = int(list_RowsAndColumns[0])
            column_value = int(list_RowsAndColumns[1])
            matrix1(row_value, column_value)
##    c_value = column_value
##    r_value = row_value
    
##    while r_value > 0:
##        row_num += 1
##        c_value = column_value
##        column_num = 0
##        list_Matrix.append([])
##        while c_value > 0:
##            column_num += 1
##            print("Row "+str(row_num)+", Column "+str(column_num)+":")
##            inp = input()
##            if inp:
##                if "." in inp:
##                    inp = float(inp)
##                else:
##                    inp = int(inp)
##            else:
##                inp = 1
##            list_Matrix[int(row_num)-1].append(inp)
##            c_value -= 1
##        r_value -= 1


##    print("The matrix is:")
##    for x in range(row_value):
##        print(list_Matrix[x]) # Prints out the arrangement and format of matrix

    mat_num += 1
##    newval = 0

    if "simple" in input_type.lower() or "1" in input_type:
        print("Simple")
        print()
        # Can just have 2 inputs instead of having a symbol in between
        print("Matrix 2")
        row_val = input("Number of Rows: ")
        while True:
            row_val_confirmation = input("Save Number Of Rows? [Y/N]: ")
            if row_val_confirmation.lower() == "n":
                row_val = input("Number of Rows: ")
            else:
                break
        column_val = input("Number of Columns: ")
        while True:
            column_val_confirmation = input("Save Number Of Columns? [Y/N]: ")
            if column_val_confirmation.lower() == "n":
                column_val = input("Number of Columns: ")
            else:
                break
        print()
        if row_val:
            row_val = int(row_val)
        else:
            row_val = 1
        
        if column_val:
            column_val = int(column_val)
        else:
            column_val = 1
        
        matrix2(row_val, column_val)
            
    elif "compact" in input_type.lower() or "" == input_type or " " == input_type:
        RxC = input("Matrix 2: Number of rows x Number of columns: ")
        while True:
            RxC_confirmation = input("Save Configuration? [Y/N]: ")
            if RxC_confirmation.lower() == "n":
                RxC = input("New Configuration: ")
            else:
                break
        print()
        if RxC:
            if "x" == RxC:
                print("Matrix Skipped")
                print()
                pass
            else:
                if "x" in RxC:
                    list_new = RxC.split("x")
                elif "X" in RxC:
                    list_new = RxC.split("X")
                elif "*" in RxC:
                    list_new = RxC.split("*")
                elif "by" in RxC:
                    list_new = RxC.split("by")
                elif "BY" in RxC:
                    list_new = RxC.split("BY")
                elif "By" in RxC:
                    list_new = RxC.split("By")
                row_val = int(list_new[0])
                column_val = int(list_new[1])
                matrix2(row_val, column_val)
        else:
            list_new.append(1)
            list_new.append(1)
            row_val = int(list_new[0])
            column_val = int(list_new[1])
            matrix2(row_val, column_val)

    final_list = []
    currColumn = 0
    currRow = 0
    if (row_value >= 1 and column_value >= 1) or (row_val >= 1 and column_val >= 1):
        step = input("Add, Subtract, Multiply or Inverse: ")
        if "Add" in step or "add" in step or "Plus" in step or "plus" in step:
            if row_val == row_value and column_val == column_value:
                for r in range(row_value):
                    final_list.append([])
        ##          if "simple" in input_type.lower():
        ##              column_value = int(list_RowsAndColumns[1])
        ##          elif "compact" in input_type.lower() or "" == input_type or " " == input_type:
        ##              column_value = col_val_above
        ##          currColumn = 0
                    for c in range(column_value):
                        val = list_new2[r][c]+list_Matrix[r][c]
                        # print("Value:",val)
                        final_list[r].append(val)
        ##              currColumn += 1
        ##          currRow += 1
                print()
                print("The result is: ")
                for row in final_list:
                    print(row)
            else:
                print("Result is Undefined. The Dimensions of the first (1st) Matrix is not equal to the Dimensions of the second (2nd) Matrix")
                
        elif "Minus" in step or "minus" in step or "Subtract" in step or "subtract" in step:
            if row_val == row_value and column_val == column_value:
                for r in range(row_value):
                    final_list.append([])
        ##          column_value = int(list_RowsAndColumns[1])
        ##          currColumn = 0
                    for c in range(column_value):
                        val = list_Matrix[r][c]-list_new2[r][c]
                        # print("Value:",val)
                        final_list[r].append(val)
        ##              currColumn += 1
        ##          currRow += 1
                print()
                print("The result is: ")
                for row in final_list:
                    print(row)
            else:
                print("Result is Undefined. The Dimensions of the first (1st) Matrix is not equal to the Dimensions of the second (2nd) Matrix")
                
        elif "Multiply" in step or "multiply" in step or "Times" in step or "times" in step:
            if column_value == row_val:
        ##        for r in range(row_value):
        ##            final_list.append([])
        ##            column_value = int(list_RowsAndColumns[1])
        ##            val = 0
        ##            newval = 0
        ##            print("Row",r)
        ##            for c in range(column_value):
        ##                print("Col",c)
        ##                val = list_Matrix[r][c]*list_new2[c][r]
        ##                # print("Value:",val)
        ##                newval += val
        ##            final_list[r].append(newval)
                for r in range(row_value):
                    final_list.append([])
                    for c in range(column_val):
                        final_list[r].append(0)
                for row_x in range(len(list_Matrix)):
                    # iterate through columns of Y
                    for col_y in range(len(list_new2[0])):
                        # iterate through rows of Y
                        for row_y in range(len(list_new2)):
                            final_list[row_x][col_y] += list_Matrix[row_x][row_y] * list_new2[row_y][col_y]
                print()
                print("The result is: ")
                for row in final_list:
                    print(row)
            else:
                print("Result is Undefined. The Number of Columns in first (1st) Matrix is not equal to the Number of Columns in second (2nd) Matrix")
                
        elif "Inverse" in step or "inverse" in step:
            OneOrTwo = input("Inverse of Matrix 1 or Matrix 2: ")
            if "1" in OneOrTwo or "Matrix 1" in OneOrTwo or "matrix 1" in OneOrTwo:
                if column_value == row_value:
                    if column_value == 2:
                        # Method 1: Code, more logical, adaptive code
                        for r in range(row_value):
                            final_list.append([])
                            for c in range(column_value):
                                final_list[r].append([])
                                if row_value % 2 == 0:
                                    if column_value % 2 == 0:
                                        final_list[r][c] = list_Matrix[c][r]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
                                    elif column_value % 2 != 0:
                                        final_list[r][c] = -list_Matrix[r][c]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
                                elif row_value % 2 != 0:
                                    if column_value % 2 == 0:
                                        final_list[r][c] = -list_Matrix[c][r]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
                                    elif column_value % 2 != 0:
                                        final_list[r][c] = list_Matrix[r][c]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
                        print()
                        print("The result is: ")
                        for row in final_list:
                            print(row)
                            
                        # Method 2: Just assign values, easy, not adaptive
                        '''
                        final_list = [[[],[]],[[],[]]]
                        #final_list.append([])
                        final_list[0][0] = list_Matrix[1][1]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
                        final_list[0][1] = -list_Matrix[0][1]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
                        #final_list.append([])
                        final_list[1][0] = -list_Matrix[1][0]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
                        final_list[1][1] = list_Matrix[0][0]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
    ##                  for r in range(row_value):
    ##                      # print("Unavailable")
    ##                      final_list.append([])
    ##                      for c in range(column_value):
    ##                          final_list[r][c] = list_Matrix[c][r]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
    ##                          final_list[r][c] = -list_Matrix[r][c]/(list_Matrix[0][0]*list_Matrix[1][1]-list_Matrix[0][1]*list_Matrix[1][0])
                        print()
                        print("The result is: ")
                        for row in final_list:
                            print(row)
                        '''
                    else:
                        print("Feature Currently Unavailable. Only 2x2 Matrices are supported")
                else:
                    print("Result is Undefined. The Dimensions of the first (1st) Matrix is not equal to the Dimensions of the second (2nd) Matrix")
            elif "2" in OneOrTwo or "Matrix 2" in OneOrTwo or "matrix 2" in OneOrTwo:
                if column_val == row_val:
                    if column_value == 2:
                        # print("Unavailable")
                        final_list.append([])
                        final_list[0][0] = list_new2[1][1]/(list_new2[0][0]*list_new2[1][1]-list_new2[0][1]*list_new2[1][0])
                        final_list[0][1] = -list_new2[0][1]/(list_new2[0][0]*list_new2[1][1]-list_new2[0][1]*list_new2[1][0])
                        final_list.append([])
                        final_list[1][0] = -list_new2[1][0]/(list_new2[0][0]*list_new2[1][1]-list_new2[0][1]*list_new2[1][0])
                        final_list[1][1] = list_new2[0][0]/(list_new2[0][0]*list_new2[1][1]-list_new2[0][1]*list_new2[1][0])
                        print()
                        print("The result is: ")
                        for row in final_list:
                            print(row)
                    else:
                        print("Feature Currently Unavailable. Only 2x2 Matrices are supported")
                else:
                    print("Result is Undefined. The Dimensions of the first (1st) Matrix is not equal to the Dimensions of the second (2nd) Matrix")
        else:
            print("Function Unavailable or Text is blank/empty")
    else:
        print("No Matrix Data")
else:
    print("Invalid Input")
