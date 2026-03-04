def find_missing_colors(grid):
    all_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
    
    present_colors = set()
    
    for row in grid:
        for color in row:
            present_colors.add(color)
    
    missing = []
    
    for color in all_colors:
        if color not in present_colors:
            missing.append(color)
    
    return missing