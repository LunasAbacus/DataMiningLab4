#!/usr/bin/env python

def main():
    
    D1 = []
    D2 = []
    D3 = []
    D4 = []
    D5 = []
    D6 = []
    D7 = []
    D8 = []

    clusters = []
    data = []

    f = open("reuters.clusters", "r")
    for line in f:
        clusters.append(line.rstrip("\n"))
    f.close()

    f = open("reuters.data", "r")
    for line in f:
        data.append(line.rstrip("\n"))
    f.close()
    
    #print clusters
    #print data

    # sort the files
    for i in range(0, len(clusters)):
        if(clusters[i] == '1'):
            D1.append(data[i])
        elif(clusters[i] == '2'):
            D2.append(data[i])
        elif(clusters[i] == '3'):
            D3.append(data[i])
        elif(clusters[i] == '4'):
            D4.append(data[i])
        elif(clusters[i] == '5'):
            D5.append(data[i])
        elif(clusters[i] == '6'):
            D6.append(data[i])
        elif(clusters[i] == '7'):
            D7.append(data[i])
        elif(clusters[i] == '8'):
            D8.append(data[i])
        else:
            print clusters[i]

    # write out the files
    f = open("Cluster1.dat", "w")
    for i in range(0, len(D1)):
        f.write('%s\n' % D1[i])
    f.close()

    f = open("Cluster2.dat", "w")
    for i in range(0, len(D2)):
        f.write('%s\n' % D2[i])
    f.close()

    f = open("Cluster3.dat", "w")
    for i in range(0, len(D3)):
        f.write('%s\n' % D3[i])
    f.close()

    f = open("Cluster4.dat", "w")
    for i in range(0, len(D4)):
        f.write('%s\n' % D4[i])
    f.close()

    f = open("Cluster5.dat", "w")
    for i in range(0, len(D5)):
        f.write('%s\n' % D5[i])
    f.close()

    f = open("Cluster6.dat", "w")
    for i in range(0, len(D6)):
        f.write('%s\n' % D6[i])
    f.close()
        
    f = open("Cluster7.dat", "w")
    for i in range(0, len(D7)):
        f.write('%s\n' % D7[i])
    f.close()

    f = open("Cluster8.dat", "w")
    for i in range(0, len(D8)):
        f.write('%s\n' % D8[i])
    f.close()

    print "done"

if __name__ == '__main__':
    main()
