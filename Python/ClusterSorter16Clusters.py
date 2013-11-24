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
    D9 = []
    D10 = []
    D11 = []
    D12 = []
    D13 = []
    D14 = []
    D15 = []
    D16 = []

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
        elif(clusters[i] == '9'):
            D9.append(data[i])
        elif(clusters[i] == '10'):
            D10.append(data[i])
        elif(clusters[i] == '11'):
            D11.append(data[i])
        elif(clusters[i] == '12'):
            D12.append(data[i])
        elif(clusters[i] == '13'):
            D13.append(data[i])
        elif(clusters[i] == '14'):
            D14.append(data[i])
        elif(clusters[i] == '15'):
            D15.append(data[i])
        elif(clusters[i] == '16'):
            D16.append(data[i])
        else:
            print clusters[i]

    # write out the files
    f = open("Cluster1.data", "w")
    for i in range(0, len(D1)):
        f.write('%s\n' % D1[i])
    f.close()

    f = open("Cluster2.data", "w")
    for i in range(0, len(D2)):
        f.write('%s\n' % D2[i])
    f.close()

    f = open("Cluster3.data", "w")
    for i in range(0, len(D3)):
        f.write('%s\n' % D3[i])
    f.close()

    f = open("Cluster4.data", "w")
    for i in range(0, len(D4)):
        f.write('%s\n' % D4[i])
    f.close()

    f = open("Cluster5.data", "w")
    for i in range(0, len(D5)):
        f.write('%s\n' % D5[i])
    f.close()

    f = open("Cluster6.data", "w")
    for i in range(0, len(D6)):
        f.write('%s\n' % D6[i])
    f.close()
        
    f = open("Cluster7.data", "w")
    for i in range(0, len(D7)):
        f.write('%s\n' % D7[i])
    f.close()

    f = open("Cluster8.data", "w")
    for i in range(0, len(D8)):
        f.write('%s\n' % D8[i])
    f.close()

    f = open("Cluster9.data", "w")
    for i in range(0, len(D9)):
        f.write('%s\n' % D9[i])
    f.close()

    f = open("Cluster10.data", "w")
    for i in range(0, len(D10)):
        f.write('%s\n' % D10[i])
    f.close()

    f = open("Cluster11.data", "w")
    for i in range(0, len(D11)):
        f.write('%s\n' % D11[i])
    f.close()

    f = open("Cluster12.data", "w")
    for i in range(0, len(D12)):
        f.write('%s\n' % D12[i])
    f.close()

    f = open("Cluster13.data", "w")
    for i in range(0, len(D13)):
        f.write('%s\n' % D13[i])
    f.close()

    f = open("Cluster14.data", "w")
    for i in range(0, len(D14)):
        f.write('%s\n' % D14[i])
    f.close()

    f = open("Cluster15.data", "w")
    for i in range(0, len(D15)):
        f.write('%s\n' % D15[i])
    f.close()

    f = open("Cluster16.data", "w")
    for i in range(0, len(D16)):
        f.write('%s\n' % D16[i])
    f.close()

    print "done"

if __name__ == '__main__':
    main()
