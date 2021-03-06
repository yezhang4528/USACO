fin = open("tttt.in", "r")
fout = open("tttt.out", "w")

WIN_NUM = 3
individual_winner_number = 0
team_winner_number = 0

lines = fin.readlines()

def build_tttt_table(tttt_table, line, row):
    newRow = []
    for j in range(0, len(line) - 1):
        newRow.append(line[j])
    tttt_table.append(newRow)
    return tttt_table

def build_possible_combinations(tttt_table):
    possible_combinations = []
    diag_combination1 = []    # diaganol from top left down
    diag_combination2 = []    # diaganol from bottom left up
    anti_diag_combination = []
    for i in range(0, WIN_NUM):
        row_combination = []
        col_combination = []
        for j in range(0, WIN_NUM):
            row_combination.append(tttt_table[i][j])
            col_combination.append(tttt_table[j][i])
        possible_combinations.append(row_combination)
        possible_combinations.append(col_combination)
        diag_combination1.append(tttt_table[i][i])
        diag_combination2.append(tttt_table[WIN_NUM-1-i][i])
    possible_combinations.append(diag_combination1)
    possible_combinations.append(diag_combination2)
    return possible_combinations

i = 0
tttt_table = []
for line in lines:
    tttt_table = build_tttt_table(tttt_table, line, i)
    i += 1

combinations = build_possible_combinations(tttt_table)
combinationSet = set()
winner1 = 0
winner2 = 0
winnerSetList = []
for combination in combinations:
    newSet = set(combination)
    if newSet not in winnerSetList:
        if len(newSet) == 1:
            winner1 +=1
            winnerSetList.append(newSet)
        if len(newSet) == 2:
            winner2 += 1
            winnerSetList.append(newSet)

fout.write(str(winner1) + '\n')    
fout.write(str(winner2))    
fin.close()
fout.close()
