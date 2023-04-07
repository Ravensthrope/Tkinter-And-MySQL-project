import tkinter as tk
from tkinter import ttk
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aafaq@09",
    database="Stock_Portfolio"
)
cursor = mydb.cursor()

def insert_data(stock_name, quantity, price):
    
    sql = "INSERT INTO stock (stock_name, quantity, price) VALUES (%s, %s, %s)"
    val = (stock_name, quantity, price)
    
    cursor.execute(sql, val)
    
    mydb.commit()
    
    print(cursor.rowcount, "record inserted.")

def display_data():
    # Clear the previous data from the text widget
    text.delete('1.0', tk.END)
    
    # Execute the SELECT query
    cursor.execute("SELECT * FROM stock")

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Loop through the rows and append the data to the text widget
    for row in rows:
        text.insert(tk.END, f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\n")

    # Close the cursor and database connection
    cursor.close()
    mydb.close()

root = tk.Tk()
root.title("Stock Market Portfolio")

# Create a frame for the left side of the window
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

# Create labels and entry fields for stock data
tk.Label(frame_left, text="Stock Name").grid(row=0, column=0, padx=5, pady=5)
stock_name = tk.Entry(frame_left)
stock_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_left, text="Quantity").grid(row=1, column=0, padx=5, pady=5)
quantity = tk.Entry(frame_left)
quantity.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_left, text="Purchase Price").grid(row=2, column=0, padx=5, pady=5)
purchase_price = tk.Entry(frame_left)
purchase_price.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_left, text="Current Price").grid(row=3, column=0, padx=5, pady=5)
current_price = tk.Entry(frame_left)
current_price.grid(row=3, column=1, padx=5, pady=5)

# Create a button to insert data into the database
insert_button = tk.Button(frame_left, text="Insert Data", command=insert_data)
insert_button.grid(row=4, column=1, padx=5, pady=5)

# Create a frame for the right side of the window
frame_right = tk.Frame(root)
frame_right.pack(side=tk.LEFT, padx=10, pady=10)

# Create a label and text widget to display stock data
tk.Label(frame_right, text="Stock Data").pack(pady=5)
text = tk.Text(frame_right, height=20, width=60)
text.pack()

# Create a button to display the latest data in the text widget
display_button = tk.Button(frame_right, text="Display Data", command=display_data)
display_button.pack(pady=5)

root.mainloop()