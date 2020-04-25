# Steps for first time

In this file i'm going to write the steps to create a repository for first time.

1. Create a repository in github. In this repository github will be added the .git directory
and README.md file.

2. Open VSCode and clone the repository where you want.

3. Crate a virtual enviroment to add all of dependence for your project. How will you do? ----> [link](https://rukbottoland.com/blog/tutorial-de-python-virtualenv/)

Summary for this step:

```
$ virtualenv env --python=python3
$ source env/bin/activate
```
- To deactivate you will write: 

```
$ deactivate
```

- Install all dependence that you will need. Example:
```
$ pip install matplotlib
```

4. Create a .gitignore file to ignore the "env" directory because 
it's a waste of space to the repo add this directory. How will you do? ----> [link](https://swcarpentry.github.io/git-novice-es/06-ignore/)

```$ touch .gitignore```

Then add all names of files or directories that you want or need ignore writing the .gitignore file
Example ---> 
>env/ 

5. Create the requirement.txt file to write it with all names of dependence. How will you do? ----> [link](https://libzx.so/main/learning/2016/03/13/best-practice-for-virtualenv-and-git-repos.html)

To know the name of dependence you will install:.

```$ pip freeze```

To add the name of all dependence you will have.

```$ pip freeze > requirement.txt```

