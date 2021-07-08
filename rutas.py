def contar_rutas_mas_cortas(C):
    alto, largo = len(C), len(C[0])

    for i in range(alto):
        for j in range(largo):
            if C[i][j] == 1:
                C[i][j] = -1
      
    if C[0][0] == -1:
        return 0
  
    for i in range(alto):
        if C[i][0] == 0:
            C[i][0] = 1
        else:
            break
  
    for i in range(1, largo):
        if C[0][i] == 0:
            C[0][i] = 1
        else:
            break
  
    for i in range(1, alto):
        for j in range(1, largo):
              
            if C[i][j] == -1:
                continue
  
            if C[i - 1][j] > 0:
                C[i][j] += C[i - 1][j]
  
            if C[i][j - 1] > 0:
                C[i][j] += C[i][j - 1]
  
    if C[alto - 1][largo - 1] > 0:
        return C[alto - 1][largo - 1] 
    else:
        return 0
