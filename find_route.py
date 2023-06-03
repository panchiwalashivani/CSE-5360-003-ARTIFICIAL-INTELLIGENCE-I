#NAME: Shivani Panchiwala
#UTA ID: 1001982478

import sys         #To extract cmd line arguments and for exit func  

def get_nearest_route(find_dest, nodes):
    list_path = []

    # Append list of path to destination and trace it
    def backtrack_dest(dest_endpoint, dest_reached):
        if dest_endpoint is None:
            return
        else:
            for visiting_node in dest_reached:
                if visiting_node["node"] == dest_endpoint:
                    list_path.append(dest_endpoint)
                    backtrack_dest(visiting_node["parent"], dest_reached)

    if find_dest:
        # get display of Distance and cost
        print("distance: " + str(find_dest["total_cost"]) + ".0 km")
        print("route: ")
        backtrack_dest(find_dest["present"], nodes)
        list_path.reverse()
        for i in range(0, len(list_path) - 1):
            print(loc[list_path[i]] + " to " + loc[list_path[i + 1]] + ", " + str(
                map_route_list[list_path[i]][list_path[i + 1]]) + ".0 km")
    else:
        print("distance: infinity")
        print("route:")
        print("none")
    return

def heuristic_search(input_Details):
    for route in input_Details:
        if "END OF INPUT" in route:
            break
        else:
            line_var = route.split(" ")
            heuristics[loc.index(line_var[0])] = int(line_var[1])
    return

def route_done(goals):
    for route in goals:
        if "END OF INPUT" in route:
            break
        else:
            x_var = route.strip().split(" ")
            a = x_var[0]
            b = x_var[1]
            if a in loc:
                pass
            else:
                loc.append(a)
            if b in loc:
                pass
            else:
                loc.append(b)

    loc.sort()  #sort location
    for i in range(len(loc)):
        map_route_list.append([])
        for j in range(len(loc)):
            map_route_list[i].append(-1)
        map_route_list[i][i] = 0

    for route in goals:
        if "END OF INPUT" in route:
            break
        else:
            list_1 = route.strip().split(" ")
            a = list_1[0]
            b = list_1[1]
            c = list_1[2]
            map_route_list[loc.index(a)][loc.index(b)] = int(c)
            map_route_list[loc.index(b)][loc.index(a)] = int(c)
    return


def hit_node_visited(currentIndex_Node, fin_node):
    for node in fin_node:
        if currentIndex_Node == node["node"]:
            return True
    return False

def star_search():
    d = loc.index(dest)
    gen_node = 1
    exp_node = 0
    max_node = 0
    fringe = []
    visited_node_list = []
    final_Dest = False
    fringe.append(
        {
            "present": loc.index(source),
            "total_cost": 0,
            "hcost": heuristics[loc.index(source)],
            "parent": None
        })
    while (len(fringe) > 0):
        exp_node = exp_node + 1
        if fringe[0]["present"] == d:
            visited_node_list.append({
                "node": fringe[0]["present"],
                "parent": fringe[0]["parent"]
            })
            final_Dest = fringe[0]
            break
        elif hit_node_visited(fringe[0]["present"], visited_node_list):
            del fringe[0]
            continue
        else:
            visited_node_list.append(
                {
                    "node": fringe[0]["present"],
                    "parent": fringe[0]["parent"]
                })
            for i in range(len(map_route_list[fringe[0]["present"]])):
                if map_route_list[fringe[0]["present"]][i] > 0:
                    fringe.append({
                        "present": i,
                        "total_cost": fringe[0]["total_cost"] + map_route_list[fringe[0]["present"]][i],
                        "hcost": heuristics[i],
                        "parent": fringe[0]["present"]
                    })
                    gen_node = gen_node + 1
            del fringe[0]
            fringe = fringe_ordered(fringe, True)

        if (len(fringe) > max_node):
            max_node = len(fringe)
    print("nodes expanded: " + str(exp_node))
    print("nodes generated: " + str(gen_node))


    get_nearest_route(final_Dest, visited_node_list)
    return

def fringe_ordered(fringe, backtrack_dest):
    if (len(fringe) > 1):
        for node_i in range(0, len(fringe) - 1):
            l = node_i
            for node_j in range(node_i + 1, len(fringe)):
                m = fringe[l]["total_cost"]
                n = fringe[node_j]["total_cost"]
                if backtrack_dest:
                    m += fringe[l]["hcost"]
                    n += fringe[node_j]["hcost"]
                if (m > n):
                    l = node_j
            temp = fringe[l]
            fringe[l] = fringe[node_i]
            fringe[node_i] = temp
        return fringe
    else:
        return fringe

def unicost_Search():
    dest_1 = loc.index(dest)
    gen_node = 1
    exp_node = 0
    maximum = 0
    fringe = [] 
    fin_node = []
    final_Dest = False
    fringe.append({
        "present": loc.index(source),
        "total_cost": 0,
        "parent": None
    })
    while (len(fringe) > 0):
        exp_node = exp_node + 1
        if fringe[0]["present"] == dest_1:
            fin_node.append({
                "node": fringe[0]["present"],
                "parent": fringe[0]["parent"]
            })
            final_Dest = fringe[0]
            break
        elif hit_node_visited(fringe[0]["present"], fin_node):
            del fringe[0]
            continue
        else:
            fin_node.append({
                "node": fringe[0]["present"],
                "parent": fringe[0]["parent"]
            })
            for i in range(len(map_route_list[fringe[0]["present"]])):
                if map_route_list[fringe[0]["present"]][i] > 0:
                    fringe.append({
                        "present": i,
                        "total_cost": fringe[0]["total_cost"] + map_route_list[fringe[0]["present"]][i],
                        "parent": fringe[0]["present"]
                    })
                    gen_node = gen_node + 1
            del fringe[0]
            fringe = fringe_ordered(fringe, False)
        if len(fringe) > maximum:
            maximum = len(fringe)
    # Display Output
    print("nodes expanded: " + str(exp_node))
    print("nodes generated: " + str(gen_node))


    get_nearest_route(final_Dest, fin_node)
    return

if len(sys.argv) >= 4:
    loc = []
    map_route_list = []
    route_done(open(sys.argv[1], "r").read().split("\n"))
    source = sys.argv[2]
    dest = sys.argv[3]
    if len(sys.argv) != 5:
        unicost_Search()
    elif len(sys.argv) == 5:
        heuristics = [0] * len(loc)
        heuristic_search(open(sys.argv[4], "r").read().split("\n"))
        star_search()
    else:
        print("Not Available")
