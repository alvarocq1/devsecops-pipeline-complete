# Phase 1: Local CI/CD with GitHub Actions

In this first phase we are going to learn the basic use of github actions, doing deploiying Sec Operations for our python app.

First thing is create the yml, this file format is known by github to describe the CI/CD, in this file we wirte the steps and actions we want github actions to execute.

We are going to use some sec tools to perform a SAST analysis (Static Analisys) for the source code of the app, and  secrets analysis to performa a search on the repository for secret leaks.  We will be using `gitleaks` and `bandit` as well. For this we are using a Ubuntu machine of Github to execute it. First we need to set up python and install its dependencies, this can be necessary depending on the type of app we are deploying.

