# The Asana center pane contains a list of tasks. These tasks are placed within rectangular blocks of size height × width, which are stacked on top of each other, and there are empty stripes of size yOffset × width left between each two consecutive blocks.

# Asana lets you use a simple click and drag motion to select multiple tasks - i.e., you can click on the first task in your desired selection, then drag the mouse to the last task in your desired selection. The selected tasks can be visualized as follows: If you join the initial and the final positions of the mouse by a line, every task block that has at least one point in common with this line is considered to be "selected".

# To test your skills, Asana engineers want you to implement a function that determines which tasks are selected based on the initial and final positions of the mouse.

# Example

# For
# dimensions = [135, 9, 1],

# tasks = ["Task 1", "Task 2", "Task 3", "Very Important Task", "Not So Important Task", "Yet Another Task", "The last task"]
# and

# mouseCoordinates = [[132, 42], 
#                     [35, 13]]
# the output should be

# solution(dimensions, tasks, mouseCoordinates) = 
#     ["Task 2", "Task 3", "Very Important Task", "Not So Important Task"]
# "Task 1" occupies the rectangle with an upper left corner at (0, 0) and a bottom right corner at (135, 9). "Task 2" is in the rectangle with corners at (0, 10) and (135, 19). The rectangle corners for the remaining tasks are as follows:

# "Task 3": (0, 20), (135, 29)
# "Very Important Task": (0, 30), (135, 39)
# "Not So Important Task": (0, 40), (135, 49)
# "Yet Another Task": (0, 50), (135, 59)
# "The last task": (0, 60), (135, 69)


def solution(dimensions, tasks, mouseCoordinates):
    width=dimensions[0]
    height = dimensions[1]
    gap = dimensions[2]
    index_list =[]

    for i in range(len(tasks)):
        
        curr_left_bottom = (i+1)*height + gap*i
        curr_left_top = i*height + i*gap
            
        for j in range(len(mouseCoordinates)):
            if mouseCoordinates[j][1] >= curr_left_top and mouseCoordinates[j][1] <=curr_left_bottom:
                index_list.append(i)
                
    
    if len(index_list)==0:
        return []
    start = min(index_list)
    end = max(index_list)
    
    return tasks[start: end+1]
                