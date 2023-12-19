#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Faith Abraham"
__email__ = "fdavidkandavalli@students.columbiabasin.edu"
__course__ = "CSIT 311"
__lab__ = "Build_DG"
__date__ = "Feb 4, 2023"
__version__ = "0.0.1"

import sys
import networkx as nx
import matplotlib.pyplot as plt

def build_dg(input_file):
    # Create a directed graph
    G = nx.DiGraph()
    
    # Read the input file
    with open(input_file, 'r') as f:
        for line in f:
            # Split the line by ',' and add the edge to the graph
            src, dst = line.strip().split(',')
            G.add_edge(src, dst)
    
    # Calculate the graph density
    density = nx.density(G)
    print("Graph density:", density)
    
    # Draw the graph
    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: build_dg <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    build_dg(input_file)
