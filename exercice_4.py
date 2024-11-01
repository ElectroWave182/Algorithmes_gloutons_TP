def sac_a_dos (n):

    prix = [0, 0, 8, 18, 20]
    nb_articles = len (prix)

    for masse in range (nb_articles, n + 1):

        maxi = 0
        for sac in range (1, nb_articles):

            valeur = prix[sac] + prix[masse - sac]
            if valeur > maxi:
                maxi = valeur

        prix.append (maxi)
    return prix[-1]


print (sac_a_dos (10))