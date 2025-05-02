import pandas as pd
import matplotlib.pyplot as plt


def read_data(data):
    df = pd.read_csv(data, encoding="ISO-8859-1")
    return df

def fixing_missing_customer_id(data):
#Assign a unique placeholder ID for each group of missing customer id with same invoice no.
#Identify rows with missing customerID
    missing_customer_id = data[data["CustomerID"].isnull()]
    #print("missing cust id \n", len(missing_customer_id))
    maximum_existing_customer_id_count = int(data["CustomerID"].dropna().max())
    #print("max custid \n", maximum_existing_customer_id_count)

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
    data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])
    invoice_date_by_quantity_top_10 = data.groupby(data["InvoiceDate"].dt.date)["Quantity"].sum().nlargest(10)
    invoice_date_by_quantity_top_10 = invoice_date_by_quantity_top_10.sort_index()
    print("Top 10 purchase dates: \n",invoice_date_by_quantity_top_10)

#Identify Top products bought
    top_products = data.groupby(["Description", "StockCode"]).size().reset_index(name = "Purchase Count").nlargest(10, "Purchase Count")
    print("Top 10 products bought: \n", top_products)

#Identify top 10 countries which purchased the most products
    top_customer_from_countries = data.groupby("Country").size().reset_index(name = "Purchase Count").nlargest(10, "Purchase Count")
    print("Top 10 countries by purchase: \n", top_customer_from_countries)
    print(data)
    data.to_csv("cleaned_ecom_data.csv", index= False)
    return invoice_date_by_quantity_top_10, top_products, top_customer_from_countries




def visualize_invoice_date_by_quantity(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index.astype(str), data.values, marker = "o", linestyle = "-", color= "orange" )
    plt.title("Invoice Date by Quantity")
    plt.xlabel("Invoice Date")
    plt.ylabel("Quantity")
    plt.xticks(rotation= 45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("images/Top purchase dates.png")
    plt.show()


def visualize_top_products(data):
    plt.figure(figsize=(10,5))
    plt.bar(data["StockCode"], data["Purchase Count"], color = "purple")
    plt.title("Top Products by purchase count")
    plt.xlabel("StockCode")
    plt.ylabel("Purchase Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/Top products.png")
    plt.show()


def visualize_top_customer_by_country(data):
    uk_data = data[data["Country"] == "United Kingdom"]
    other_data = data[data["Country"] != "United Kingdom"]

    #create subplot
    fig, axs = plt.subplots(1,2, figsize= (16,6), gridspec_kw= {"width_ratios": [1,2]})

    #plot UK
    axs[0].bar(uk_data["Country"], uk_data["Purchase Count"], color= "steelblue")

    axs[0].set_title("United Kingdom Purchase Count")
    axs[0].set_xlabel("Country")
    axs[0].set_ylabel("Purchase Count")

    #plot for other countries
    axs[1].bar(other_data["Country"], other_data["Purchase Count"], color="skyblue")

    axs[1].set_title("Other Countries Purchase Count")
    axs[1].set_xlabel("Country")
    axs[1].set_ylabel("Purchase Count")
    axs[1].tick_params(axis ="x", rotation = 45)

    plt.tight_layout()
    plt.savefig("images/Top Countries purchase count.png")
    plt.show()

#main program
def main():

    ecom_data = read_data("data.csv")
    ecom_data = fixing_missing_customer_id(ecom_data)
    invoice_data_by_quantity, top_products, top_customer_by_country = explore_data(ecom_data)
    visualize_invoice_date_by_quantity(invoice_data_by_quantity)
    visualize_top_products(top_products)
    visualize_top_customer_by_country(top_customer_by_country)


if __name__ == main():
    main()


