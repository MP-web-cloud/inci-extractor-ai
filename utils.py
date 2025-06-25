import pandas as pd
import os

def load_inci_base(path="inci_base.csv"):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        return pd.DataFrame(columns=["INCI"])

def update_inci_base(new_incis, path="inci_base.csv"):
    df = load_inci_base(path)
    existing = set(df["INCI"].str.lower())
    new_cleaned = [inci for inci in new_incis if inci.lower() not in existing]
    new_df = pd.DataFrame({"INCI": new_cleaned})
    updated_df = pd.concat([df, new_df], ignore_index=True)
    updated_df.to_csv(path, index=False)
    return new_cleaned
