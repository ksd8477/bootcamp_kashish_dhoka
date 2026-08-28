def clean_column_names(df):
    """
    Standardizes dataframe column names: lowercase, no spaces, no extra whitespace.
    """
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df