# Measure App: You vs the Stars

A [Streamlit](https://docs.streamlit.io/?utm_source=chatgpt.com) app that lets you enter your height (in centimetres) and compares it to a list of celebrity heights from a [CSV file](https://github.com/EDGENortheastern/celebrity-height-app/blob/main/celebs_height.csv). The app displays a bar chart and highlights your height for easy visual comparison.

## User Documentation

This app is currently under construction 🏗️

You can find [live app here](https://celebrity-height-app-4z9tos9maderykxcqq4cvy.streamlit.app/)

## Technical Documentation

Technical documentation explains how the project works behind the scenes. It focuses on the technologies used, the structure of the code, and the steps required to install, run, and maintain the app. This section is written for developers.

### Clone the repo

To start working with the existing app, you can clone it. 

Cloning is the process of creating a local copy of a GitHub repository on your own computer. It allows you to view, edit, and run the app locally just as it exists online, while keeping your own changes separate, on your computer.

Cloning from the terminal means using command-line instructions to download the entire GitHub repository onto your computer.

Use the copy button in the top-right corner of the code block below to copy the entire command, then paste it into your terminal to create a local copy of the project.

```bash
git clone https://github.com/EDGENortheastern/celebrity-height-app.git
```

The command below means `change directory` into the project folder. You use it in the terminal to move inside the folder you've just cloned.

```bash
cd celebrity-height-app
```

You can also open [Visual Studio Code](https://code.visualstudio.com/) manually and select `File/Open Folder' to find your cloned app.

### Create and activate a virtual environment

A virtual environment is like a little bubble for your project.

It keeps everything your app needs (like Streamlit, [Pandas](https://pandas.pydata.org/docs/), and [Plotly](https://plotly.com/python/) separate from everything else on your computer.

Without it, things can get messy: one project might need one version of a package, and another project might need a different one.

The virtual environment stops them from fighting each other.

Run this in your terminal to create it in your project folder:

```bash
python -m venv venv
```

Then activate it (wake it up) on a Mac:

```bash
source venv/bin/activate
```

on Windows:

```bash
venv\Scripts\Activate.ps1
```

You’ll know it’s working when you see (venv) at the start of your terminal line.

## Installing Dependencies

Once your virtual environment is active, you need to install the software libraries your app depends on.
This is done using pip, which stands for [Python Installer for Packages](https://pip.pypa.io/en/stable/cli/pip_install/?utm_source=chatgpt.com).

Think of pip as Python’s version of an app store: it downloads and installs the extra tools your program needs to run (like Streamlit, Pandas, and Plotly).

Run this command in your terminal:

```bash
pip install -r requirements.txt
```

The file [requirements.txt](https://github.com/EDGENortheastern/celebrity-height-app/blob/main/requirements.txt) lists all the packages your existing app needs to run.

You already have this file in your project, so you don’t need to create it again.

If you want to learn how to create or update a requirements.txt file for other projects, go to the Developer Manual for detailed instructions.

## Developer Manual

The Developer Manual is a step-by-step guide that explains how to rebuild or extend the app from scratch.

You need to create your own repository on GitHub, clone it to your computer, and then install the required dependencies.

```bash
pip install streamlit plotly pandas
```

The command `pip freeze` lists all the Python packages currently installed in your virtual environment, along with their exact versions.

This is useful because it lets you capture the state of your environment: the exact versions that make your app work.

You can save this list to a new file called `requirements.txt` by running:

```bash
pip freeze > requirements.txt
```
