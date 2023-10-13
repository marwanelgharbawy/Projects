/*
 * File: TaskManager.c
 * Author: Marwan El-Gharbawy
 * Description: Task manager program where the user can add, remove tasks or mark them as complete.
 *              Task and description limits can be easily modified in the "Macros" section.
 *              Tasks are shown in table format.
 * Date: 14 August 2023
 */

/* Header Files */
#include <stdio.h>   // Standard I/O functions
#include <stdbool.h> // Boolean data types

/* Macros */
#define MAX 25 // Max number of tasks
#define DES 35 // Max number of characters for each description

/* Function Declarations */

/**
 * @brief Show tasks in table format
 *
 * @param Tasks Descriptions of tasks
 * @param Status Status of tasks if completed or not
 * @param Counter Number of tasks
 * @param Option The option to print complete (1) incomplete (2) or all tasks (0)
 */
void table(char task[MAX][DES], bool done[MAX], int counter, int table_option);

/* Main Function */
int main()
{
    int option;               // For the option for each case (add,view,mark,...)
    int viewkey;              // For the option for each view case (view all, view completed,...)
    int doneflag;             // Used in view and mark cases
    int counter = 0;          // Task counter
    int rem;                  // Task ID to be removed
    char task[MAX][DES];      // Task Description
    bool done[MAX] = {false}; // Task status

    printf("Task Manager\n\n");

    // Program: The user will be prompted with the previous options, each one will be executed in switch cases

    do // Looping until program ends
    {
        printf("1. Add Task\n");
        printf("2. View Tasks\n");
        printf("3. Mark task as complete\n");
        printf("4. Remove Task\n");
        printf("5. Exit\n\n");
        printf("Select option: ");
        scanf("%d", &option);

        switch (option) // Depending on option, it will execute the desired case
        {
        case 1:

            if (counter == MAX) // Task counter reached max
            {
                printf("Task limit (%d) reached.\n\n", MAX);
                break;
            }

            // Add task

            printf("Enter task description: ");
            scanf("\n");
            scanf("%[^\n]", task[counter]);
            counter++; // Incrementing task counter
            printf("Task added successfully!\n\n");
            break;

        case 2:

            // View tasks

            if (counter == 0) // Task counter is null
            {
                printf("There are no tasks.\n\n");
                break;
            }

            printf("1. View all tasks\n");
            printf("2. View complete tasks\n");
            printf("3. View incomplete tasks\n");
            printf("4. Return to previous menu\n\n");

            do
            {
                printf("Select view option: ");
                scanf("%d", &viewkey); // Depending on viewkey, it will execute the desired case

                if (viewkey == 1)
                {
                    // View all tasks
                    // Calling function with option 0: showing all tasks

                    table(task, done, counter, 0);
                }
                else if (viewkey == 2)
                {
                    // View complete

                    doneflag = 0;

                    // The following loop will check if there's any complete tasks

                    for (int i = 0; i < counter; i++)
                    {
                        if (done[i])
                            doneflag = 1; // This flag is set to 1 when finding a complete task
                    }

                    if (doneflag)
                    {
                        // Calling function with option 1: showing complete tasks
                        table(task, done, counter, 1);
                    }
                    else
                    {
                        // This message will be displayed when the flag is set to 0
                        printf("There are no complete tasks.\n\n");
                    }
                }
                else if (viewkey == 3)
                {
                    // View incomplete

                    doneflag = 0;

                    for (int i = 0; i < counter; i++)
                    {
                        if (!done[i])
                            doneflag = 1;
                    }

                    if (doneflag)
                    {
                        // Calling function with option 2: showing incomplete tasks
                        table(task, done, counter, 2);
                    }
                    else
                    {
                        printf("There are no incomplete tasks. Great job, you've finished everything!\n\n");
                    }
                }
                else if (viewkey == 4)
                {
                    // Exit to main menu
                    break;
                }
                else
                    printf("Wrong option, try again.\n\n"); // Will be reprompted for view option

            } while (viewkey < 1 || viewkey > 4); // Looping in case the user entered a wrong value, reprompting

            break;

        case 3:

            // Mark task as complete

            if (counter == 0) // Task counter is null
            {
                printf("There are no tasks.\n\n");
                break;
            }

            printf("Enter task ID to mark as complete: ");
            scanf("%d", &doneflag); // Using this variable as an index to mark tasks as done

            if ((doneflag <= counter) && (doneflag > 0)) // To make sure task already exists
            {
                if (done[doneflag - 1] == true) // If it's already marked as complete
                {
                    printf("Task has already been completed before.\n\n"); // Generating a more logical message
                }
                else
                {
                    done[doneflag - 1] = true; // Setting task to True
                    printf("Task done!\n\n");
                }
            }
            else
            {
                printf("Task doesn't exist.\n\n");
            }
            break;

        case 4:

            // Remove task

            if (counter == 0) // Task counter is null
            {
                printf("There are no tasks.\n\n");
                break;
            }

            printf("Enter task ID to remove: ");
            scanf("%d", &rem);

            if ((rem > counter) || (rem < 1)) // Case where task ID doesn't exist
            {
                printf("Task doesn't exist.\n\n");
                break;
            }
            else if (rem == counter)
            {
                // If the task to be removed is the last one, decrementing task counter

                counter--;
                done[rem - 1] = false; // Resetting task if it was marked as done
            }
            else
            {
                // To remove a task, its following tasks will be copied to the ones before

                for (int i = (rem - 1); i < counter; i++)
                {
                    // Copying task status and description to previous ones

                    // Copying status
                    done[i] = done[i + 1];

                    // Copying description
                    for (int j = 0; j < DES; j++)
                    {
                        task[i][j] = task[i + 1][j];
                    }
                }
                done[counter] = false; // Resetting last task in case it was done
                counter--;             // Decrementing task counter
            }
            printf("Task removed successfully!\n\n");
            break;

        case 5:

            // Exit program

            printf("Exiting Task Manager. Have a great day!\n");
            break;

        default:
            printf("Wrong option, try again.\n\n");
        }
    } while (option != 5); // The program will end if the input was 5, after printing the exit message
}

/* Function Definitions */
// Showing data in a table

void table(char task[MAX][DES], bool done[MAX], int counter, int table_option)
{
    // Printing in table format

    // Printing title

    if (table_option == 0) // Show all
    {
        printf("\nAll tasks:\n");
    }
    else if (table_option == 1) // Show completed
    {
        printf("\nComplete tasks:\n");
    }
    else if (table_option == 2) // Show incompleted
    {
        printf("\nIncomplete tasks:\n");
    }

    printf("\nTask ID \tStatus   \tDescription\n");

    for (int i = 0; i < counter; i++)
    {

        if (table_option == 1) // Show completed
        {
            if (!done[i])
                continue; // The loop will skip the iteration if the task is incomplete
        }
        else if (table_option == 2) // Show incompleted
        {
            if (done[i])
                continue; // The loop will skip the iteration if the task is complete
        }

        // The table_option variable would be set to 0 if showing all tasks, not skipping anything

        // Printing task ID

        printf("%d         \t", i + 1);

        // Printing status

        if (done[i])
        {
            printf("Complete  \t");
        }
        else
        {
            printf("Incomplete\t");
        }

        // Printing Description

        printf("%s\n", task[i]);
    }
    printf("\n");
}