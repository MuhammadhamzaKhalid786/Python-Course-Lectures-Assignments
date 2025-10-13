import pandas as pd

# Dataset
data = {
    "Name": ["Arooj", "Aleena", "Sara", "Areeba", "Laiba"],
    "Age": [22, 23, 24, 21, 25],
    "Salary": [800000, 600000, 700000, 500000, 900000],
    "Department": ["IT", "HR", "Finance", "IT", "HR"]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)


# 1. Display first 3 rows
print("\n1. First 3 rows:\n", df.head(3))

# 2. Display last 2 rows
print("\n2. Last 2 rows:\n", df.tail(2))

# 3. Show DataFrame info
print("\n3. DataFrame Info:")
print(df.info())

# 4. Show summary statistics
print("\n4. Summary Statistics:\n", df.describe())

# 5. Select Name column
print("\n5. Select 'Name' column:\n", df["Name"])

# 6. Select multiple columns
print("\n6. Select Name and Salary columns:\n", df[["Name", "Salary"]])

# 7. Calculate average salary
print("\n7. Average Salary:", df["Salary"].mean())

# 8. Find maximum salary
print("\n8. Maximum Salary:", df["Salary"].max())

# 9. Find minimum salary
print("\n9. Minimum Salary:", df["Salary"].min())

# 10. Calculate total salary
print("\n10. Total Salary:", df["Salary"].sum())

# 11. Filter employees with Salary > 650000
print("\n11. Salary > 650000:\n", df[df["Salary"] > 650000])

# 12. Filter employees with Age < 24
print("\n12. Age < 24:\n", df[df["Age"] < 24])

# 13. Sort by Age
print("\n13. Sort by Age:\n", df.sort_values(by="Age"))

# 14. Sort by Salary (descending)
print("\n14. Sort by Salary (descending):\n", df.sort_values(by="Salary", ascending=False))

# 15. Add new column Bonus (10% of Salary)
df["Bonus"] = df["Salary"] * 0.10
print("\n15. After adding Bonus column:\n", df)

# 16. Update Sara's Salary
df.loc[df["Name"] == "Sara", "Salary"] = 750000
print("\n16. Update Sara's Salary:\n", df)

# 17. Group by Department (Average Salary)
print("\n17. Average Salary by Department:\n", df.groupby("Department")["Salary"].mean())

# 18. Count employees in each Department
print("\n18. Count by Department:\n", df["Department"].value_counts())

# 19. Add column Age Category (Young/Old)
df["AgeCategory"] = df["Age"].apply(lambda x: "Young" if x < 24 else "Old")
print("\n19. Add AgeCategory column:\n", df)

# 20. Save DataFrame to CSV
df.to_csv("employee_data.csv", index=False)
print("\n20. Data saved to employee_data.csv")
