import pytest
import os
# Import your class (Assumes your main file is named 'main.py' or similar)
# If your main file is named 'todo.py', change this to: from todo import TaskManager
from to_do import TaskManager 

def test_add_and_save_task(tmp_path):
    # 1. SETUP: Create a fake file path in the temporary folder
    # tmp_path is a special variable pytest gives us automatically
    fake_file = tmp_path / "test_tasks.txt"
    
    # 2. INITIALIZE: Start the manager with the FAKE file
    # We pass the weird path variable strictly as a string
    manager = TaskManager(filename=str(fake_file))
    
    # 3. ACTION: Add a task
    manager.add_task("Test Task 1")
    
    # Check memory (Did it add to the list?)
    assert "Test Task 1" in manager.tasks
    
    # 4. ACTION: Save to disk
    manager.save_data()
    
    # 5. VERIFY: Read the fake file to see if it actually wrote it
    with open(fake_file, "r") as f:
        content = f.read()
        
    # Check the file content
    assert "Test Task 1" in content