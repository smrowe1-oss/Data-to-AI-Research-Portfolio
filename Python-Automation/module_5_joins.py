import pandas as pd

# 1. SETUP: Creating the Dataframes (Representing SQL Tables)
# In an AI role, these would be loaded from a SQL database or CSVs.
drivers_df = pd.DataFrame({
    'driverID': ['ASD12', 'OLF85', 'LKG46', 'POL72'],
    'location': ['New York', 'Newark', 'Jersey City', 'Newark'],
    'licenseType': ['Large van', 'Small van', 'Pickup', 'Flatbed']
})

vehicles_df = pd.DataFrame({
    'vehicleID': ['DIM45', 'DIM47', 'DIM48', 'DIM49'],
    'location': ['New York', 'Jersey City', 'New York', 'Newark'],
    'vehtype': ['Large van', 'Small van', 'Pickup', 'Flatbed']
})

# 2. THE INNER JOIN (Equijoin)
# Goal: Find drivers and vehicles in the same city for immediate pairing.
# This mimics: SELECT * FROM Drivers INNER JOIN Vehicles ON location = location
inner_join_df = pd.merge(drivers_df, vehicles_df, on='location', how='inner')

# 3. THE LEFT OUTER JOIN
# Goal: Identify all drivers, even those whose required vehicle isn't in their city.
# This helps identify "Orphaned" data or resource gaps.
left_join_df = pd.merge(drivers_df, vehicles_df, on='location', how='left')

# 4. THE UNION OPERATOR
# Goal: Stack datasets (e.g., merging 1996 data with 1997 data).
# Note: In Pandas, we use concat(). Columns must match exactly.
merged_data = pd.concat([drivers_df, drivers_df]) # Doubling the set for demonstration

# 5. COMPOSITE KEY LOGIC
# In AI Research, we often create a 'unique_id' by combining two features.
# This mimics: CONSTRAINT [PK_Order_Details] PRIMARY KEY ([OrderID], [ProductID])
drivers_df['composite_key'] = drivers_df['driverID'] + "_" + drivers_df['location']

print("--- Inner Join Result (Matching Cities) ---")
print(inner_join_df)
