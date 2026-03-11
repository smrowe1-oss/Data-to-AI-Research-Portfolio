import pandas as pd

# Create the Driver Dimension Table (The "Who")
drivers_df = pd.DataFrame({
    'driverID': ['ASD12', 'OLF85', 'LKG46', 'POL72'],
    'location': ['New York', 'Newark', 'Jersey City', 'Newark'],
    'licenseType': ['Large van', 'Small van', 'Pickup', 'Flatbed']
})

# Create the Vehicle Transaction Table (The "What")
# We add a 'Value' column to simulate investment/asset costs for visualization
vehicles_df = pd.DataFrame({
    'vehicleID': ['DIM45', 'DIM47', 'DIM48', 'DIM49'],
    'location': ['New York', 'Jersey City', 'New York', 'Newark'],
    'asset_value': [85000, 42000, 55000, 92000]
})

# Export to CSVs optimized for Tableau
drivers_df.to_csv('drivers_dim.csv', index=False)
vehicles_df.to_csv('vehicles_fact.csv', index=False)

print("Files 'drivers_dim.csv' and 'vehicles_fact.csv' are ready for Tableau!")
