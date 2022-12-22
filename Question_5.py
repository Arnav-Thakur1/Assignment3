#Problem5
P_prog = "ABCDEFGHIJK"
i = 0
while len(P_prog)-i*2 >= 1:
    print(" "*i, P_prog[0 : len(P_prog) - i*2])
    i += 1