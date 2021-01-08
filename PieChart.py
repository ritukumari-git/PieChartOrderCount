#!/usr/bin/env python3

import matplotlib.pyplot as plt
import subprocess
from prettytable import PrettyTable

def totalNumberOfOrders(myFile):
    count = 0    
    with open(myFile) as openfile:
        for line in openfile:
            for part in line.split("|"):
                if "35=D" in part:
                    count=count + 1
    return (count)

def NASDAQOrders(fileName):
    p1 = subprocess.Popen(["grep", "100=NASDAQ", fileName], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "35=D"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    p3 = subprocess.Popen(["grep", "-c", "^"], stdin=p2.stdout, stdout=subprocess.PIPE)
    p2.stdout.close()
    output = p3.communicate()[0]

    #Counting total number of Filled orders for NASDAQ
    t1 = subprocess.Popen(["grep", "100=NASDAQ", fileName], stdout=subprocess.PIPE)
    t2 = subprocess.Popen(["grep", "39=2"], stdin=t1.stdout, stdout=subprocess.PIPE)
    t1.stdout.close()
    t3 = subprocess.Popen(["grep", "150=2"], stdin=t2.stdout, stdout=subprocess.PIPE)
    t2.stdout.close()
    t4 = subprocess.Popen(["grep", "-c", "^"], stdin=t3.stdout, stdout=subprocess.PIPE)
    t3.stdout.close()
    output2 = t4.communicate()[0]
    
    #Counting total number of Partial filled orders for NASDAQ
    x1 = subprocess.Popen(["grep", "100=NASDAQ", fileName], stdout=subprocess.PIPE)
    x2 = subprocess.Popen(["grep", "39=1"], stdin=x1.stdout, stdout=subprocess.PIPE)
    x1.stdout.close()
    x3 = subprocess.Popen(["grep", "150=1"], stdin=x2.stdout, stdout=subprocess.PIPE)
    x2.stdout.close()
    x4 = subprocess.Popen(["grep", "-c", "^"], stdin=x3.stdout, stdout=subprocess.PIPE)
    x3.stdout.close()
    output3 = x4.communicate()[0]
    
    #Counting total number of Cancelled orders for NASDAQ
    y1 = subprocess.Popen(["grep", "100=NASDAQ", fileName], stdout=subprocess.PIPE)
    y2 = subprocess.Popen(["grep", "39=5"], stdin=y1.stdout, stdout=subprocess.PIPE)
    y1.stdout.close()
    y3 = subprocess.Popen(["grep", "150=5"], stdin=y2.stdout, stdout=subprocess.PIPE)
    y2.stdout.close()
    y4 = subprocess.Popen(["grep", "-c", "^"], stdin=y3.stdout, stdout=subprocess.PIPE)
    y3.stdout.close()
    output4 = y4.communicate()[0]
    
    #Counting total number of Cancelled orders for NASDAQ
    z1 = subprocess.Popen(["grep", "100=NASDAQ", fileName], stdout=subprocess.PIPE)
    z2 = subprocess.Popen(["grep", "39=5"], stdin=z1.stdout, stdout=subprocess.PIPE)
    z1.stdout.close()
    z3 = subprocess.Popen(["grep", "150=5"], stdin=z2.stdout, stdout=subprocess.PIPE)
    z2.stdout.close()
    z4 = subprocess.Popen(["grep", "-c", "^"], stdin=z3.stdout, stdout=subprocess.PIPE)
    z3.stdout.close()
    output5 = z4.communicate()[0]
    
    return output.decode("utf-8"), output2.decode("utf=8"), output3.decode("utf=8"), output4.decode("utf=8"), output5.decode("utf=8")

def NYSEOrders(fileName):
    #Counting total number of New Orders for NYSE
    p1 = subprocess.Popen(["grep", "100=NYSE", fileName], stdout=subprocess.PIPE) 
    p2 = subprocess.Popen(["grep", "35=D"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    p3 = subprocess.Popen(["grep", "-c", "^"], stdin=p2.stdout, stdout=subprocess.PIPE)
    p2.stdout.close()
    output = p3.communicate()[0]
    
    #Counting total number of Filled orders for NYSE
    t1 = subprocess.Popen(["grep", "100=NYSE", fileName], stdout=subprocess.PIPE)
    t2 = subprocess.Popen(["grep", "39=2"], stdin=t1.stdout, stdout=subprocess.PIPE)
    t1.stdout.close()
    t3 = subprocess.Popen(["grep", "150=2"], stdin=t2.stdout, stdout=subprocess.PIPE)
    t2.stdout.close()
    t4 = subprocess.Popen(["grep", "-c", "^"], stdin=t3.stdout, stdout=subprocess.PIPE)
    t3.stdout.close()
    output2 = t4.communicate()[0]
    
    #Counting total number of Partial filled orders for NYSE
    x1 = subprocess.Popen(["grep", "100=NYSE", fileName], stdout=subprocess.PIPE)
    x2 = subprocess.Popen(["grep", "39=1"], stdin=x1.stdout, stdout=subprocess.PIPE)
    x1.stdout.close()
    x3 = subprocess.Popen(["grep", "150=1"], stdin=x2.stdout, stdout=subprocess.PIPE)
    x2.stdout.close()
    x4 = subprocess.Popen(["grep", "-c", "^"], stdin=x3.stdout, stdout=subprocess.PIPE)
    x3.stdout.close()
    output3 = x4.communicate()[0]
    
    #Counting total number of Cancelled orders for NYSE
    y1 = subprocess.Popen(["grep", "100=NYSE", fileName], stdout=subprocess.PIPE)
    y2 = subprocess.Popen(["grep", "39=5"], stdin=y1.stdout, stdout=subprocess.PIPE)
    y1.stdout.close()
    y3 = subprocess.Popen(["grep", "150=5"], stdin=y2.stdout, stdout=subprocess.PIPE)
    y2.stdout.close()
    y4 = subprocess.Popen(["grep", "-c", "^"], stdin=y3.stdout, stdout=subprocess.PIPE)
    y3.stdout.close()
    output4 = y4.communicate()[0]
    
    #Counting total number of Expired orders for NYSE
    z1 = subprocess.Popen(["grep", "100=NYSE", fileName], stdout=subprocess.PIPE)
    z2 = subprocess.Popen(["grep", "39=5"], stdin=z1.stdout, stdout=subprocess.PIPE)
    z1.stdout.close()
    z3 = subprocess.Popen(["grep", "150=5"], stdin=z2.stdout, stdout=subprocess.PIPE)
    z2.stdout.close()
    z4 = subprocess.Popen(["grep", "-c", "^"], stdin=z3.stdout, stdout=subprocess.PIPE)
    z3.stdout.close()
    output5 = z4.communicate()[0]
    
    return output.decode("utf-8"), output2.decode("utf=8"), output3.decode("utf=8"), output4.decode("utf=8"), output5.decode("utf=8")

def LSEOrders(fileName):
    p1 = subprocess.Popen(["grep", "100=LSE", fileName], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "35=D"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    p3 = subprocess.Popen(["grep", "-c", "^"], stdin=p2.stdout, stdout=subprocess.PIPE)
    p2.stdout.close()
    output = p3.communicate()[0]

    #Counting total number of Filled orders for LSE
    t1 = subprocess.Popen(["grep", "100=LSE", fileName], stdout=subprocess.PIPE)
    t2 = subprocess.Popen(["grep", "39=2"], stdin=t1.stdout, stdout=subprocess.PIPE)
    t1.stdout.close()
    t3 = subprocess.Popen(["grep", "150=2"], stdin=t2.stdout, stdout=subprocess.PIPE)
    t2.stdout.close()
    t4 = subprocess.Popen(["grep", "-c", "^"], stdin=t3.stdout, stdout=subprocess.PIPE)
    t3.stdout.close()
    output2 = t4.communicate()[0]
    
    #Counting total number of Partial filled orders for LSE
    x1 = subprocess.Popen(["grep", "100=LSE", fileName], stdout=subprocess.PIPE)
    x2 = subprocess.Popen(["grep", "39=1"], stdin=x1.stdout, stdout=subprocess.PIPE)
    x1.stdout.close()
    x3 = subprocess.Popen(["grep", "150=1"], stdin=x2.stdout, stdout=subprocess.PIPE)
    x2.stdout.close()
    x4 = subprocess.Popen(["grep", "-c", "^"], stdin=x3.stdout, stdout=subprocess.PIPE)
    x3.stdout.close()
    output3 = x4.communicate()[0]
    
    #Counting total number of Cancelled orders for LSE
    y1 = subprocess.Popen(["grep", "100=LSE", fileName], stdout=subprocess.PIPE)
    y2 = subprocess.Popen(["grep", "39=5"], stdin=y1.stdout, stdout=subprocess.PIPE)
    y1.stdout.close()
    y3 = subprocess.Popen(["grep", "150=5"], stdin=y2.stdout, stdout=subprocess.PIPE)
    y2.stdout.close()
    y4 = subprocess.Popen(["grep", "-c", "^"], stdin=y3.stdout, stdout=subprocess.PIPE)
    y3.stdout.close()
    output4 = y4.communicate()[0]
    
    #Counting total number of Cancelled orders for LSE
    z1 = subprocess.Popen(["grep", "100=LSE", fileName], stdout=subprocess.PIPE)
    z2 = subprocess.Popen(["grep", "39=5"], stdin=z1.stdout, stdout=subprocess.PIPE)
    z1.stdout.close()
    z3 = subprocess.Popen(["grep", "150=5"], stdin=z2.stdout, stdout=subprocess.PIPE)
    z2.stdout.close()
    z4 = subprocess.Popen(["grep", "-c", "^"], stdin=z3.stdout, stdout=subprocess.PIPE)
    z3.stdout.close()
    output5 = z4.communicate()[0]
    
    return output.decode("utf-8"), output2.decode("utf=8"), output3.decode("utf=8"), output4.decode("utf=8"), output5.decode("utf=8")

def PAROrders(fileName):
    p1 = subprocess.Popen(["grep", "100=PAR", fileName], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "35=D"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    p3 = subprocess.Popen(["grep", "-c", "^"], stdin=p2.stdout, stdout=subprocess.PIPE)
    p2.stdout.close()
    output = p3.communicate()[0]

    #Counting total number of Filled orders for PAR
    t1 = subprocess.Popen(["grep", "100=PAR", fileName], stdout=subprocess.PIPE)
    t2 = subprocess.Popen(["grep", "39=2"], stdin=t1.stdout, stdout=subprocess.PIPE)
    t1.stdout.close()
    t3 = subprocess.Popen(["grep", "150=2"], stdin=t2.stdout, stdout=subprocess.PIPE)
    t2.stdout.close()
    t4 = subprocess.Popen(["grep", "-c", "^"], stdin=t3.stdout, stdout=subprocess.PIPE)
    t3.stdout.close()
    output2 = t4.communicate()[0]
    
    #Counting total number of Partial filled orders for PAR
    x1 = subprocess.Popen(["grep", "100=PAR", fileName], stdout=subprocess.PIPE)
    x2 = subprocess.Popen(["grep", "39=1"], stdin=x1.stdout, stdout=subprocess.PIPE)
    x1.stdout.close()
    x3 = subprocess.Popen(["grep", "150=1"], stdin=x2.stdout, stdout=subprocess.PIPE)
    x2.stdout.close()
    x4 = subprocess.Popen(["grep", "-c", "^"], stdin=x3.stdout, stdout=subprocess.PIPE)
    x3.stdout.close()
    output3 = x4.communicate()[0]
    
    #Counting total number of Cancelled orders for PAR
    y1 = subprocess.Popen(["grep", "100=PAR", fileName], stdout=subprocess.PIPE)
    y2 = subprocess.Popen(["grep", "39=5"], stdin=y1.stdout, stdout=subprocess.PIPE)
    y1.stdout.close()
    y3 = subprocess.Popen(["grep", "150=5"], stdin=y2.stdout, stdout=subprocess.PIPE)
    y2.stdout.close()
    y4 = subprocess.Popen(["grep", "-c", "^"], stdin=y3.stdout, stdout=subprocess.PIPE)
    y3.stdout.close()
    output4 = y4.communicate()[0]
    
    #Counting total number of Cancelled orders for PAR
    z1 = subprocess.Popen(["grep", "100=PAR", fileName], stdout=subprocess.PIPE)
    z2 = subprocess.Popen(["grep", "39=5"], stdin=z1.stdout, stdout=subprocess.PIPE)
    z1.stdout.close()
    z3 = subprocess.Popen(["grep", "150=5"], stdin=z2.stdout, stdout=subprocess.PIPE)
    z2.stdout.close()
    z4 = subprocess.Popen(["grep", "-c", "^"], stdin=z3.stdout, stdout=subprocess.PIPE)
    z3.stdout.close()
    output5 = z4.communicate()[0]
    
    return output.decode("utf-8"), output2.decode("utf=8"), output3.decode("utf=8"), output4.decode("utf=8"), output5.decode("utf=8")

def marketPieChart(numOfNYSEOrders, numofNASDAQ, numofLSE, numofPAR):
    # Data to plot
    #labels = 'Python', 'C++', 'Ruby', 'Java'
    labels = 'NYSE', 'NASDAQ', 'LSE', 'PAR'
    sizes = [numOfNYSEOrders, numofNASDAQ, numofLSE, numofPAR]
    colors = ['yellowgreen', 'gold', 'lightcoral', 'lightskyblue']
    explode = (0, 0, 0, 0)  # explode slice
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.savefig('pic.png')
    #plot=>plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    plt.pie(sizes, explode=explode, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
     myFile="/Users/coolritz/Documents/PYTHON/CODE/messages.txt"
     total = totalNumberOfOrders(myFile)
     
     numOfNYSEOrders, numFilledNYSE, partialNYSE, cancelNYSE, expireNYSE = NYSEOrders(myFile)
     numofNASDAQ, numFilledNASDAQ, partialNASDAQ, cancelNASDAQ, expireNASDAQ = NASDAQOrders(myFile)
     numofLSE, numFilledLSE, partialLSE, cancelLSE, expireLSE = LSEOrders(myFile)
     numofPAR,numFilledPAR, partialPAR, cancelPAR, expirePAR = PAROrders(myFile)
    
     totalFills = numFilledNYSE + numFilledNASDAQ + numFilledLSE + numFilledPAR
     totalPartialFills = partialNYSE + partialNASDAQ+ partialLSE+ partialPAR
     totalCancels = cancelNYSE + cancelNASDAQ + cancelLSE+cancelPAR
     totalExpired = expireNYSE+ expireNASDAQ+expireLSE+ expirePAR
     
     print(totalFills)
     
     y = PrettyTable()
     y.field_names = ["Total Number of Orders"]
     y.add_row([total])
     
     x = PrettyTable()
     x.field_names = ["Market", "TotalOrders", "Fills", "Partial Fills", "Cancel", "Expired"]
     x.add_row(["NYSE",numOfNYSEOrders, numFilledNYSE, partialNYSE, cancelNYSE,expireNYSE])
     x.add_row(["NASDAQ",numofNASDAQ, numFilledNASDAQ, partialNASDAQ,cancelNASDAQ, expireNASDAQ])
     x.add_row(["LSE",numofLSE,numFilledLSE,partialLSE, cancelLSE,expireLSE ])
     x.add_row(["PAR",numofPAR, numFilledPAR, partialPAR,  cancelPAR,expirePAR])
     print(y)
     print(x)
     marketPieChart(numOfNYSEOrders, numofNASDAQ, numofLSE, numofPAR)
