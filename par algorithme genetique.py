import random
#par algorithme genetique :
#creation de matrice de poid :

def generate_coord():
    coord=[]
    for _ in range(25):
        x,y=random.randint(0,20),random.randint(0,20)
        coord.append((x,y))
    return coord

c = generate_coord()

def matrice_poid(coord):
    n = len(coord)
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            M[i][j] = (((coord[i][0] - coord[j][0]) ** 2) + ((coord[i][1] - coord[j][1]) ** 2)) ** (1 / 2)
            M[j][i] = M[i][j]
    return M

def creer_initial(N):
    M=[]
    L=[i for i in range(25)]
    for i in range(N):
        L_copy = L.copy()  # Créer une copie indépendante
        random.shuffle(L_copy)
        M.append(L_copy)
    return M
print(creer_initial(1))

def distances_boucles(population,M):
    n = len(population[0])
    L_distances = []
    for boucle in population :
        cost=0
        for i in range(n):
            cost += M[boucle[i]][boucle[(i+1)% n]]
        L_distances.append(cost)
    return L_distances


def meilleure_individu(population,M):
    L=distances_boucles(population,M)
    min_cost,index = L[0],0
    for i in range(len(L)):
        if L[i]<min_cost:
            min_cost,index = L[i],i
    meilleur = (min_cost,index)
    return meilleur

def mutation(individu,probmut):
    n=len(individu)
    mutant=individu.copy()
    if random.random() < probmut:
        i,j = sorted(random.sample(range(n), 2))
        mutant[i:j+1]=list(reversed(mutant[i:j+1]))
    return mutant

def crossover(p1,p2):
    n=len(p1)
    point_croisement = random.randint(1,n-1)
    f1=p1[:point_croisement]
    f2=p2[:point_croisement]
    for i in p2:
        if i not in f1:
            f1.append(i)
    for i in p1:
        if i not in f2:
            f2.append(i)
    return f1,f2

parent1 = [5, 3, 2, 1, 4, 7, 8, 0, 6]
parent2 = [3, 1, 0, 5, 8, 6, 4, 2, 7]

#la selection des indevidus par roulette

def genere_roulette(population,T):
    D = distances_boucles(population,T)
    m = min(D)
    F =[(1/((d-0.99*m)**3)) for d in D]
    F_total = sum(F)
    R = []
    cumul = 0
    for f in F :
        cumul += f/F_total
        R.append(cumul)
    return R

def indiceroulette(R):
    x = random.random()
    for i,j in enumerate(R):
        if x < j:
            return i

def generation_suivante(population,T,probamut):
    next_gen = []
    Roulette = genere_roulette(population,T)
    index = indiceroulette(Roulette)
    p1,p2 = random.sample(population, 2)
    f1,f2 = crossover(p1, p2)
    next_gen.append(f1)
    next_gen.append(f2)



    return next_gen