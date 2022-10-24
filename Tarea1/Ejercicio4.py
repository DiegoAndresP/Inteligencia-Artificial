def arbol_ref(arbol:list, rama:tuple):
    tree = arbol
    for i in rama:
        if isinstance(tree, list) and len (tree) >=i+1:
         tree=tree[i]
    else:
        return None
    return tree








