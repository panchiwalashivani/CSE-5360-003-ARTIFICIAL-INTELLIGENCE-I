NAME: Shivani Panchiwala
UTA ID: 1001982478


I used Python as my programming language for Task1 

Code Structure:
1) Takes two arguments: find_dest and nodes
2) Then it iterates through each node in the destination endpoint's reachable children until it finds one with a matching parent
3) find_dest dictionary is used to get the distance and cost of each node on a path from present to destination.
4) Uses backtrack_dest() function to print out all nodes in reverse order, starting with present node, until it reaches destination node.
5) Takes in an input of details and returns a list of heuristics
6) Sorting the locations in order from largest to smallest.


To run the program, follow steps in cmd:

Uninformed Search: py find_route.py input1.txt origin_city destination_city

"py find_route.py input1.txt Bremen Kassel"

Informed Search: py find_route.py input1.txt origin_city destination_city heuristic_filename

"py find_route.py input1.txt Bremen Kassel h_kassel.txt"