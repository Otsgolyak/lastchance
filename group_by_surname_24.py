lst_of_students = ['Anton Golyak', 'Will Smith', 'Antonio Banderas', 'Giorgio Armani', 'Zhanna Tashnizi', 'Elvis Presley', 'Anthony Kiddis', 'Jeff Waters', 'Mike Tison', 'Mikkie Roork', 'Silvester Stalone']

def group_by_surname(lst_of_students): 
    lst_2 = []
    group_A_B_C_D = []
    group_E_F_G_H = []
    group_I_J_K_L = []
    group_M_N_O_P = []
    group_Q_R_S_T = []
    group_U_V_W_X_Y_Z = []
    name_parts = ''
    for student in lst_of_students:
        
        name_parts = student.split(' ')
        lst_2.append(name_parts)
    print(lst_2)
    for i in range(len(lst_2)):
        first_letter = lst_2[i][1][0]
        
        if first_letter>='A' and first_letter<='D':
            group_A_B_C_D.append(lst_of_students[i])
        if first_letter>='E' and first_letter<='H':
            group_E_F_G_H.append(lst_of_students[i])
        if first_letter>='I' and first_letter<='L':
            group_I_J_K_L.append(lst_of_students[i])
        if first_letter>='M' and first_letter<='P':
            group_M_N_O_P.append(lst_of_students[i])
        if first_letter>='Q' and first_letter<='T':
            group_Q_R_S_T.append(lst_of_students[i])
        if first_letter>='U' and first_letter<='Z':
            group_U_V_W_X_Y_Z.append(lst_of_students[i])            
    print(group_A_B_C_D, len(group_A_B_C_D)) 
    print(group_E_F_G_H, len(group_E_F_G_H))
    print(group_I_J_K_L, len(group_I_J_K_L))
    print(group_M_N_O_P, len(group_M_N_O_P))
    print(group_Q_R_S_T, len(group_Q_R_S_T))
    print(group_U_V_W_X_Y_Z, len(group_U_V_W_X_Y_Z))     
group_by_surname(lst_of_students)
print('Total count of students: ', len(lst_of_students))