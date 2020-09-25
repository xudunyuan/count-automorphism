from graph import *
from graph_io import *
import os
import copy

def init_colors(graph):
    """
    This function colors each vertex in "graph" based on the amount
    of neighbours. The colours are then saved in the first list inside
    the colors variable.
    The colors variable is a list of list of which each list contains
    the colors that were used in a certain iteration.
    """
    colors = [[]]
    for vertex in graph.vertices:
        color = len(vertex.neighbours)
        vertex.colornum = color
        if color not in colors[0]:
            colors[0].append(color)
    return colors

def color_refinement(graph, colors):
    """
    This function further refines colors according to the color refinement
    procedure. It bases the next color of a vertex on the colors of its neighbours.
    Please see the inline comments for a deeper explanation of the function.
    """
    changed_color = True
    copy_colors = copy.deepcopy(colors)
    iteration = 0
    while changed_color:
        iteration += 1
        copy_colors.append([])
        for vertex in graph.vertices:
            # First the color is defined as the colors of the neighbours, e.g.
            # if a vertex has neighbours with colors 1, 4 and 2, then this is saved
            # as "1 2 4"
            color = " ".join(sorted([str(v.colornum) for v in vertex.neighbours]))
            vertex.new_color = color
            if color not in copy_colors[iteration]: copy_colors[iteration].append(color)
        # Now the list of colors is redefined, such that the color names are no longer
        # strings but integers, e.g. the color "1 2 4" can become color 2. Note that
        # the color 2 in the current iteration has no relation to the color in the
        # previous iteration.
        for vertex in graph.vertices:
                vertex.colornum = copy_colors[iteration].index(vertex.new_color)
        copy_colors[iteration] = [i for i in range(len(copy_colors[iteration]))]
        # Lastly, we check for stable colorings, so we now when to stop the color
        # refinement process.
        if len(copy_colors[iteration]) == len(copy_colors[iteration-1]):
            changed_color = False


# Below you will find an example usage of the above functions.
# The graphs are added into a single graph class, such that they
# can be colored at the same time.

with open('colorref_smallexample_4_7.grl') as f:
    graphs = load_graph(f, read_list=True)[0]

G = graphs[0] + graphs[2]
color_refinement(G, init_colors(G))

with open(os.path.join(os.getcwd(), 'mygraph.dot'), 'w') as f:
    write_dot(G, f)




# The below lines can be used to create DOT-files for multiple graphs

# for i, G in enumerate(graphs):
#     with open(os.path.join(os.getcwd(), 'mygraph' + str(i) + '.dot'), 'w') as f:
#         write_dot(G, f)