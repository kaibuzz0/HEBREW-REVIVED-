#!/usr/bin/env python3
import os
import sys

print('\n' + '='*60)
print('COMPLETE BIBLE ARCHIVE')
print('='*60)
print('\n1. Search')
print('2. View Bible')
print('3. Download')
print('4. Exit')

choice = input('\nChoice: ').strip()

if choice == '1':
    os.system('python3 tools/search_system.py')
elif choice == '2':
    print('\nOpen: downloads/MEGA_BIBLE_UNIFIED.txt')
elif choice == '3':
    print('\nVisit: downloads/index.html')
