# utils/loader.py
import pandas as pd

def load_data(oil_type):
    filename = f"data/{oil_type}.csv"
    df = pd.read_csv(filename)

    # Corrigir nomes (strip e lower não funcionam com acentos, então fazemos manual)
    if oil_type == "brent":
        df = df.rename(columns={
            "Data": "Date",
            "Último": "Price"
        })
        df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y", dayfirst=True, errors="coerce")
        df["Price"] = df["Price"].str.replace(",", ".").astype(float)
    else:  # wti
        df.columns = [col.strip().lower() for col in df.columns]
        df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df = df.rename(columns={"date": "Date", "price": "Price"})

    df = df[["Date", "Price"]].dropna()
    df = df.sort_values("Date")

    return df
