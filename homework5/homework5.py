# --- 3.1 Vocabulary Review ---
'''
1. Git vs. GitHub: Git is the software tool for tracking changes. GitHub is the online platform where you put projects.

2. Terminal vs. Command Line: Terminal is the app you open. command line is the actual space where you type commands.

3. Local vs. Remote Repository: Local is the project folder on your computer, whereas remote is the version stored on a server like GitHub.

4. Version Control: A system that records changes to files so you can recall specific versions later.

5. Staging Area: A middle ground where you prep specific changes before officially saving them

6. git add: Adds file changes to the staging area to get them ready for a commit

7. git commit: Permanently saves your staged changes in the local repository history.

8. git push: Uploads your local commits to a remote repository on GitHub.

9. git status: Shows the current state of your working directory & staging area.

10. git pull: Fetches and merges changes from the remote repo to your local machine.

11. pwd: "Print working directory": shows the file path of where you are right now.

12. ls: "List": shows all files and folders in your current location.

13. cd: "Change directory": used to move between different folders.

14. nano: A basic text editor that lets you edit files directly in the terminal

15. touch: A quick way to create a brand-new empty file.

16. mv: "Move": used to move files to new locations/rename them.

17. rm: "Remove": deletes a file or directory

18. cat: "Concatenate": reads a file and prints the text onto your screen.
'''

# --- 3.2 A Directory Tree ---
'''
1. pwd

2. ls

3. cd ../brianna_repo and git pull

4. mv homework.py ../judy_decal/homework/

5. cd ../judy_decal/homework/

6. cat homework.py

7. git add homework.py, git commit -m "finished hw", and git push

8. git pull then git push. The error means the online/remote version has changes you don't have on your computer yet, probably from another device or person.

9. cd ~/Recent/
'''

# --- 4.1 Data Types ---
def checkDataType(val):
    return str(type(val).__name__)

# --- 4.2 Conditionals ---
def evenOrOdd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
# --- 5 Loops ---
def sumWithLoop(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

# --- 6.1 Lists --- 
def duplicateList(items):
    new_list = []
    for item in items:
        new_list.append(item)
        new_list.append(item)
    return new_list

# --- 6.2 Debugging ---
# The original code was missing a colon after the function definition and had a typo in the variable name (nu instead of num). Corrected: 
def square(num):
    return num * num

'''numbersTest = [1, 2, 3, 4]
print(sumWithLoop(numbersTest))'''