import os # We need this to check if file exists

class TaskManager:
    def __init__(self):
        self.filename = "mytasks.txt"
        self.tasks = [] # This list will hold our data
        self.load_data() # Load automatically when object is created!

    def load_data(self):
       try:
           with open(self.filename , "r") as f:
               for line in f:
                   clean_task = line.strip()
                   self.tasks.append(clean_task)
               print("Previous tasks loaded!")
       except FileNotFoundError:
            print("No previous tasks found.")

    def save_data(self):
       with open (self.filename , "w") as f:
          for task in self.tasks:
            f.write(task + '\n')
       print("Data Saved Successfully!")
           
    

    def add_task(self, task_name):
        self.tasks.append(task_name)
        print("Task added successfully!")

    def view_tasks(self):
        # LOGIC:
        if len(self.tasks)==0:
            print('your to-do-list is empty')
        else :
            print('\n your tasks')
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
        

# --- THE MAIN MENU LOOP (I wrote this part for you) ---
manager = TaskManager()

while True:
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Save & Exit")
    
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        t = input("Enter task name: ")
        manager.add_task(t)
    elif choice == "2":
        manager.view_tasks()
    elif choice == "3":
        manager.save_data()
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")