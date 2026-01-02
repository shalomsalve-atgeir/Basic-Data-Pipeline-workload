import pandas as pd
import mysql.connector
from config import DB_CONFIG


def get_connection():
    # create database connection
    return mysql.connector.connect(**DB_CONFIG)

def read_csv(file_path):
    return pd.read_csv(file_path)

def truncate_table(table_name):
    # clears data from target table before loading fresh data goes
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"TRUNCATE TABLE {table_name}")
    conn.commit()
    conn.close()


def audit_start(process, file, table):
    # inserts a new audit record when file load starts
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO audit_log
        (process_name, file_name, table_name, start_time, status)
        VALUES (%s, %s, %s, NOW(), 'PROGRESS')
        """,
        (process, file, table)
    )
    conn.commit()
    conn.close()


def audit_success(file, table, rows):
    # updates audit record when file load completes successfully
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE audit_log
        SET end_time = NOW(),
            rows_loaded = %s,
            status = 'SUCCESS'
        WHERE file_name = %s
          AND table_name = %s
          AND end_time IS NULL
        """,
        (rows, file, table)
    )
    conn.commit()
    conn.close()


def audit_failure(file, table):
    # updates audit record if file load fails
    print("Load failed for", file, "into", table)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE audit_log
        SET end_time = NOW(),
            status = 'FAILURE'
        WHERE file_name = %s
          AND table_name = %s
          AND end_time IS NULL
        """,
        (file, table)
    )
    conn.commit()
    conn.close()


def load_df_to_table(df, table_name):
    # loads dataframe into mysql table row by row
    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(row))})",
            tuple(row)
        )

    conn.commit()
    conn.close()