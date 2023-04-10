#====================================================================
def tree_check(dictionary, start_name):

    def check_repeat(list1, list2):
        same = False
        for i in list1:
            for j in list2:
                if i == j:
                    same = True
                    break
        return same

    queue = []
    visited = []

    names = list(dictionary.keys())
    work_node = start_name
    queue = queue + dictionary[work_node]
    visited.append(work_node)

    for key in dictionary:
        if work_node in dictionary[key]:
            dictionary[key].remove(work_node)

    cycle = False
    while cycle == False:

        if len(queue) == 0:
            break

        work_node = queue.pop(0)
        visited.append(work_node)

        for key in dictionary:
            if work_node in dictionary[key]:
                dictionary[key].remove(work_node)

        share_items = check_repeat(dictionary[work_node], queue)

        if share_items == False:
            queue = queue + dictionary[work_node]

        else:
            cycle = True
    
    is_tree = False
    if cycle == False:
        if len(names) == len(visited):
            is_tree = True
    
    return(is_tree)
#====================================================================
#przykładowe listy grafy
adj_list1 = {'0': ['1'], '1': ['0', '2'], '2': ['1', '3', '5'], '3': ['2'], '4': ['5'], '5': ['2', '4', '6', '7'], '6': ['5'], '7': ['5']}
#adj_list2 = {'0': ['1'], '1': ['0', '2'], '2': ['1', '3', '5'], '3': ['2', '4'], '4': ['3', '5'], '5': ['2', '4', '7'], '6': [], '7': ['5']}
#adj_list3 = {'0': ['1'], '1': ['0', '2'], '2': ['1', '3'], '3': ['2'], '4': ['5'], '5': ['4', '6', '7'], '6': ['5'], '7': ['5']}

x = tree_check(adj_list1, "0")
print(x)