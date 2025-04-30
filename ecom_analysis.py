import pandas as pd


def read_data(data):
    df = pd.read_csv(data, encoding="ISO-8859-1")
    return df

def fixing_missing_customer_id(data):
#Assign a unique placeholder ID for each group of missing customer id with same invoice no.
#Identify rows with missing customerID
    missing_customer_id = data[data["CustomerID"].isnull()]
    maximum_existing_customer_id_count = int(data["CustomerID"].dropna().max())

#Group by invoice no. to assign same id to same invoice
    unique_invoices = missing_customer_id["InvoiceNo"].unique()
    fake_ids = range(maximum_existing_customer_id_count + 1, maximum_existing_customer_id_count + 1 + len(unique_invoices))
    invoice_to_id = dict(zip(unique_invoices, fake_ids))
    data.loc[data["CustomerID"].isnull(),"CustomerID"] = data.loc[data["CustomerID"].isnull(),"InvoiceNo"].map(invoice_to_id)
    data["CustomerID"] = data["CustomerID"].astype(int)
    return data



def explore_data(data):
    pd.set_option("display.max_columns", None)
    print(data.head(10))
    data.info()
    print("Data Summary: \n",data.describe())
    #Missing values
    print("Number of missing values: \n", data.isnull().sum())
    #Fix missing values for columns= "Description" and "CustomerID"
    data["Description"] = data["Description"].fillna("Not Mentioned")
    print("Number of missing values: \n", data.isnull().sum())

#Identify Top 10 purchase dates
    invoice_date_by_quantity_top_10 = data.groupby("InvoiceDate")["Quantity"].sum().nlargest(10)
    print("Top 10 purchase dates: \n",invoice_date_by_quantity_top_10)

#Identify Top products bought
    top_products = data.groupby(["Description", "StockCode"]).size().reset_index(name = "Purchase Count").nlargest(10, "Purchase Count")
    print("Top 10 products bought: \n", top_products)

#Identify top 10 countries which purchased the most products
    top_customer_from_countries = data.groupby("Country").size().reset_index(name = "Purchase Count").nlargest(10, "Purchase Count")
    print("Top 10 countries by purchase: \n", top_customer_from_countries)









ecom_data = read_data("data.csv")
ecom_data = fixing_missing_customer_id(ecom_data)
explore_data(ecom_data)


