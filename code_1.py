from util import *
from config import DATA_PATH, PROCESS_NAME

FILES_TO_LOAD = [
    ("campaigns.csv", "raw_campaigns"),
    ("customers.csv", "raw_customers"),
    ("customer_reviews_complete.csv", "raw_customer_reviews"),
    ("interactions.csv", "raw_interactions"),
    ("support_tickets.csv", "raw_support_tickets"),
    ("transactions.csv", "raw_transactions")
]

for file_name, table_name in FILES_TO_LOAD:
    try:
        print("Starting load for", file_name)
        audit_start(PROCESS_NAME, file_name, table_name)

        df = read_csv(DATA_PATH + file_name)
        truncate_table(table_name)
        load_df_to_table(df, table_name)
        audit_success(file_name, table_name, len(df))

        print("Completed load for", file_name)

    except Exception as e:
        audit_failure(file_name, table_name)
        print("Error while loading", file_name)
        print(e)
