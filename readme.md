# Project Template

## Setup
To clone repository: 

- open terminal
- create and navigate to "Projects" folder
	- mkdir projects (md projects)
	- cd projects
	- git clone {project_url}
- enter github username when prompted
- enter github password when prompted
- repository will now be cloned

## Installing requirements
- navigate the project
- set up a virtual environment (my_virtual_env)
- install packages
	- pip install -e .
- add kernel to jupter notebook
	- ipython kernel install --name "my_virtual_env" --user

## Working with notebooks
- in terminal enter
	- jupyter notebook
- this will open up a notebook and ask you which kernel you want to use
- select "my_virtual_env"


## Working with git
- To pull most recent changes to your machine:
	- git checkout branch_name
	- git pull

- When working on a new feature, first create a new branch
	- git status (check the branch you're on and if you're behind and commits)
	- git checkout branch_you_want_to_start_from (optional)
	- git pull (pull most recent updates)
	- git branch new_branch (create a new branch)
	- git checkout new_branch (move to new branch)

- To push changes:
	- git add .
	- git commit -m "A detailed message about what changes you are committing."
	- git push ('git push --set-upstream origin new_branch' on first commit)
	- git status (to see that all your changes have been commited)

- To merge branches: 
	- git checkout master
	- git merge develop
	- git push