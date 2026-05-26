import pandas as pd

df = pd.read_csv("data/sales.csv")

summary = df.groupby("region")["amount"].sum().reset_index()

summary.to_csv("output/sales_summary.csv", index=False)

print("Pipeline completed successfully")
print(summary)
