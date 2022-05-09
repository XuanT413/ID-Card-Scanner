import os
import sys
import numpy as np



def main():
    stonks = np.array([], dtype=str)
    file_path = '/Users/xprin/Downloads/adobe.csv'
    with open(file_path, 'r') as f:
        for line in f:
            np.append(stonks, np.asarray(f.readline().split('.')))  

    print(stonks[1])

main()
