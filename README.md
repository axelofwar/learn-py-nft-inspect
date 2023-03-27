# Learn Collaborative Development

Class: Decode
Created: February 25, 2023 4:15 PM
Materials: https://discord.gg/f2C9tqt5gp
Type: Tutorial
For web version w/ images: 
Lesson 1: [Github and Project Management](https://axelofwar.notion.site/Decode-GitHub-Project-Management-cbe607bf786d4edf8abcbba4cc3da2e3)

Lesson 2: [Integrated Development Environments](https://axelofwar.notion.site/Decode-IDEs-3f566c7ab0f3452ca44ddce00299f45e)

Lesson 3: [Python Classic Setup](https://www.notion.so/axelofwar/Decode-Start-w-Python-classic-4d3cdd449e784c92802e1a2f72117b3d?pvs=4)

Lesson 4: [Python Anaconda Setup](https://www.notion.so/axelofwar/Decode-Start-w-Python-Anaconda-de41de7c48574e94b00ab45c3245463b?pvs=4)
# Welcome to Decode’s coding Journey!

My name is Axelofwar and I’m extremely excited to welcome you to Day 1 - Learn Collaborative Development! There are a ton of languages and frameworks used in modern day development that can make the coding landscape feel very broad and sometimes even scary. Before we dive into any of those, there are some basics to understand about the coding environment and working with other developers on a project. We’ll start with some of these common tools that enable any developer to contribute - regardless of language or framework.

- Topics Covered
  - **GitHub** and Project Management
  - **IDEs** and Coding Environments

Agile and Scrum: these are development methodologies that help teams work together more efficiently. Agile is a philosophy that emphasizes working in small, iterative cycles and prioritizing customer feedback. Scrum is a specific implementation of Agile that divides work into sprints, which are short periods of time where the team focuses on a specific set of tasks. Each sprint ends with a review of what was accomplished and a planning meeting for the next sprint. The goal is to create a flexible and collaborative work environment that encourages continuous improvement.

## How to use GitHub for beginners

GitHub is a web platform used for version control and collaboration. It can also be for project management! Here are some terms for getting started:

**Terms** - there’s tons of terminology that gets used in the dev world but I’ll try to break down some of the most important into two categories - Agile/Scrum terms and GitHub terms (more on those later).

- Agile/Scrum terms:
  - Board - the total sum of tasks needed to complete a project (completed and ongoing)
    - Example: This is an example project from github’s native project management software! Here we have a project board showing all the tasks and stories related to our example project!
      ![Screenshot 2023-02-25 at 6.02.52 PM.png](Learn%20Collaborative%20Development%20cbe607bf786d4edf8abcbba4cc3da2e3/Screenshot_2023-02-25_at_6.02.52_PM.png)
      We will look at using Agile/Scrum terms moving forward, but our examples will utilize the GitHub projects section shown above - which is their native project management tool.
  - Sprint - the amount of time assigned to an iterative cycle.
  - Story - the overarching goal of the work assigned to a developer for that iterative cycle. This can be small tasks or bigger jobs broken into tasks.
  - Task - the components that go into a story. The goal of a story may need more than once script written to accomplish it, in which case you would have multiple tasks assigned to the same story.
  - Backlog - the stories marked for development but not marked as immediate priority. As a developer finishes their stories or tasks for the sprint, if their is time left they will in the sprint they will often refer to the backlog for other tasks they can pick up in the interim if they believe it can be completed within the sprint.
    - Common practice is to aim to complete all stories within a given sprint - and if you aren’t able, to then adjust the story size in into smaller tasks or break it up across multiple sprints and push to backlog.
  - Stages - Ready, In progress, In review, and Done are key stages that help a reviewer or approver of code identify where in a project’s lifecycle, and where in the development cycle, the code is. Use these sections of the board to indicate to an approver what stage you are in of your development and to request input/review
- GitHub terms:

  - Repository - the location or file system where code is stored online
  - Branch - think of your code repository as a tree. The _main_ branch is the root of the tree, this is where the core of development happens and where production environments will go to find ready to use code. _Other_ branches can be created off of the main branch to track code changes, feature updates, and version incrementation without affecting the code in the main branch. This is useful for when you want to develop a feature on top of a working app without messing with the working and deployed feature. Typically when you want to make changes or add updates to a codebase, you will open a pull request on a new branch that tracks main.
    - `git branch -b` → show current branches
    - `git checkout -b <new_branch_name> origin/main` → create a new branch that tracks origin/main
    - Example: You will notice that the main branch and axelofwar-nft-inspect branch differ. The latter branch has a file added to the /utils folder called nft_inspect_tools.py that is not in main yet. You can also see that the latest addition to each branch shows a different message and update time, this is an example of version control! See if you can find the open pull request for this branch! Once it’s been reviewed it can be merged and we will see this additional file on the main branch as well!
      ![axelofwar/chatGPT-help-bot on branch ********main********](Learn%20Collaborative%20Development%20cbe607bf786d4edf8abcbba4cc3da2e3/Screenshot_2023-02-25_at_7.34.35_PM.png)
      axelofwar/chatGPT-help-bot on branch **\*\*\*\***main**\*\*\*\***
      ![axelofwar/chatGPT-help-bot on branch **************************axelofwar-nft-inspect**************************](Learn%20Collaborative%20Development%20cbe607bf786d4edf8abcbba4cc3da2e3/Screenshot_2023-02-25_at_7.34.59_PM.png)
      axelofwar/chatGPT-help-bot on branch \***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***axelofwar-nft-inspect\***\*\*\*\*\*\*\***\*\*\***\*\*\*\*\*\*\***
  - Add - identify the files that you want to track changes in. These are the files that will be included in your later commit, push, and merge to the main branch
    - `git add <file_name`>
  - Commit - the changes in your local branch that you would like staged to add to the matching branch on the server
    - `git commit -m "changes made to x file"`
  - Push - how you get the changes from local branch to sever branch
    - `git push origin HEAD` → this will push to the HEAD of whatever branch you are on (HEAD = your last checkpoint)
  - Fetch - how you get the changes from server branch to local branch
    - `git fetch --prune` → this will pull latest server changes and prune(delete) any branches that no longer exist
  - Merge - add the changes from one branch to another - this use your local instance of the main branch as reference for what is changed - NOT THE VERSION ON THE SERVER - so make sure that you pull latest changes into your branch first to avoid merge conflicts
    - `git merge`
  - Rebase - better than merge imo, this will rewind any updates you’ve made and add in the updates from the main branch on the server before fast-forwarding your branch back to where you had it. This is great for preserving your changes while updating the rest of your code base so that when you want to merge your PR - there are no merge conflicts.
    - `git rebase`
    - `git rebase -i`→ interactive rebase to edit previous commits (this is useful for editing old commit messages or squashing multiple commits into one - when you want to request review I HIGHLY RECOMMENDED to squash first - seek help if needed)
    - `git rebase origin/main` → rebase main onto your branch in order to update it with main changes while preserving your code
    - `git rebase -i --root` → rebase **ALL** commits on a branch (use with caution!)
  - Pull Request - in order to get the code you’ve updated on your branch added (’merged’ in git terms) to the main branch - the best practice is to open a pull request on that branch. This pull request is a formalized request to the main branch owner for you to add whatever code changes you are proposing to their main codebase. **ALL** changes you would like added to the main branch should be created in a separate branch and pull requested to the main (unless you own the repository)

    - Example: Here you can see a pull request that has been assigned to me (axelofwar) - when it’s ready for review and approval to merge to main - I will add a reviewer by clicking the gear next to the “No Reviews” section. You can see that the pull request has been assigned to the project I’ve created for this learning tutorial so that you all can check it out! Below that you can also see there is an issue linked. For each branch where you are doing development, it is typically tied to a story or issue (same concept) that has been identified for either a feature addition or enhancement. You can link that issue in the development section so that other reviewers can quickly see all related branches/issues.

    ![Screenshot 2023-02-25 at 6.01.48 PM.png](Learn%20Collaborative%20Development%20cbe607bf786d4edf8abcbba4cc3da2e3/Screenshot_2023-02-25_at_6.01.48_PM.png)

  - Issues - an issue in git is a story or task as known in Agile/Scrum. Use issues to identify work that you are going to take on, or assign open issues to yourself in order to identify to the rest of the team which tasks or stories you are taking responsibility for.
    - Example: Here you can see an issue that has been created in order to track the branch in development and associated pull request reference above. Typically we only need to track either the issue, or the pull request in the project. **In this case you can remove the project link from the branch above and instead link the branch to the issue in ‘development’ as shown below. This will store the branch on the issue - and the issue in the project**
      ![Screenshot 2023-02-25 at 7.48.50 PM.png](Learn%20Collaborative%20Development%20cbe607bf786d4edf8abcbba4cc3da2e3/Screenshot_2023-02-25_at_7.48.50_PM.png)

GitHub also offers many other features such as wikis, page deployments, branch protections, and much more! You should look into these if you want to become a 10x open source contributor! Much of the open source community simply scroll GitHub for issues on projects related to things they enjoy and look for ways to contribute! This is a great way to enhance your skills, network, and potentially even become an official contributor on profitable ventures!

### Note on Project Management:

There are numerous tools for project management - some of the most popular being Jira, Asana, and ClickUp. Github has its own integrated project management that we’ve looked at some today in the projects section - but feel free to explore others! I personally know a number of companies (including my web2 job) that use Jira and it has some great features (albeit a little clunky to learn).

## Integrated Development Environments (IDEs)

Integrated Development Environments (IDEs) are software applications that provide a comprehensive environment for developers to write code, test, and debug. Put simply - this is where devs write our code instead of an arbitrary text editor + terminal. Here are three of the most popular IDEs:

1. **Visual** **Studio** **Code**: Developed by Microsoft, Visual Studio Code (VS Code) is a free and open-source IDE that supports a wide range of programming languages. It offers features like IntelliSense (code completion), debugging, Git integration, and extensions that provide additional functionality.
2. Eclipse: Eclipse is another popular IDE that supports multiple programming languages. It offers features like code completion, refactoring, debugging, and Git integration. Eclipse also has a plugin architecture that allows for additional functionality.
3. IntelliJ IDEA: Developed by JetBrains, IntelliJ IDEA is an IDE specifically designed for Java development. It offers features like code completion, debugging, and Git integration. IntelliJ IDEA also has a plugin architecture that allows for additional functionality.

The go to IDE for most is VS Code, and most opt for this unless they are experienced and have specific requirements. If you’re looking for a python specific IDE to help you get started learning, there are several IDEs that are popular among Python developers:

- PyCharm: Created by JetBrains, PyCharm is a popular IDE for Python development that offers code completion, debugging, and Git integration. It also has a variety of plugins available for additional functionality.
- Spyder: Spyder is an open-source IDE specifically designed for scientific Python development. It offers features like code completion, debugging, and variable explorer.
- **Jupyter Notebook**: Jupyter Notebook is a web-based interactive development environment that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. It is often used for data analysis and visualization in Python. (**\*\***\*\*\*\***\*\***VERY BEGINNER FRIENDLY**\*\***\*\*\*\***\*\***)

Ultimately, the best IDE for Python development depends on your personal preferences and the specific requirements of your project, but I would recommend VS Code for most, and Jupyter Notebook for the most user friendly and python focused option.
