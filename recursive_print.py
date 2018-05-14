def printN(N):
    if N:
        printN(N-1)
        print("%d\n"%N if ( not N%20) else "%d,"%N,end="")


#printN(500)


def PrintN1(N):
    for i in range(1,N+1):
        print("%d\n"%i if ( not i%20) else "%d,"%i,end="")


PrintN1(500)
