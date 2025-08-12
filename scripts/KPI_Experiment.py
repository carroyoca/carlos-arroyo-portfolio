import pandas as pd
import numpy as np

# 1. Supplier Influence
data_supplier_influence = {
    "Supplier": ["Supplier A", "Supplier B", "Supplier C"],
    "Bids Presented": [50, 40, 60],
    "Bids Won": [35, 28, 42],
    "Success Rate (%)": [70, 70, 70],
    "Bundling Savings ($)": [100000, 85000, 120000],
    "Performance Score": [8.5, 7.8, 8.9]
}
supplier_influence_df = pd.DataFrame(data_supplier_influence)

# 2. Decision Support
data_decision_support = {
    "Recommendation ID": [1, 2, 3, 4, 5],
    "Business": ["Business X", "Business Y", "Business Z", "Business X", "Business Y"],
    "Accepted (Yes/No)": ["Yes", "Yes", "No", "Yes", "Yes"],
    "Uptake Rate (%)": [80, 85, 75, 90, 95],
    "Analysis Delivery Timely (Yes/No)": ["Yes", "Yes", "No", "Yes", "Yes"],
    "Timeliness Rate (%)": [95, 96, 90, 95, 97]
}
decision_support_df = pd.DataFrame(data_decision_support)

# 3. Sustainability and Innovation
data_sustainability_innovation = {
    "Year": [2021, 2022, 2023],
    "Carbon Footprint Reduction (%)": [-5, -5, -5],
    "Modern Equipment Adoption (%)": [50, 60, 70]
}
sustainability_innovation_df = pd.DataFrame(data_sustainability_innovation)

# 4. Business Alignment
data_business_alignment = {
    "Business": ["Business X", "Business Y", "Business Z"],
    "Engagements (Per Year)": [5, 5, 5],
    "Total Engagements": [15, 15, 15],
    "Plan Accuracy (%)": [75, 78, 74]
}
business_alignment_df = pd.DataFrame(data_business_alignment)

# 5. Operational Efficiency
data_operational_efficiency = {
    "Year": [2021, 2022, 2023],
    "Equipment Replaced on Time (%)": [88, 90, 92],
    "Average Cost per Unit ($)": [1000, 950, 900],
    "Cost Reduction (%)": [0, 5, 10]
}
operational_efficiency_df = pd.DataFrame(data_operational_efficiency)

# Save all datasets to an Excel file with separate sheets
file_path = r"C:\\Users\\carro\\Documents\\Cimpress_database\\CapEx_KPIs_Datasets.xlsx"
with pd.ExcelWriter(file_path) as writer:
    supplier_influence_df.to_excel(writer, sheet_name="Supplier Influence", index=False)
    decision_support_df.to_excel(writer, sheet_name="Decision Support", index=False)
    sustainability_innovation_df.to_excel(writer, sheet_name="Sustainability & Innovation", index=False)
    business_alignment_df.to_excel(writer, sheet_name="Business Alignment", index=False)
    operational_efficiency_df.to_excel(writer, sheet_name="Operational Efficiency", index=False)

print(f"File successfully saved to: {file_path}")
