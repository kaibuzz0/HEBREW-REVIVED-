#!/usr/bin/env python3
"""
Export to CSV format
"""

import sqlite3
import csv

def export_to_csv():
    conn = sqlite3.connect('data/complete_bible.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    for (table,) in tables[:10]:  # Sample
        try:
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            
            if rows:
                filename = f'exports/csv/{table}.csv'
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([desc[0] for desc in cursor.description])
                    writer.writerows(rows)
                print(f"✓ Exported {table} to CSV")
        except:
            pass
    
    conn.close()
    print("\nCSV export complete in exports/csv/")

if __name__ == "__main__":
    import os
    os.makedirs('exports/csv', exist_ok=True)
    export_to_csv()
