#!/usr/bin/env python3
"""
SIMPLE USER INTERFACE
Easy menu system for beginners
"""

def main_menu():
    while True:
        print("\n" + "="*60)
        print("COMPLETE BIBLE ARCHIVE v4.0")
        print("="*60)
        print("\nMain Menu:")
        print("  1. 🔍 Search the Archive")
        print("  2. 📊 Run Analysis")
        print("  3. 📖 View Complete Document")
        print("  4. 💾 Export Data")
        print("  5. 🤖 AI Assistant (Optional)")
        print("  6. ❌ Exit")
        print()
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == "1":
            import search_system
        elif choice == "2":
            import seeds_decoder_v3
        elif choice == "3":
            print("\nOpen COMPLETE_BIBLE_ARCHIVE.html in your browser")
            input("Press Enter to continue...")
        elif choice == "4":
            print("\nExport options:")
            print("  - Check exports/ directory")
            print("  - Database: data/complete_bible.db")
        elif choice == "5":
            import tools.ai_assistant
            tools.ai_assistant.main()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
