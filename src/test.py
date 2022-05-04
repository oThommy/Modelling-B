from integer_linear_problem import ILP
FILEPATH = r'./../brightspace-locker/Data assignment parcel transport 2 Small.xlsx'
ilp = ILP(FILEPATH)

# hubs = {7, 3, 9}
hubs = {1, 2, 5}
non_hubs = ilp.N - hubs

H = dict()
for node in ilp.N:
    H[node] = 1 if node in hubs else 0

E = {node: dict() for node in ilp.N}

# non-hub to hub / hub to non-hub edges
for non_hub in non_hubs:
    cost_dict = {hub: ilp.c[non_hub][hub] for hub in hubs} # filter on hubs
    min_cost_hub = min(cost_dict, key=cost_dict.get)
    for hub in hubs:
        E[non_hub][hub] = 1 if hub == min_cost_hub else 0
        E[hub][non_hub] = 1 if hub == min_cost_hub else 0 # since E_ij = E_ji for all i =/= j

# non-hub to non-hub edges (including itself)
for non_hub1 in non_hubs:
    for non_hub2 in non_hubs:
        E[non_hub1][non_hub2] = 0

# hub to hub edges (including itself)
for hub1 in hubs:
    for hub2 in hubs:
        E[hub1][hub2] = 1


print(ilp.get_z(H, E))
