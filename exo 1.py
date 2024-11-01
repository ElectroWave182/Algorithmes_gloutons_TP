def est_palindrome (T, A, B):

    # Initialisation
    debut = A
    fin = B
    memes = True

    while fin > debut and memes:

        # Progression
        memes = memes and T[debut] == T[fin]
        debut += 1
        fin -= 1

    return memes


def est_palindrome2 (L):

    if len (L) <= 1:
        return True
    else:
        return L[0] == L[-1] and est_palindrome2 (L[1 : -1])


def palin_max (T):

    # Initialisation
    maxi = 0
    taille = len (T)

    for fin in range (taille):
        for debut in range (fin):

            # Progression
            if est_palindrome (T, debut, fin):
                longueur = fin - debut + 1

                if longueur > maxi:
                    maxi = longueur
                    pos = debut

    return (pos, maxi)


assert est_palindrome ("kayak_truc_inutile", 0, 4)
assert not (est_palindrome ("kayak_truc_inutile", 1, 4))
assert est_palindrome ("unrocsibiscornu", 0, 14)

assert est_palindrome2 ("kayak")
assert not (est_palindrome2 ("kayak_truc_inutile"))
assert est_palindrome2 ("unrocsibiscornu")

assert palin_max ("kayak_truc_inutile") == (0, 5)
assert palin_max ("truc_inutile_kayak") == (13, 5)
assert palin_max ("ab_unrocsibiscornu_ab") ==  (2, 16)
