def lielaku_skaits(saraksts):
    lielaki=0

    videjais=sum(saraksts)/len(saraksts)
    print(videjais)
    return lielaki

    print("viens skaitlis lielāks par vidējo:", lielaku_skaits([1,3,5])==1)   
    
    
    """
    Funkcija akceptē vienu argumentu - masīvu ar skaitļiem 
    un atgriež cik no šiem skaitļiem ir strikti lielāki
    par skaitļu vidējo vērtību.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem.

    Argumenti:
        saraksts {list} -- skaitļu saraksts
    Atgriež:
        int -- par vidējo lielāku skaitļu skaits
    Piemēri:
        lielaku_skaits([1, 3, 5]) == 1
        lielaku_skaits([100, 10, 180]) == 2
    """
