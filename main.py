import string
import itertools

# Variaves AFN
states_afn = int(input("States : "))
states_final_afn = input("States Final: ").split()
syms_afn = int(input("Syms : "))
lines_afn = []
for i in range(0, states_afn):
    col = []
    for j in range(0, syms_afn) :
        val = input(F'{i} | {string.ascii_lowercase[j]} : ')

        if( val == '-' ) : val = () #zerando valores - 
        else : val = tuple( int(i) for i in val.split(',')) # tranformando em tupla

        col.append( val )
    lines_afn.append(col)

# Variaves AFD
lines_afd = []
states_afd = 2 ** states_afn
syms_afd = syms_afn

# Gerando combinação de estados
states_combinations_afd = []
for i in range(1, states_afn+1):
    for j in itertools.combinations([*range(0, states_afn)], i):
        states_combinations_afd.append(j)
        # print(','.join([str(value) for value in j])) # printar tupla

# Criand Matriz AFD
for state in states_combinations_afd: # Conbinação Estados do AFD
    arr_sym = [None] * syms_afn # Array para juntar as tuplas 

    for tuple_state in state: # estados do afd
        for letter in range(0, syms_afn):
            tuple_aux = lines_afn[tuple_state][letter]

            if ( arr_sym[letter] ) : arr_sym[letter].append(tuple_aux)
            else : arr_sym[letter] = [tuple_aux]
    
    # limpando array 
    new_arr_sym = []
    for a1 in arr_sym:
        aux = ()
        for a2 in a1:
            aux += a2
        new_arr_sym.append(tuple(set(aux)))
    lines_afd.append(new_arr_sym) # adicionando array no vetor de linhas
    
# Verificando estados inacessiveis
lines_not_using = []
for i in range(0, states_afd):
    for i_st, state in enumerate(states_combinations_afd):
        is_using = True # aux para verificar se alguem usa esse estado
        for i_ln, line in enumerate(lines_afd):
            for l in line :
                # se os estados forems iguais e não estiver inutilizavel e não for ele mesmo
                if (state == l and i_st != i_ln and is_using and (i_ln not in lines_not_using) ) : 
                    is_using = False
        if (is_using and (i_st not in lines_not_using) ): #adiciona aos excluidos
            lines_not_using.append(i_st)
            
# imprimindo AFD
print("------------------ AFD GERADO ------------------")

def eFinal(states_final, state): # func para saber se estado é final ou não
    for s1 in state : 
        if ( str(s1) in states_final_afn ) : return "(f)"
    return ""
        
for i_st, state in enumerate(states_combinations_afd):
    for i_ln, line in enumerate(lines_afd):
        if (i_ln not in lines_not_using ) : 
            if ( i_st == i_ln ) : 
                for i, l in enumerate(line) :
                    #print(F'{state}\t---{string.ascii_lowercase[i]}--->\t{l}')
                    str_final1 = eFinal(states_final_afn, state)
                    str_final2 = eFinal(states_final_afn, l)
                    print(F'S{i_st}{str_final1}\t---{string.ascii_lowercase[i]}--->\tS{states_combinations_afd.index(l)}{str_final2}')

#print(states_afn, syms_afn, lines_afn)
#print(states_afd, syms_afd, lines_afd, states_combinations_afd)