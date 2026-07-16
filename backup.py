#!/usr/bin/env python3
"""
Backup System
Create backups of database and analysis
"""

import shutil
import datetime
import os

def create_backup():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f'backups/{timestamp}'
    
    os.makedirs(backup_dir, exist_ok=True)
    
    # Backup database
    if os.path.exists('data/complete_bible.db'):
        shutil.copy('data/complete_bible.db', backup_dir)
        print(f"✓ Database backed up to {backup_dir}")
    
    # Backup analysis
    if os.path.exists('tools/exports/seeds_decoder_v3_analysis.json'):
        shutil.copy('tools/exports/seeds_decoder_v3_analysis.json', backup_dir)
        print(f"✓ Analysis backed up to {backup_dir}")
    
    print(f"\nBackup complete: {backup_dir}")

if __name__ == "__main__":
    create_backup()
