def earliest_ancestor(ancestors, starting_node):
    all_parents = []

    # Loop through finding all the parents of the starting_node (6)
    # Add them to the parents array to loop on later
    for r in ancestors:
        if r[1] == starting_node:
            all_parents.append(r)

    # Continue looping until we have no more parents to loop on
    while len(all_parents) > 0:
        # Add the current parent to the variable and remove from the array
        ancestor = all_parents.pop()
        # Recursively pass the parent of the parent to find our lowest ancestor
        earlyAncestor = earliest_ancestor(ancestors, ancestor[0])
        # If we found another add it to the parents array
        if earlyAncestor > -1:
            all_parents.append((earlyAncestor, ancestor[0]))
        # If length is 0 we have no more parents, return the current parent
        elif len(all_parents) == 0:
            return ancestor[0]
    # If all else fails we have no earliest ancestor, return -1
    return -1


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(ancestors, 6))
