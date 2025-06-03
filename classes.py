"""
Muhammad Rafie 2025
"""
import math
import random


class Goal:
    """
    Class containing a goal's title, description, and date.

    Instance Attributes:
        - title: goal title
        - desc: goal description
        - date: goal deadline
        - status: goal completion state
        - status_icon: ...

    Representation Invariants:
    """
    title: str
    desc: str
    date: str
    status: bool
    status_icon: str

    def __init__(self, title: str, desc: str, date: str) -> None:
        self.title = title
        self.desc = desc
        self.date = date
        self.status = False
        self.status_icon = ''


class ToDoContainer:
    """
    Class containing...

    Instance Attributes:
        - progress: percentages of tasks done
        - goal_list: list of all set goals
        - length: number of set goals
        - completed: number of completed goals
        - ongoing: running status of program

    Representation Invariants:
        - self.length >= self.completed
    """
    progress: float
    goal_list: list[Goal]
    length: int
    completed: int
    ongoing: bool

    def __init__(self) -> None:
        self.progress = 0
        self.goal_list = []
        self.length = 0
        self.completed = 0

        self.ongoing = True

    def update_status(self) -> None:
        if self.length != 0:
            self.progress = (self.completed / self.length) * 100
        else:
            self.progress = 0

    def add_goal(self, title: str, desc: str, date: str) -> None:
        new_goal = Goal(title, desc, date)

        self.goal_list.append(new_goal)
        self.length += 1
        self.update_status()

    def remove_goal(self, index: int) -> None:
        removed_goal = self.goal_list.pop(index)

        if removed_goal.status:
            self.completed -= 1
        self.length -= 1
        self.update_status()

    def complete_goal(self, index: int) -> None:
        completed_goal = self.goal_list[index]
        completed_goal.status = True
        completed_goal.status_icon = ' ☺'

        self.completed += 1
        self.update_status()


if __name__ == '__main__':
    todo = ToDoContainer()

    available_options = ['add goal', 'remove goal', 'complete goal', 'view goal', 'exit']

    mottos = ['Keep going!', "You're doing great!", "Keep up the pace!", "You're awesome!",
              'Youre almost there!']

    while todo.ongoing:
        print("========")
        print(" ")
        # Progress Bar
        percent = math.floor(todo.progress)
        print("My Progress:")
        print('▓' * percent + '░' * (100 - percent) + ' ' + str(percent) + '% ' + '| ' + mottos[random.randint(0,
                                                                                                              len(mottos) - 1)])
        # Goal Container
        print(" ")
        print("My Goals:")

        if todo.length == 0:
            print("I have none!")

        for i in range(todo.length):
            print(str(i + 1) + '. ' + todo.goal_list[i].title + todo.goal_list[i].status_icon)

        # Option Container
        print(" ")
        print("========")

        print("What would you like to do?")
        print("You are able to:")
        for option in available_options:
            print("-" + option)

        choice = input("\nEnter action: ").lower().strip()
        while choice not in available_options:
            print("That was an invalid option; try again.")
            choice = input("\nEnter action: ").lower().strip()

        print("========")
        print("You decided to:", choice)

        # Choice selection

        if choice == 'add goal':
            title = input("\nEnter title: ")
            desc = input("\nEnter description: ")
            date = input("\nEnter date: ")

            todo.add_goal(title, desc, date)
            print("Successfully added goal!")


        elif choice == 'remove goal':
            if todo.length != 0:
                choice = input("\nEnter goal number: ")
                while int(choice) > todo.length or int(choice) < 1:
                    print("That was an invalid option; try again.")
                    choice = input("\nEnter goal number: ")

                todo.remove_goal(int(choice) - 1)
                print("Successfully removed goal!")
            else:
                print("You have no goals!")

        elif choice == 'complete goal':
            choice = input("\nEnter goal number: ")
            while int(choice) > todo.length or int(choice) < 1:
                print("That was an invalid option; try again.")
                choice = input("\nEnter goal number: ")

            todo.complete_goal(int(choice) - 1)
            print("Successfully completed goal!")

        elif choice == 'view goal':

            print("Type the number associated with the goal:")
            choice = input("\nEnter goal number: ")
            while int(choice) > todo.length or int(choice) < 1:
                print("That was an invalid option; try again.")
                choice = input("\nEnter goal number: ")

            goal_object = todo.goal_list[int(choice) - 1]

            print("========")
            print(goal_object.title + goal_object.status_icon)
            print("--------")
            print(goal_object.desc)
            print("Due by:" + '' + goal_object.date)
            print("========")

        elif choice == 'exit':
            # Add more here
            todo.ongoing = False
