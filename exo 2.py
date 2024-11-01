def palindromes (T):

    n = len (T)
    matrice = [[True] * n] * n
    maxi = 1

    for diag in range (n - 1):
        matrice[diag][diag + 1] = T[diag] == T[diag + 1]

        if 

    for col in range (2, n):
        for lig in range (col - 2):
            matrice[lig][col] = matrice[lig - 1][col - 1] and T[lig] == T[col]