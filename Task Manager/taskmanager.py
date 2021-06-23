

taskList = ["testOne", "testTwo"]

def accessTasks():
    print(taskList)
    changeFunction = input("Enter:\n1 to add a task\n2 to remove a task\n:")
    if changeFunction == "1":
        addingTasks()
    else:
        removingTasks()


def addingTasks():
    taskToADD = input("Please enter your first task to your list: ")
    taskList.append(taskToADD)
    accessTasks()

def removingTasks():
    taskToREMOVE = input("Please enter a task to remove: ")
    taskList.remove(taskToREMOVE)
    accessTasks()



accessTasks()
