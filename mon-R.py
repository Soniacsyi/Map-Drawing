# Assume we have the values for BC(L) and TR(L)
BC_L = ... # Replace with the actual calculation or value for Betweenness Centrality
TR_L = ... # Replace with the actual calculation or value for Traffic Rate

# Weight factors
phi_1 = 0.5
phi_2 = 0.5

# Calculate resilience R(L)
R_L = phi_1 * BC_L + phi_2 * TR_L

# Now R_L holds the resilience of the metro line
print(f"The resilience of the metro line L is {R_L}")