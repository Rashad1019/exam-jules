import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('psych_sales_data.csv')

# 1. Bar chart: Total Units Sold by Console
plt.figure(figsize=(10, 6))
units_by_console = df.groupby('Console')['Units_Sold'].sum().sort_values(ascending=False)
units_by_console.plot(kind='bar', color='skyblue')
plt.title('Total Units Sold by Console')
plt.xlabel('Console')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_console.png')
plt.close()

# 2. Pie chart: Revenue distribution by Region
plt.figure(figsize=(8, 8))
revenue_by_region = df.groupby('Region')['Revenue_USD'].sum()
revenue_by_region.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['gold', 'lightgreen', 'lightcoral', 'lightskyblue'])
plt.title('Revenue Distribution by Region')
plt.ylabel('')  # Remove y-label for pie chart
plt.tight_layout()
plt.savefig('revenue_by_region.png')
plt.close()

# 3. Line chart: Total Units Sold over time
# First, create a Period column for sorting and plotting
month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}
df['Month_Num'] = df['Month'].map(month_map)
df['Date'] = pd.to_datetime(pd.DataFrame({
    'year': df['Year'],
    'month': df['Month_Num'],
    'day': 1
}))

plt.figure(figsize=(12, 6))
units_over_time = df.groupby('Date')['Units_Sold'].sum().sort_index()
units_over_time.plot(kind='line', marker='o', linestyle='-', color='green')
plt.title('Total Units Sold Over Time')
plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_trend.png')
plt.close()

print("Charts created successfully: sales_by_console.png, revenue_by_region.png, sales_trend.png")
