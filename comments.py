# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 16:36:01 2017

@author: Mike616
"""
"""
Program
input: a pickled that contains needed graph
output: a new pickled file that contains the found path

Shortest path algorithm during preprocessing
input: a graph
output: a new graph with fewer number of vertices and edges

Shortest path algorithm during query
inputs: graph, starting vertex, finishing vertex
outputs: set of edges that represent the shortest path

Structure of the program
1. Extract the pickled data
2. Iteratively compute the k-paths (preprocessing)
3. During the query use bidirectional Dijkstra algorithm on k-path
4. Save the result in the pickled file


local_path(vertex v)


"""