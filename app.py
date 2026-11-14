from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("sales.csv")

    df["Revenue"] = df["Quantity"] * df["Price"]

    total_sales = df["Revenue"].sum()
    total_quantity = df["Quantity"].sum()
    total_orders = len(df)

    return render_template(
        "index.html",
        total_sales=total_sales,
        total_quantity=total_quantity,
        total_orders=total_orders
    )

if __name__ == "__main__":
    app.run(debug=True)