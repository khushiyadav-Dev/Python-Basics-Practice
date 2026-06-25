'''
Ek practical Task Manager jo:
Tasks add karta hai
List karta hai
Mark as done karta hai
JSON file mein save karta hai (data persist rehta hai)

Real-world Problem: Hamare daily tasks ko organized rakhna difficult hota hai aur agar data save na ho
to sab kuch bhul jata hai. Isko solve karne ke liye ye simple lekin powerful task manager banaya h.
'''

import json
import os
from datetime import datetime

# FILE_PATH - JSON file ka path jahan pe tasks save honge
FILE_PATH = "tasks.json"

# ============================================
# FUNCTION 1: Tasks ko JSON file se load karna
# ============================================
def load_tasks():
    """
    Ye function JSON file se sab tasks ko load karta hai
    Agar file exist nahi karta to empty list return karta hai
    
    Purpose: Data persistence - jab program dobara start ho to pichle tasks yaad rahe
    """
    try:
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'r', encoding='utf-8') as file:
                tasks = json.load(file)
                return tasks
        else:
            return []  # Agar file nahi hai to empty list return karo
    except Exception as e:
        print(f"❌ Error loading tasks: {e}")
        return []

# ============================================
# FUNCTION 2: Tasks ko JSON file mein save karna
# ============================================
def save_tasks(tasks):
    """
    Ye function tasks ko JSON file mein save karta hai
    Har baar jab new task add ho ya update ho to ye call hota hai
    
    Purpose: Data persistence - tasks kabhi loss na ho
    """
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
            print("✅ Tasks successfully saved!")
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")

# ============================================
# FUNCTION 3: Naya task add karna
# ============================================
def add_task(tasks):
    """
    User se naya task input leta hai aur tasks list mein add karta hai
    
    Task structure:
    {
        "id": unique number,
        "title": task ka naam,
        "description": task ki details,
        "priority": HIGH/MEDIUM/LOW,
        "status": "pending" ya "completed",
        "created_at": creation time,
        "due_date": deadline (optional)
    }
    """
    print("\n" + "="*50)
    print("🆕 NAYA TASK ADD KARO")
    print("="*50)
    
    try:
        # Task ka unique ID generate karo (last task ke ID + 1)
        task_id = max([task.get('id', 0) for task in tasks], default=0) + 1
        
        # User se input lo
        title = input("📝 Task ka naam dedo (title): ").strip()
        if not title:
            print("❌ Task name khaali nahi ho sakta!")
            return
        
        description = input("📄 Task ki description (optional): ").strip()
        
        # Priority select karo
        print("\n🎯 Priority select karo:")
        print("1. HIGH (Bahut important)")
        print("2. MEDIUM (Normal)")
        print("3. LOW (Kam important)")
        priority_choice = input("Priority choose karo (1/2/3): ").strip()
        
        priority_map = {"1": "HIGH", "2": "MEDIUM", "3": "LOW"}
        priority = priority_map.get(priority_choice, "MEDIUM")
        
        # Due date lo (optional)
        due_date = input("📅 Due date (YYYY-MM-DD) ya Enter skip karo: ").strip()
        
        # Naya task object create karo
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "priority": priority,
            "status": "pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": due_date if due_date else None
        }
        
        # Task ko list mein add karo
        tasks.append(new_task)
        save_tasks(tasks)
        
        print(f"\n✅ Task successfully add ho gaya! (ID: {task_id})")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# ============================================
# FUNCTION 4: Sabhi tasks ko display karna
# ============================================
def view_tasks(tasks):
    """
    Sabhi tasks ko acha format mein display karta hai
    Different filtering options provide karta hai
    """
    print("\n" + "="*50)
    print("📋 TASKS LIST")
    print("="*50)
    
    if not tasks:
        print("❌ Koi bhi task nahi hai. Naya task add karo!")
        return
    
    # Filter options
    print("\n🔍 Filter options:")
    print("1. Sabhi tasks dekho (All)")
    print("2. Sirf pending tasks")
    print("3. Sirf completed tasks")
    print("4. Priority ke hisaab se sort karo")
    
    choice = input("Choose karo (1/2/3/4): ").strip()
    
    # Filter karo
    if choice == "2":
        filtered_tasks = [t for t in tasks if t['status'] == 'pending']
        print("\n⏳ Pending Tasks:")
    elif choice == "3":
        filtered_tasks = [t for t in tasks if t['status'] == 'completed']
        print("\n✔️ Completed Tasks:")
    elif choice == "4":
        # Priority order: HIGH > MEDIUM > LOW
        priority_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
        filtered_tasks = sorted(tasks, key=lambda x: priority_order.get(x['priority'], 3))
        print("\n🎯 Tasks by Priority:")
    else:
        filtered_tasks = tasks
        print("\n📋 All Tasks:")
    
    # Tasks ko display karo
    if not filtered_tasks:
        print("❌ Is filter ke according koi task nahi mila!")
        return
    
    for i, task in enumerate(filtered_tasks, 1):
        print(f"\n{i}. 📌 ID: {task['id']} | Status: {task['status'].upper()}")
        print(f"   Title: {task['title']}")
        print(f"   Priority: {task['priority']}")
        if task['description']:
            print(f"   Description: {task['description']}")
        if task['due_date']:
            print(f"   Due Date: {task['due_date']}")
        print(f"   Created: {task['created_at']}")

# ============================================
# FUNCTION 5: Task ko mark as done/completed karna
# ============================================
def mark_task_completed(tasks):
    """
    User ID select karta hai aur vo task ko completed mark karte hain
    """
    print("\n" + "="*50)
    print("✅ TASK KO MARK AS DONE KARO")
    print("="*50)
    
    if not tasks:
        print("❌ Koi bhi task nahi hai!")
        return
    
    # Pending tasks dikhao
    pending_tasks = [t for t in tasks if t['status'] == 'pending']
    if not pending_tasks:
        print("✔️ Sab tasks pehle se completed hain!")
        return
    
    print("\n⏳ Pending Tasks:")
    for task in pending_tasks:
        print(f"ID: {task['id']} | {task['title']} | Priority: {task['priority']}")
    
    try:
        task_id = int(input("\n🆔 Task ka ID enter karo jo complete karna hai: "))
        
        # Task ko find karo
        for task in tasks:
            if task['id'] == task_id:
                if task['status'] == 'completed':
                    print(f"⚠️ Ye task pehle se completed hai!")
                    return
                
                task['status'] = 'completed'
                task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_tasks(tasks)
                print(f"✅ Task '{task['title']}' successfully completed! 🎉")
                return
        
        print("❌ Is ID ke saath koi task nahi mila!")
        
    except ValueError:
        print("❌ Please valid ID enter karo!")
    except Exception as e:
        print(f"❌ Error: {e}")

# ============================================
# FUNCTION 6: Task ko delete karna
# ============================================
def delete_task(tasks):
    """
    User ID select karta hai aur vo task ko delete karte hain
    """
    print("\n" + "="*50)
    print("🗑️ TASK KO DELETE KARO")
    print("="*50)
    
    if not tasks:
        print("❌ Koi bhi task nahi hai!")
        return
    
    # Sabhi tasks ID ke saath dikhao
    print("\n📋 Available Tasks:")
    for task in tasks:
        print(f"ID: {task['id']} | {task['title']} | Status: {task['status']}")
    
    try:
        task_id = int(input("\n🆔 Delete karne ke liye task ID enter karo: "))
        
        # Task ko find aur delete karo
        for i, task in enumerate(tasks):
            if task['id'] == task_id:
                deleted_task = tasks.pop(i)
                save_tasks(tasks)
                print(f"✅ Task '{deleted_task['title']}' successfully delete ho gaya! ❌")
                return
        
        print("❌ Is ID ke saath koi task nahi mila!")
        
    except ValueError:
        print("❌ Please valid ID enter karo!")
    except Exception as e:
        print(f"❌ Error: {e}")

# ============================================
# FUNCTION 7: Task ko edit/update karna
# ============================================
def edit_task(tasks):
    """
    Existing task ko edit karta hai - title, description, priority change kar sakte ho
    """
    print("\n" + "="*50)
    print("✏️ TASK KO EDIT KARO")
    print("="*50)
    
    if not tasks:
        print("❌ Koi bhi task nahi hai!")
        return
    
    # Sabhi tasks dikhao
    print("\n📋 Available Tasks:")
    for task in tasks:
        print(f"ID: {task['id']} | {task['title']}")
    
    try:
        task_id = int(input("\n🆔 Edit karne ke liye task ID enter karo: "))
        
        # Task ko find karo
        for task in tasks:
            if task['id'] == task_id:
                print(f"\n📝 Current Title: {task['title']}")
                new_title = input("Naya title enter karo (Enter se skip): ").strip()
                if new_title:
                    task['title'] = new_title
                
                print(f"📄 Current Description: {task.get('description', 'None')}")
                new_description = input("Naya description enter karo (Enter se skip): ").strip()
                if new_description:
                    task['description'] = new_description
                
                print(f"🎯 Current Priority: {task['priority']}")
                print("1. HIGH  2. MEDIUM  3. LOW")
                priority_choice = input("Naya priority enter karo (Enter se skip): ").strip()
                priority_map = {"1": "HIGH", "2": "MEDIUM", "3": "LOW"}
                if priority_choice in priority_map:
                    task['priority'] = priority_map[priority_choice]
                
                task['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_tasks(tasks)
                print(f"✅ Task successfully update ho gaya!")
                return
        
        print("❌ Is ID ke saath koi task nahi mila!")
        
    except ValueError:
        print("❌ Please valid ID enter karo!")
    except Exception as e:
        print(f"❌ Error: {e}")

# ============================================
# FUNCTION 8: Statistics dikhana
# ============================================
def show_statistics(tasks):
    """
    Tasks ke baare mein stats dikhata hai
    Total tasks, completed, pending, high priority tasks, etc.
    """
    print("\n" + "="*50)
    print("📊 TASK STATISTICS")
    print("="*50)
    
    if not tasks:
        print("❌ Koi bhi task nahi hai!")
        return
    
    total = len(tasks)
    completed = len([t for t in tasks if t['status'] == 'completed'])
    pending = len([t for t in tasks if t['status'] == 'pending'])
    high_priority = len([t for t in tasks if t['priority'] == 'HIGH'])
    
    completion_percentage = (completed / total * 100) if total > 0 else 0
    
    print(f"\n📈 Overview:")
    print(f"   Total Tasks: {total}")
    print(f"   ✅ Completed: {completed}")
    print(f"   ⏳ Pending: {pending}")
    print(f"   🎯 High Priority: {high_priority}")
    print(f"   📊 Completion Rate: {completion_percentage:.1f}%")
    
    # Progress bar
    print(f"\n   Progress: ", end="")
    filled = int(completion_percentage / 5)
    print("█" * filled + "░" * (20 - filled) + f" {completion_percentage:.1f}%")

# ============================================
# MAIN MENU
# ============================================
def main_menu():
    """
    Main menu jo har option show karta hai aur user input leta hai
    """
    tasks = load_tasks()  # Start mein tasks load karo
    
    while True:
        print("\n" + "="*50)
        print("📌 TASK MANAGER - MAIN MENU")
        print("="*50)
        print("\n1. ➕ Add New Task")
        print("2. 📋 View All Tasks")
        print("3. ✅ Mark Task as Completed")
        print("4. ✏️ Edit Task")
        print("5. 🗑️ Delete Task")
        print("6. 📊 View Statistics")
        print("7. 🚪 Exit")
        
        choice = input("\nChoose an option (1-7): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            show_statistics(tasks)
        elif choice == "7":
            print("\n👋 Goodbye! Keep being productive! 🚀")
            break
        else:
            print("❌ Invalid choice! Please enter 1-7")
        
        input("\n📌 Press Enter to continue...")

# ============================================
# PROGRAM START
# ============================================
if __name__ == "__main__":
    print("\n🎉 Welcome to TASK MANAGER! 🎉")
    print("Apne sab tasks ko organized rakho aur productive bano!")
    main_menu()
