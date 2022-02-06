# 📌 Getting Started ⭐

Refer to the following articles on the basics of Git and Github and can also contact the Project Mentors, in case you are stuck:

- If you don't have git on your machine, [install](https://help.github.com/articles/set-up-git/) it.
- [Watch this video to get started, if you have no clue about open source](https://youtu.be/SL5KKdmvJ1U)
- [Forking a Repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
- [Cloning a Repo](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
- [How to create an Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issues/creating-an-issue)
- [How to create a Pull Request](https://opensource.com/article/19/7/create-pull-request-github)
- [Getting started with Git and GitHub](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)

# 📜 Instructions to follow while contributing to OBJECTIFY

Below are the steps to follow to contribute to this project:

**1.**  Fork [this](https://github.com/ShubhamKrSingh21/Objectify) repository.   

**2.**  Clone your forked copy of the project.
```
git clone --depth 1 https://github.com/<your_user_name>/backend.git
```
where `your_user_name` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

**3.** Navigate to the project directory :file_folder: .
```
cd backend
```

**4.** Now Open Your Favourite Text-Editor and run the command in terminal: .
```
npm install
```

**5.** Add a reference(remote) to the original repository.
```
git remote add upstream https://github.com/ShubhamKrSingh21/Objectify 
```
**6.** Check the remotes for this repository.
```
git remote -v
```
**7.** Always take a pull from the upstream repository to your main branch to keep it at par with the main project (updated repository).
```
git pull upstream main
```
**8.** Create a new branch.
```
git checkout -b <your_branch_name>
```

**9.** Make necessary changes and commit those changes
<p align="center"><img width=35% src="https://media2.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif?cid=ecf05e47pzi2rpig0vc8pjusra8hiai1b91zgiywvbubu9vu&rid=giphy.gif"></p>

**10.** Track your changes:heavy_check_mark: .
```
git add . 
```
**11.** Commit your changes .
```
git commit -m "Relevant message"
```
**12.** Push the committed changes in your feature branch to your remote repo.
```
git push -u origin <your_branch_name>
```

**13.** To create a pull request, click on `compare and pull requests`. Please ensure you compare your feature branch to the desired branch of the repo you are suppose to make a PR to.

<img src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" width=600>

**14.** Add appropriate title and description to your pull request explaining your changes and efforts done.

**15.** Click on `Create Pull Request`.

<img src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" width=600>

**16.** Congrats :exclamation: You have created a PR to the OBJECTIFY :boom: . Sit back patiently and relax till then the project maintainers will review your PR. Please understand,  there will be some time taken to review a PR and can vary from a few hours to a few days too so be Patient and keep contributing.
