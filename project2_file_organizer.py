'''
Ek Desktop Cleaner jo automatically files ko unke type ke hisaab se folders mein sort kar deta hai (Images, Documents, Videos, etc.) + date-wise organization.
Bahut useful hai real life mein jab downloads folder mess ho jata hai.
'''

import os
import shutil
from datetime import datetime
from pathlib import Path

# File types dictionary - har file extension ko category mein map karte hain
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.txt'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.wma'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c']
}

def get_file_category(filename):
    """
    File ka extension check karke uska category return karte hain
    Args: filename (str)
    Return: category name ya 'Others'
    """
    # File ka extension nikaalte hain
    file_extension = os.path.splitext(filename)[1].lower()
    
    # Sab categories ko check karte hain
    for category, extensions in FILE_TYPES.items():
        if file_extension in extensions:
            return category
    
    # Agar koi match nahi hota toh 'Others' return karte hain
    return 'Others'

def get_date_folder(file_path):
    """
    File ke creation date se date-wise folder name banate hain (YYYY-MM-DD format)
    Args: file_path (str)
    Return: date string (YYYY-MM-DD)
    """
    # File ka creation time nikaalte hain (timestamps mein)
    file_creation_time = os.path.getctime(file_path)
    
    # Timestamp ko date format mein convert karte hain
    date_created = datetime.fromtimestamp(file_creation_time).strftime('%Y-%m-%d')
    
    return date_created

def organize_files(source_folder):
    """
    Source folder ke andar sab files ko organize karte hain
    Pehle category folder, phir date folder banate hain
    Args: source_folder (str) - organize karne wala folder path
    """
    
    # Agar folder exist nahi karta toh error dete hain
    if not os.path.isdir(source_folder):
        print(f"❌ Folder '{source_folder}' exist nahi karta!")
        return
    
    # Source folder mein sab files aur folders nikaalte hain
    items = os.listdir(source_folder)
    
    # Counter - kitne files organize hue
    organized_count = 0
    
    # Har item ko process karte hain
    for item in items:
        item_path = os.path.join(source_folder, item)
        
        # Agar yeh file hai (folder nahi)
        if os.path.isfile(item_path):
            # File ka category nikaalte hain (Images, Documents, etc.)
            category = get_file_category(item)
            
            # File ke creation date se date folder nikaalte hain
            date_folder = get_date_folder(item_path)
            
            # Category folder ka path banate hain
            category_folder = os.path.join(source_folder, category)
            
            # Date folder ka full path banate hain (Category ke andar)
            date_path = os.path.join(category_folder, date_folder)
            
            # Agar folder exist nahi karta toh banate hain
            os.makedirs(date_path, exist_ok=True)
            
            # File ko new location pe move karte hain
            destination = os.path.join(date_path, item)
            shutil.move(item_path, destination)
            
            # Confirmation print karte hain
            print(f"✅ Moved: {item} → {category}/{date_folder}/")
            organized_count += 1
    
    # Summary print karte hain
    print(f"\n🎉 Total files organized: {organized_count}")

def main():
    """
    Main function - user se input lete hain aur organize karte hain
    """
    print("=" * 50)
    print("📁 Desktop File Organizer 📁")
    print("=" * 50)
    
    # User se folder path input lete hain
    folder_path = input("\nEnter folder path to organize (ya Downloads likho): ").strip()
    
    # Agar user 'Downloads' likhe toh home folder ka Downloads use karte hain
    if folder_path.lower() == 'downloads':
        folder_path = os.path.expanduser('~/Downloads')
    
    # Confirmation lete hain
    print(f"\n📂 Organizing folder: {folder_path}")
    confirm = input("Kya aap sure hain? (yes/no): ").lower()
    
    if confirm == 'yes':
        organize_files(folder_path)
    else:
        print("❌ Operation cancelled!")

# Script run karte hain jab directly execute ho
if __name__ == "__main__":
    main()
