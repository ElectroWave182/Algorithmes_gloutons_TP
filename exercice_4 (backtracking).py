def sac_a_dos (n, sol, maxi):

    prix = [0, 0, 8, 18, 20]

    if n < 2:
        aux = valeur (sol)
        if aux > maxi[0]