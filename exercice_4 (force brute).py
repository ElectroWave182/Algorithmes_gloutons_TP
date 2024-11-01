def sac_a_dos (n):

    prix = [0, 0, 8, 18, 20]
    maxi = 0

    for a in range (0, n + 1, 3):
        for b in range (0, n + 1, 4):
            for c in range (0, n + 1, 2):

                valeur = a * prix[2] + b * prix[3] + c * prix[4]
                if maxi < valeur and a + b + c <= n:
                    maxi = valeur

    return maxi


print (sac_a_dos (10))