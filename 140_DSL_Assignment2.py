def accept_matrix(R,C):
    for i in range(R):
        A1 = []
        for j in range(C):
            A1.append(int(input("Enter number : ")))
        A.append(A1)

def display_matrix(R,C):
    for i in range(R):
        for j in range(C):
            print(A[i][j], end=" ")
        print()

def saddle_point(R,C):
    for i in range(R):
        A1 = []
        for j in range(C):
            A1.append(int(input()))
        A.append(A1)

    for i in range(R):
        min_row = A[i][0]
        col_ind = 0
        for j in range(C):
            if min_row > A[i][j]:
                min_row = A[i][j]
                col_ind = j
        check = 0
        for k in range(R):
            if min_row < A[k][col_ind]:
                check = 1
                break
        if check == 0:
            print("Saddle point found at index " + str(i) + " , " + str(col_ind))
        else:
            print("Saddle point not found ")
            break
        print()


while(1):
    print("\n1.Accept matrix \n2.Show matrix \n3.Saddle point")
    print("0 to exit")
    z = int(input("\nEnter your choice : "))
    if (z == 0):
        print("You are exited")
        break
    elif (z == 1):
        A = []
        R = int(input("Enter the number of rows : "))
        C = int(input("Enter the number of columns : "))
        accept_matrix(R,C)
    elif (z == 2):
        display_matrix(R,C)
    elif (z == 3):
        R = int(input("Enter the number of rows : "))
        C = int(input("Enter the number of columns : "))
        A = []
        print("Enter the entries : ")
        saddle_point(R,C)
    else:
        print("Wrong choice")
        break










