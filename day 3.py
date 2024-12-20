#task1 
# Program to multiply two matrix which is in the form of a 2d list 

def multiply_matrices(mat1, mat2):
  
    if len(mat1[0]) != len(mat2):
        print("Matrix multiplication is not possible.")
        return None

    
    rows_mat1 = len(mat1)
    cols_mat2 = len(mat2[0])
    result = [[0] * cols_mat2 for _ in range(rows_mat1)]


    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result


matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

result_matrix = multiply_matrices(matrix1, matrix2)
if result_matrix:
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)



#Menu driven dictionary

def pharmacy_menu():
    pharmacy = {}  # Dictionary to store weapon data

    while True:
        print("\n--- Armory Menu ---")
        print("1. Add Weapon")
        print("2. Retrieve Weapon Details")
        print("3. Display All Weapons")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
           
            weapon_name = input("Enter weapon name: ").strip()
            weapon_details = input("Enter weapon details: ").strip()
            armory[weapon_name] = weapon_details
            print(f"Weapon '{weapon_name}' added successfully!!!")

        elif choice == "2":
           
            weapon_name = input("Enter weapon name to retrieve: ").strip()
            if weapon_name in armory:
                print(f"Details of '{weapon_name}': {armory[weapon_name]}")
            else:
                print(f"Weapon '{weapon_name}' not found.")

        elif choice == "3":
            
            if armory:
                print("\n--- Armory Inventory ---")
                for weapon, details in armory.items():
                    print(f"{weapon}: {details}")
            else:
                print("No weapons in the armory.")

        elif choice == "4":
            print("Exiting Armory Menu. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


armory_menu()


