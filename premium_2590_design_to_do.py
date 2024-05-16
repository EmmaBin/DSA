# Design a Todo List Where users can add tasks, mark them as complete, or get a list of pending tasks. Users can also add tags to tasks and can filter the tasks by certain tags.

# Implement the TodoList class:

# TodoList() Initializes the object.
# int addTask(int userId, String taskDescription, int dueDate, List < String > tags)
# Adds a task for the user with the ID userId with a due date equal to dueDate and a list of tags attached to the task.
# The return value is the ID of the task. This ID starts at 1 and is sequentially increasing.
# That is, the first task's id should be 1, the second task's id should be 2, and so on.

# List < String > getAllTasks(int userId) Returns a list of all the tasks not marked as complete for the user with ID userId,
# ordered by the due date. You should return an empty list if the user has no uncompleted tasks.
# List < String > getTasksForTag(int userId, String tag) Returns a list of all the tasks that are not marked as complete for the user with the ID userId and have tag as one of their tags,
# ordered by their due date. Return an empty list if no such task exists.
# void completeTask(int userId, int taskId) Marks the task with the ID taskId as completed only if the task exists and the user with the ID userId has this task,
# and it is uncompleted.


class TodoList:
    # todo={
    #     userID:{
    #         task1:{
    #             completed:bool,
    #             descrption:string,
    #             duedate:int,
    #             tags:[]
    #         },
    #         task2:{

    #         }
    #     },
    #      anotherUser:{

    # }
    # }

    def __init__(self):
        self.taskId = 1
        self.todo = {}

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:

        if userId not in self.todo:
            self.todo[userId] = {}
        self.todo[userId][self.taskId] = {
            'completed': False,
            'description': taskDescription,
            'due': dueDate,
            'tags': tags
        }
        self.taskId += 1
        return self.taskId - 1

    def getAllTasks(self, userId: int) -> List[str]:
        result = []
        if userId in self.todo:
            sorted_tasks = sorted(
                self.todo[userId].items(), key=lambda x: x[1]['due'])
            for taskId, task in sorted_tasks:
                if not task['completed']:
                    result.append(task['description'])
        return result

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        result = []
        if userId in self.todo:
            sorted_tasks = sorted(
                self.todo[userId].items(), key=lambda x: x[1]['due'])
            for taskId, task in sorted_tasks:
                if not task['completed'] and tag in task['tags']:
                    result.append(task['description'])
        return result

    def completeTask(self, userId: int, taskId: int) -> None:
        if userId in self.todo and taskId in self.todo[userId]:
            self.todo[userId][taskId]['completed'] = True

# 注意：
# sorted_tasks return list of tuples look like this:
# [
#     (11, {'completed': True, 'description': 'Finish project', 'due': 20230518, 'tags': ['work']}),
#     (13, {'completed': False, 'description': 'Call mom', 'due': 20230519, 'tags': ['personal']}),
#     (12, {'completed': False, 'description': 'Buy groceries', 'due': 20230520, 'tags': ['home']}),
#     (10, {'completed': False, 'description': 'Read book', 'due': 20230522, 'tags': ['personal']})
# ]
