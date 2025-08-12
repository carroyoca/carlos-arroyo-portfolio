import pandas as pd
import numpy as np

# Generate a larger dataset with 5000 rows
np.random.seed(42)  # Ensure reproducibility

categories = ["Small Format", "Large Format", "Packaging", "Promotional Items"]
equipment_types = {
    "Small Format": ["Digital Printer", "Desktop Printer", "Compact Printer"],
    "Large Format": ["Offset Printer", "Large Format Digital Printer", "Banner Printer"],
    "Packaging": ["Digital Cutter", "Box Folding Machine", "Label Printer"],
    "Promotional Items": ["Textile Printer", "Heat Press Machine", "UV Printer"]
}
suppliers = {
    "Type A": ["Supplier X", "Supplier Y", "S1"],
    "Type B": ["Supplier W", "Supplier V", "S2"],
    "Type C": ["Supplier T", "Supplier S", "Supplier R"]
}

def assign_supplier(supplier_type):
    return np.random.choice(suppliers[supplier_type])

supplier_types = list(suppliers.keys())
businesses = [
    "BuildASign", "Druck.at", "Drukwerkdeal.nl", "Easyflyer", "Exaprint", "Pens.com",
    "Packstyle", "Pixartprinting", "Printi", "Tradeprint", "Vista", "WIRmachenDRUCK"
]
factory_types = ["Large", "Medium", "Small"]
technology_types = ["Digital", "Offset"]
replacement_cycles = [4, 5, 6]  # Adjusted lifecycle to 4-6 years
acquisition_years = np.random.randint(2015, 2020, size=5000)  # Adjusted acquisition years

data_5000 = []
for i in range(5000):
    category = np.random.choice(categories)
    equipment_type = (
        np.random.choice(equipment_types[category])
        if isinstance(equipment_types[category], list)
        else equipment_types[category]
    )
    acquisition_year = acquisition_years[i]
    current_year = 2024
    supplier_type = np.random.choice(supplier_types)
    supplier = assign_supplier(supplier_type)

    # Assign costs and forecasts based on category and technology type
    if category == "Small Format":
        acquisition_cost = np.random.randint(130000, 180000)  # Highest costs
        maintenance_cost = np.random.randint(18000, 25000)
        forecast_growth = round(np.random.uniform(0.005, 0.015), 4)  # Lowest growth
    elif category == "Large Format":
        acquisition_cost = np.random.randint(90000, 130000)  # High costs
        maintenance_cost = np.random.randint(12000, 18000)
        forecast_growth = (
            round(np.random.uniform(-0.02, 0.01), 4) if "Offset" in equipment_type else round(np.random.uniform(0.01, 0.02), 4)
        )  # Negative growth for some Offset
    elif category == "Promotional Items":
        acquisition_cost = np.random.randint(60000, 90000)  # Lower costs
        maintenance_cost = np.random.randint(7000, 12000)
        forecast_growth = round(np.random.uniform(0.015, 0.025), 4)  # Higher growth
    else:  # Packaging
        acquisition_cost = np.random.randint(25000, 50000)  # Lowest costs
        maintenance_cost = np.random.randint(3000, 8000)
        forecast_growth = round(np.random.uniform(0.02, 0.04), 4)  # Highest growth

    replacement_cycle = np.random.choice(replacement_cycles)

    # Calculate Total Cost of Ownership (TCO)
    # Consumables need to make up 79-82% of the TCO with variability
    base_tco = acquisition_cost + (maintenance_cost * replacement_cycle)
    consumable_percentage = np.random.uniform(0.79, 0.82)  # Random percentage between 79% and 82%
    consumable_cost_per_year = round((consumable_percentage * base_tco) / ((1 - consumable_percentage) * replacement_cycle), 2)
    tco = base_tco + (consumable_cost_per_year * replacement_cycle)

    technology_type = (
        "Digital" if "Digital" in equipment_type else "Offset"
    )
    emission_data = (
        np.random.randint(500, 1000) if technology_type == "Digital" else
        np.random.randint(1500, 2500)  # Offset has higher emissions
    )
    business = np.random.choice(businesses)
    factory_type = np.random.choice(factory_types)
    
    # Calculate if the equipment is overdue for replacement
    overdue_years = current_year - acquisition_year - replacement_cycle
    overdue_for_replacement = "Yes" if overdue_years > 0 else "No"

    # Adjust the proportion of overdue replacements (significantly fewer "Yes")
    if overdue_for_replacement == "Yes" and np.random.random() > 0.2:
        overdue_for_replacement = "No"

    data_5000.append({ 
        "Business": business,
        "Factory Type": factory_type,
        "Category": category,
        "Equipment Type": equipment_type,
        "Acquisition Date": f"{acquisition_year}-01-01",
        "Replacement Cycle (Years)": replacement_cycle,
        "Supplier": supplier,
        "Acquisition Cost ($)": acquisition_cost,
        "Maintenance Cost ($/yr)": maintenance_cost,
        "Consumable Costs ($/yr)": consumable_cost_per_year,
        "Total Cost of Ownership ($)": round(tco, 2),
        "Technology Type": technology_type,
        "Forecast Growth (1 Year)": forecast_growth,
        "Supplier Type": supplier_type,
        "Emission Data (kg CO2/yr)": emission_data,
        "Overdue for Replacement": overdue_for_replacement
    })

# Convert to DataFrame
large_capex_df = pd.DataFrame(data_5000)

# Save to Excel
file_path = r"C:\\Users\\carro\\Documents\\Cimpress_database\\Printers_Database_2024_All_Businesses_Updated.xlsx"
large_capex_df.to_excel(file_path, index=False)

print(f"File saved to: {file_path}")
