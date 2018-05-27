格式：
Network: Subrs.o network.o
        gcc -o Network Subrs.o network.o
Subrs.o: Subrs.c Netdefs.h
        gcc -c Subrs.c
network.o: network.c Netdefs.h
        gcc -c network.c
clean:
        rm -f *.o
