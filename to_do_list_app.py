tasks=[]
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Tasks")
    print("4. Exit")
    choice=int(input("enter your choice:"))
    if (choice==1):
        task=input("enter task:")
        tasks.append(task)
        print("Task added..!")
    elif (choice==2):
        print("Tasks:",tasks)
    elif (choice==3):
        tasks.pop(int(input("enter task number to remove:"))-1)
        print("Task Removed...!")
    else:
        print("Invalid Choice!...")
        break