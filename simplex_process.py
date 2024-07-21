import  utils

def smallest_positive(l):
    smallest = max(l)
    for i in l:
        if i >= 0:
            if i < smallest:
                smallest = i
    return smallest
def at_least_one():
    for i in utils.new_tab[-1]:
        if i > 0:
            return True
    return False

def second_tab(old):
    n_tb = [[0] * 10 for i in range(5)]
    l_z, cp, which_is_p = [], [], []
    n_lp, n_cp, pivot = 0, 0, 0
    for i in range(0, 9):
        l_z.append(old[-1][i])
    n_cp = l_z.index(max(l_z))
    for i in range(0, len(old) - 1):
        cp.append(old[i][n_cp])
    for i in range(0, len(old) - 1):
        if old[i][n_cp] != 0:
            which_is_p.append(old[i][-1] / old[i][n_cp])
        else:
            which_is_p.append(-1)
    n_lp = which_is_p.index(smallest_positive(which_is_p))
    utils.base[n_lp] = utils.all[n_cp]

    pivot = old[n_lp][n_cp]

    for i in range(0, len(old[n_lp])):
        n_tb[n_lp][i] = old[n_lp][i] / pivot
    for i in range(0, len(old)):
        if i != n_lp:
            for j in range(0, len(old[n_lp])):
                n_tb[i][j] = old[i][j] - (old[i][n_cp] / pivot) * old[n_lp][j]
    utils.new_tab = n_tb.copy()

def solutions():
    solution = [0, 0, 0, 0, 0]
    second_tab(utils.tab)
    while at_least_one():
        second_tab(utils.new_tab)
    
    for i in utils.base:
        if isinstance(i, int):
            solution[i] = '%.2f'%utils.new_tab[utils.base.index(i)][-1]
    total = '%.2f'%-(utils.new_tab[-1][-1])


    for i in range(0, len(solution)):
        if solution[i] == '%.2f'%0:
            solution[i] = 0

    print(f"Oat: {solution[0]} units at ${'%.f'%utils.po}/unit\n\
Wheat: {solution[1]} units at ${'%.f'%utils.pw}/unit\n\
Corn: {solution[2]} units at ${'%.f'%utils.pc}/unit\n\
Barley: {solution[3]} units at ${'%.f'%utils.pb}/unit\n\
Soy: {solution[4]} units at ${'%.f'%utils.ps}/unit\n\n\
Total production value: ${total}")