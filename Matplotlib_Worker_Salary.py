import matplotlib.pyplot as plt

# Sample data
names = ["Amin", "Rafi", "Siam", "Nila", "Rumi", "Eva", "Tarek", "Hasan"]
salaries = [25000, 30000, 28000, 35000, 22000, 40000, 27000, 33000]

# Create a bar chart
plt.figure(figsize=(10,5))
plt.bar(names, salaries)
plt.title("Salary of 8 People")
plt.xlabel("Person")
plt.ylabel("Salary (BDT)")
plt.xticks(rotation=45)

# Show the chart
plt.show()
