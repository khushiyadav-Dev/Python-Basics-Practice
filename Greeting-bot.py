import datetime
import platform

def greeting_assistant():
    # User se naam poochna
    name = input("Enter your name: ")
    
    # Current time nikalna
    current_time = datetime.datetime.now()
    hour = current_time.hour
    
    # Time ke hisaab se wish karna
    if hour < 12:
        wish = "Good Morning"
    elif 12 <= hour < 18:
        wish = "Good Afternoon"
    else:
        wish = "Good Evening"
        
    print(f"\n--- Hello {name}! {wish}! ---")
    print(f"Today's Date: {current_time.strftime('%d-%B-%Y')}")
    print(f"Current Time: {current_time.strftime('%I:%M %p')}")
    
    # System ki info (AI feel dene ke liye)
    print("\n[System Diagnosis]")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print("Status: All systems are operational. Ready to help you, Khushi!")

if __name__ == "__main__":
    greeting_assistant()
  
