


import json

class User():
    def __init__(self, name, age, filename):
        self.name = name
        self.age = age
        self.tasks = self.load_tasks(filename)
        print(self.greeting())
        self.filename = filename

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)

        except Exception as e:
            print(e)

        finally:
            print("Loading tasks.....")

    def greeting(self):
        return f"hi {self.name} enjoy this app it's made for you"



class ToDo(User):
    def __init__(self, name, age, filename):
        super().__init__(name, age, filename) #--->inheritance


    def show_tasks(self):
        print()
        task_list = self.tasks["tasks"]
        
        if len(task_list) == 0:
            print("No tasks for yet")
        for idx, task in enumerate(task_list):
            statue = "[completed]" if task["complete"] else "[STILL]"
            print(f"task {idx+1} -> {task['description']} | {statue} |")

    def add_task(self):
        self.show_tasks()
        description = input("Enter task description: ")
        self.tasks["tasks"].append({"description": description, "complete": False})
        self.save_tasks()

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

    def remove_tasks(self):
        self.show_tasks()
        user_input = input("Task do u want to remove by here title: ")
        try:
            self.tasks["tasks"] = [task for task in self.tasks["tasks"] if task["Title"] != user_input]
            self.save_tasks()
        except Exception as e:
            print(f"Error occurred while removing task: {e}")

    def update_tasks(self):
        self.show_tasks()
        user_input = input("Enter the title of the task you want to update: ")
        for task in self.tasks["tasks"]:
            if task["Title"] == user_input:
                user = input("Do u want to change the description (yes or no): ").lower()
                if user == "yes":
                    new_description = input("Enter the new description: ")
                    task["description"] = new_description
                    self.save_tasks()
                    break
                task["complete"] = not task["complete"]
        else:
            print("Task not found.")

def main(run):
    print("Welcome to your to do list app what do you want to do")
    while True:
        print("1:" "show tasks",
              "2:" "add task",
              "3:" "remove task",
              "4:" "update task",
              "5:" "Exit")

        user_input = input("Enter by number: ")
        if user_input == "1":
            run.show_tasks()

        elif user_input == "2":
            run.add_task()

        elif user_input == "3":
            run.remove_tasks()

        elif user_input == "4":
            run.update_tasks()

        elif user_input == "5":
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Try to enter a valid number")


if __name__=='__main__':
    name = input("Name: ")
    age = input("Age: ")
    filename = "to_do_list.json"
    user = ToDo(name, age, filename)
    main(user)
    
