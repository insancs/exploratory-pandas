import pandas as pd
import matplotlib.pyplot as plt

# Membaca file csv
order_data = pd.read_csv("E:/DQLab/Dataset/order.csv")

'''Pandas 1'''
# Melihat struktur baris dan kolom dari dataframe
print("Jumlah baris :%d, Jumlah kolom :%d" % order_data.shape)
# Preview dataframe menggunakan head dan tail
print("Data teratas\n", order_data.head(), "\nData terbawah\n", order_data.tail())
# Summary dataframe, tambahkan include "all" jika semua kolom diproses, include "object" jika non numeric
print("Data Summary\n", order_data.describe())
# Menghitung median, mean, std,varians
print(order_data.loc[:, "price"].median())

'''Pandas 2'''
# plot histogram kolom: price
# order_data[["price"]].plot.hist(figsize=(4, 5), bins=10)
# plt.show()

# Menentukan outliers dari kolom product_weight_gram
# Hitung quartile 1 dan 3
Q1 = order_data["product_weight_gram"].quantile(0.25)
Q3 = order_data["product_weight_gram"].quantile(0.75)
IQR = Q3 - Q1
print(IQR)

# Renama kolom, bisa dengan nama kolom atau index
order_data.rename(columns={"Age": "Umur"}, inplace=True)

# Penggunaan groupby
op = order_data["price"].groupby(order_data["payment_type"]).mean()
print("\nPayment Type :\n", op)

# Hitung harga maksimum pembelian customer menggunakan sort_values, default ascending=True
sort_harga = order_data.sort_values(by="price", ascending=False)
print("\nHarga maksimun\n", sort_harga["price"])

'''Mini Project'''
print("\nMini Project\n")
# Median price yang dibayar customer dari masing-masing metode pembayaran.
print("Rata-rata price berdasarkan payment_type")
median_price = order_data["price"].groupby(order_data["payment_type"]).mean()
print(median_price)

# Ubah freight_value menjadi shipping_cost dan cari shipping_cost
# termahal dari data penjualan tersebut menggunakan sort.
order_data.rename(columns={"freight_value ": "shipping_cost "}, inplace=True)
sort_value = order_data.sort_values(by="price", ascending=False)
print("\nHarga terbesar\n", sort_value["price"].head())

# Untuk product_category_name, berapa  rata-rata weight produk tersebut
# dan standar deviasi mana yang terkecil dari weight tersebut,
mean_value = order_data["product_weight_gram"].groupby(order_data["product_category_name"]).mean()
std_value = order_data["product_weight_gram"].groupby(order_data["product_category_name"]).std()
print("\nMean :", mean_value)
print("\nStandar Deviasi :", std_value)

# Buat histogram quantity penjualan dari dataset tersebutuntuk melihat persebaran quantity
# penjualan tersebut dengan bins = 5 dan figsize= (4,5)
order_data[["quantity"]].plot.hist(figsize=(4, 5), bins=5)
plt.show()
