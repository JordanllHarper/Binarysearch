from taskClass import Task

taskList = [

]


def startup():
    startupTaskList = [
        [],
        [],
        [],


    ]
    file = open("C:\\Users\\jorda\\PycharmProjects\\Learning\\Task Manager\\storage.txt", "r")


   # navigation()


def navigation():
    userChoice = input(
        "Enter 1. to view tasks\n"
        "Enter 2. to create a new task\n"
        "Enter 3. to delete a task\n"
        "Enter 4. to exit\n")
    if userChoice == "1":
        seeTasks(1)
    elif userChoice == "2":
        createNewTask()
    elif userChoice == "3":
        deleteTask(1)
    elif userChoice == "4":
        quitProgram()
    else:
        print("Please enter a valid choice.")
        navigation()


def seeTasks(whereToGoAfter):
    count = 0
    for eachTask in taskList:
        count += 1
        print("This is task " + str(count))
        print(str(eachTask.taskName) + " | " + str(eachTask.dueDate) + " | " + str(eachTask.priorityLevel))
    if whereToGoAfter == 1:
        navigation()
    else:
        deleteTask(2)


def createNewTask():
    taskName = str(input("Enter a task you wish to complete: "))
    dueDate = str(input("Enter the due date of the task (in DD/MM/YYYY format): "))
    priorityLevel = str(input("Enter a priority level for the task: "))
    task = Task(taskName, dueDate, priorityLevel)
    taskList.append(task)
    navigation()


def deleteTask(whereToGo):
    def seeTaskToDelete():
        seeTasks(2)
        deleting()

    def deleting():
        taskToDelete = int(input("Enter task to delete: "))
        taskList.pop(taskToDelete - 1)

        navigation()

    if whereToGo == 1:
        seeTaskToDelete()
    else:
        deleting()


def quitProgram():
    file = open("C:\\Users\\jorda\\PycharmProjects\\Learning\\Task Manager\\Storage.txt", "w")

    for eachTask in taskList:
        file.write(str(eachTask.taskName) + "\n")
        file.write(str(eachTask.dueDate) + "\n")
        file.write(str(eachTask.priorityLevel) + "\n")

    quit()


startup()
