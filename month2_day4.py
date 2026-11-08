import pandas as pd
import numpy as np

# A messy dataset representing an incomplete transactions feed
messy_data = {
    "tx_id": ["T1", "T2", "T3", "T4"],
    "amount": [500, np.nan, 1200, np.nan],  # ⚠️ Missing values!
    "status": ["Completed", "Completed", np.nan, "Failed"] # ⚠️ Missing status!
}

df = pd.DataFrame(messy_data)


df["amount"]=df["amount"].fillna(0)
df["status"]=df["status"].fillna("Unknown")
print(df)