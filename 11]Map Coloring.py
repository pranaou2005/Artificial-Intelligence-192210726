def is_valid(region, color, coloring, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def map_coloring(regions, neighbors, colors, coloring={}):
    if len(coloring) == len(regions):
        return coloring
    
    region = next(iter([r for r in regions if r not in coloring]))
    for color in colors:
        if is_valid(region, color, coloring, neighbors):
            coloring[region] = color
            result = map_coloring(regions, neighbors, colors, coloring)
            if result:
                return result
            coloring.pop(region)
    return None

def main():
    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW', 'T'],
        'T': ['V']
    }
    colors = ['red', 'green', 'blue']
    
    coloring = map_coloring(regions, neighbors, colors)
    if coloring:
        print("Map Coloring Solution:")
        for region, color in coloring.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
