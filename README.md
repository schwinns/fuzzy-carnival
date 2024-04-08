### Git and Github basics

This is a walk-through. We will run these commands together, but all this information and more can be found online. Here is some info [from our Wiki](https://github.com/shirtsgroup/shirts-group-wiki/wiki/Git-and-GitHub-Tutorials). Here are the [Github Docs](https://docs.github.com/en).

#### Set up a repo
Here, we will walk through how to set up a Github repository to track your code!

1. Navigate to your repository
2. Initialize version control with Git

`git init`

3. Add (or "stage") your files. Let's assume you have a bunch of files already in the current directory.

`git add .`

4. Commit these files. This is how Git knows what changes have been made.

`git commit -m "Added some code and figures"`

5. Go to Github.com and sign in to your account.
6. Go to **Repositories** at the top of your home page.
7. Click **New** in the top right corner. 
8. Give your repository a name, description, and visibility. You can also add a README, .gitignore, and a license at this time, but we will do these later.
9. Click **Create repository**. Now, you should see this new repository in your **Repositories** tab at the top.
10. To link your local repository (with all your files that we just committed) to the repository on Github, we need the link to the Github repository. Click **<> Code** and copy the HTTPS link.
11. Back in the terminal, link the local repository to the remote repository.

`git remote add origin REMOTE-URL`

12. Finally, push the local files to the remote repository.

`git push origin main`

#### Reset to a previous commit
Next, we will walk through what to do if something broke.

1. First, we need to make a change. 
2. Say we no longer want that change. Maybe it broke other code or we just don't need it anymore. There are a few ways to get back to a previous version, but I will just show one here. 
3. Locally, we can "reset" the commit. If it is the most recent commit, we can reset to `HEAD~1`. In this case, `HEAD` is the current (bad) commit and `~1` tells git to go back one commit. 

`git reset --hard HEAD~1`

We use `--hard` to not only reset the commit, but also undo the changes we made to the file. `HEAD~1` can be the SHA of any commit that you want to go back to. 

#### Add a `.gitignore`
Let's add a `.gitignore` file to not track certain files. This can be useful for _ignoring_ large files (e.g. `xtc`, `edr`, `log`).

1. First, we will create a `.gitignore` file manually.

`touch .gitignore`

2. Now, let's add the files we want to ignore with your favorite text editor.

`code .gitignore`

3. Finally, just stage, commit, and push the `.gitignore` file to Github.

`git add .gitignore`
`git commit -m "Created a .gitignore"`
`git push origin main`

#### Use and edit code from Github
Here, we discuss working with other people's code on Github. 

1. Say you find some code on Github that you want to use. We can _clone_ a copy to your local computer using the link from the **<> Code** button.

`git clone https://github.com/shirtsgroup/polymerist.git` 

2. Then, we make some changes that we want to track. Since this is not our repository, we do not want to push directly to the `main` branch.
3. One way we can track these changes is to create a separate `branch`. Let's first look at the branches that currently exist.

`git branch` 

4. And now create a new branch.

`git checkout -b new_branch`

5. Now, we can commit our changes to this new branch.

`git add .`
`git commit -m "Some fake changes."`

6. But, we want to be sure to push to our newly created branch.

`git push -u origin new_branch`

7. If you think your changes are needed in the `main` branch, you can create a _pull request_ on Github to propose to merge your changes into the `main` branch. I am not going to show that here, but there is plenty of good information out there. An example from [the Github Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

#### So, remember...
![git out](/figs/git_image.jpg)