import numpy as np
import sys

def print_stat(listNum, file_name):
    print(file_name)
    print("mean:", np.mean(listNum), "std:", np.std(listNum), "max:", np.max(listNum), "min:", np.min(listNum), "n:", len(listNum), "\n")

def main(argv):
    listSum = []
    for file_name in argv:
        with open(file_name) as file:
            listNum = [int(line.rstrip()) for line in file if line.rstrip().isnumeric()]
        if listNum:
            print_stat(listNum, file_name)
        listSum += listNum
        
    if listSum:
        print_stat(listSum, "combined")

if __name__ == "__main__":
   main(sys.argv[1:])
