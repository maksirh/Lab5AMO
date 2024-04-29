def funcslar(listKoef, listViln):
    slar = ''
    for viln in range(len(listViln)):
        slar += f'{listKoef[viln * len(listViln)]}*x1'
        for b in range(1, len(listViln)):
            slar += f' + {listKoef[b + viln * len(listViln)]}*x{b + 1}'
        slar += f' = {listViln[viln]}\n'
    return slar
