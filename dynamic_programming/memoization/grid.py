def grid_traveller(n, m, ref = {}):
    if f'{n}{m}' in ref:
        return ref[f'{n}{m}']
    if n == 1 and m == 1: return 1
    if n == 0 or m == 0: return 0
    value = grid_traveller(n - 1, m) + grid_traveller(n, m - 1)
    ref[f'{n}{m}'] = value
    return value


print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
print(grid_traveller(3, 3))
print(grid_traveller(9, 9))
print(grid_traveller(50, 50))
