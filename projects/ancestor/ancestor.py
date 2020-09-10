
def earliest_ancestor(ancestors, starting_node, first=True):
    earliest = [];
    found = False;
    search = starting_node;
    while not found:
        earliest = [];
        for a in ancestors:
            if a[1] == search:
                earliest.append(a[0]);
        if len(earliest) >= 1:
            found = True;
        else:
            found = True;
            earliest.append(-1);
    
    if len(earliest) == 1 and earliest[0] == -1 and first == True:
        return earliest[0]; # -1
    elif len(earliest) == 1 and earliest[0] == -1 and first == False:
        return starting_node;
    elif len(earliest) == 1 and earliest[0] != -1:
        return earliest_ancestor(ancestors, earliest[0], False);
    else:
        if earliest[0] < earliest[1]:
            return earliest_ancestor(ancestors, earliest[0], False);
        else:
            return earliest_ancestor(ancestors, earliest[1], False);

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)];
    print(earliest_ancestor(test_ancestors, 1));