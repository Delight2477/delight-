# Revenue categories
import pandas as pd
import matplotlib.pyplot as plt
data = {
        "Name": ["Grace Ono", "Japheth Osayande", "Micheal Abu", "Augusta Evangeline", 
                 "Omoaneni Henry", "Uyi Imuentiyan"],
        "Department": ["Admin", "Estate", "Technical", "Account", "Marketing", 
                       "legal"],
        "Staff_Strenght": [4, 2, 4, 4, 6, 1], 
        "Lapses": [0, 0, 0, 1, 7, 2], 
        "Revenue": ["Stable", "Stable", "Stable", "Massive Growth", "Decline",
                    "Stable"]}
df = pd.DataFrame(data)
dept_summary = df.groupby("Department").agg({"Staff_Strenght": "sum", "Lapses": "sum"}).reset_index()
print("\nDepartment Summary:")
print(dept_summary)
print("\nRevenue Categories Count:")
print(df["Revenue"].value_counts())
plt.figure(figsize=(6, 6))
plt.pie(df["Revenue"].value_counts(),
        labels=df["Revenue"].value_counts().index,
        autopct="%1.1f%%", startangle=90, colors=["green", "red", "gold"])
plt.title("Revenue Performance Categories")
plt.show()