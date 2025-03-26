def genere_permutation(L):
    if len(L)==0 :
        return [[]]
    permutationPossible = []
    for i in  range(len(L)):
        element = L[i]
        #on vas prendre element de la liste
        R = L[:i] + L[i+1:]
        for permutation in genere_permutation(R):
            permutationPossible.append([element]+permutation)
    return permutationPossible

perm = genere_permutation([0,1,2])

#cette fonctionne genre toute les boucle possible d'un graphe d'ordre n si on comence par depart
def genere_boucles(n,depart):
    L = [i for i in range(n)]
    toutePossibilite = []
    for boucle in genere_permutation(L):
        if boucle[0]==depart:
            toutePossibilite.append(boucle)
    return toutePossibilite



poid = [
    [0,  2, 9,  10],
    [2,  0, 6,   4],
    [9,  6, 0,   8],
    [10, 4, 8,   0]
]

permu = [
    [0, 1, 2, 3],  # Une boucle passant par 0 → 1 → 2 → 3 → retour à 0
    [2, 3, 1, 0]   # Une autre boucle passant par 2 → 3 → 1 → 0 → retour à 2
]


def distances_boucles(LB,T):
    n= len(LB[0])
    L_distances = []
    for boucle in LB :
        cost=0
        for i in range(n):
            cost += T[boucle[i]][boucle[(i+1)% n]]
        L_distances.append(cost)
    return L_distances

'''print(distances_boucles(permu,poid))'''

def meilleure_boucles(LB,T):
    L=distances_boucles(LB,T)
    min_cost,index = L[0],0
    for i in range(len(L)):
        if L[i]<min_cost:
            min_cost,index = L[i],i
    meilleur=(min_cost,index)
    return meilleur


print(meilleure_boucles(permu,poid))

def coord_vers_matrice(LC):
    n=len(LC)
    M=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1,n) :
            M[i][j]=(((LC[i][0]-LC[j][0])**2) +((LC[i][1]-LC[j][1])**2))**(1/2)
            M[j][i]= M[i][j]
    return M

test_LC = [(1,2),(3,7),(9,9)]
print(coord_vers_matrice(test_LC))
'''On dispose des coordonnées des pointssuivants:
A(0, 0), B(1, 1), C(2, 4), D(1, −3), E(0, −5), F (0, 4), G(−1, −5), H(−2, 3) et I(−3, 0).
Résoudre le problème du voyageur de commerce sur le graphe ayant ces points comme sommets'''




ville_name=["A","B","C","D","E","F","G","H","I"]
ville=[(0, 0),(1, 1),(2, 4),(1,-3),(0,-5),(0, 4),(-1,-5),(-2,3),(-3, 0)]
poid_matrice=coord_vers_matrice(ville)
boucle_ville= genere_boucles(len(ville_name),0)
best= meilleure_boucles(boucle_ville,poid_matrice)

print("the best route is the following")
bestroute =[ville_name[i] for i in boucle_ville[best[1]]]
print(bestroute)
print(best)

