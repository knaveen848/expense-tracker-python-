import pandas as pd

# 1. Create sales data
data = {
    "Product": ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse",
                "Monitor", "Phone", "Laptop", "Mouse", "Headphones"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories",
                 "Accessories", "Electronics", "Electronics", "Electronics",
                 "Accessories", "Accessories"],
    "Quantity": [2, 5, 10, 8, 15, 3, 4, 1, 20, 7],
    "Price": [50000, 20000, 2000, 1500, 800,
              12000, 20000, 50000, 800, 2000]
}

df = pd.DataFrame(data)
print("SALES DATA")
print(df)
df["total price"]=df["Quantity"] * df["Price"]

print("\nDATA WITH TOTAL SALES:")
print( )
print(df)
totalrevenue=df["total price"].sum( )
print("total revenue is :",totalrevenue)
average_scale=df["total price"].mean( )
print("average scale is :",average_scale)
highest_scale=df["total price"].max( )
print("highest scale is :",highest_scale)
lowest_scale=df["total price"].min( )
print("lowest scale :",lowest_scale)
highest_product=df.loc[ df["total price"].idxmax(), "Product"]
print("highest product is :",highest_product)
print()
print("product with quantity greater than 5 :")
print(df[df["Quantity"] >5])
category_scales=df.groupby("Category")["total price"].sum( )
print( )
print("category wise scales :",category_scales)
print( )
print("product count:")
print()
print(df["Product"].value_counts)
print( )
sorted_data=df.sort_values("total price",ascending=False)
print("sales sorted from high to low :")
print()
print(sorted_data)
df.to_csv("sales_data.csv",index=False)
print()
print(" sale analysis completed succesfully")