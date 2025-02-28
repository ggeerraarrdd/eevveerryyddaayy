# eevveerryyddaayy

A Github template repository for documenting technical skill-building challenges

## Description

> [!NOTE]
> ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.
<!-- markdownlint-disable MD028 -->

<!-- markdownlint-enable MD028 -->
> [!NOTE]
> This is the documentation for the Github template repository [`eevveerryyddaayy-template`](https://github.com/ggeerraarrdd/eevveerryyddaayy-template/), which is the templatized version of [`SQL Everyday`](https://github.com/ggeerraarrdd/sql-everyday).

`eevveerryyddaayy-template`, or simply `eevveerryyddaayy`, is a Github template repository that helps you document your self-learning journey. It automates the process of file creation, organizing and storing, as well as indexing your record of personal achievements and development over time. This streamlining allows you to spend more time on what matters most—the actual learning.

Whether you are a student fresh out of college or an experienced developer, this portfolio-building platform simplifies how you track your daily practice, skill-building challenges or technical interview preparation. It keeps all your progress organized in one place.

![The Crickets](docs/the_crickets.png)
_(Everyday, it's a gettin' closer / Goin' faster than a roller coaster / Push like yours will surely come my way, a-hey, a-hey-hey / Push like yours will surely come my way)_

## Table of Contents

* [Description](#description)
* [Features](#features)
* [Project Structure](#project-structure)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
  * [Dependencies](#dependencies)
  * [Installation](#installation)
  * [Configuration](#configuration)
* [Usage](#usage)
* [System Administration](#system-administration)
  * [Configuration Updates](#configuration-updates)
* [Author(s)](#authors)
* [Version History](#version-history)
  * [Release Notes](#release-notes)
  * [Initial Release](#initial-release)
* [Future Work](#future-work)
* [License](#license)
* [Contributing](#contributing)
* [Acknowledgments](#acknowledgments)
* [Screenshots](#screenshots)

## Features

* 🌐 Portfolio Builder - Transforms a Github repository into a coding portfolio website with README.md serving as the homepage
* 📝 Automated File Management - Creates and organizes daily practice files
* 🗂️ Automated Indexing - Creates and maintains a table of contents of your files for quick reference and access
* ✨ Dynamic Markdown Tables - Intelligently adjust column widths to accommodate new content, maintaining alignment and readability
* 📊 Daily Progress Tracking - Visualizes your learning journey in tabular form
* 📚 Solution Repository - Showcases different approaches to programming challenges
* ⚡ Jupyter Notebook Interface - Simplifies data entry through a form-like template

## Project Structure

```text
eevveerryyddaayy-template/
│
├── src/
│   ├── __init__.py
│   │
│   ├── config/
│   │   └── __init__.py
│   │
│   ├── forms/
│   │   └── __init__.py
│   │
│   ├── handlers/
│   │   └── __init__.py
│   │
│   ├── templates/
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   └── __init__.py
│   │
│   └── app.py
│   
├── solutions/
│
├── every_entry.ipynb
├── every_start.ipynb
├── every_update.ipynb
│
├── .vscode
├── docs/
├── .gitignore
├── .pylintrc
├── LICENSE
├── README.md
└── requirements.txt
```

## Prerequisites

* **Python 3.12**
  * Not tested on other versions
* **VS Code** as your development environment
* Familiarity with **Jupyter Notebooks**
* **Jupyter extension** for VS Code
  * Required for running notebook files
  * **IMPORTANT**: Install specifically version `v2024.11.0` - not tested on any other version
  * From VS Code marketplace: Extensions icon → ⚙️ icon next to Jupyter → Install Another Version → Select v2024.11.0

## Getting Started

### Dependencies

* See `requirements.txt`

### Installation

1. **Follow Github's documentation on [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)**

    👉 The template repository is located [here](https://github.com/ggeerraarrdd/eevveerryyddaayy-template/).

2. **Clone the new repository**

    * Open a terminal window in VS Code.
    * Navigate to where you want the repository directory saved.

    ```bash
    git clone your-repository-url
    ```

3. **Setup a Python virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. **Rename VS Code settings file**

    * Navigate to the `.vscode` directory
    * Rename `settings.template.json` to `settings.json`

### Configuration

1. **Default settings**

    **Project Title:**
    * The default title is "[ ] Everyday". **You can choose a different title.**

    **Index Table:**
    * The default index table has 5 columns. **You can add a 6th column.**
    * The default name of an activated sixth column is "NB". **You can choose a different name.**
    * The first column uses sequential numbering as default (e.g. "001", "002"). **You can switch to date format.**

    **Form:**
    * The default Site list in the Form includes: [Codewars](https://www.codewars.com/), [DataLemur](https://datalemur.com/) and [LeetCode](https://leetcode.com/). **You can add or remove.**

    If you don't want to change these default settings, skip to #4.
  
2. **Customize Project settings**

    You can customize your settings during initialization by using the `every_start.ipynb` notebook.

    1. Open the `every_start.ipynb` notebook in the root directory.
    2. Modify the code cell containing configuration settings:

        ```python
        # Project: Title
        PROJ_TITLE='[ ] Everyday'
        
        # Index Table: Extra Column
        NB=0
        NB_NAME='NB'
        
        # Index Table: Sequential Numbering
        SEQ_NOTATION=0

        # Index Table: Sequential Gaps
        SEQ_SPARSE=0
        
        # Form: Site Options
        SITE_OPTIONS=['Codewars', 'DataLemur', 'LeetCode']
        ```

3. **Configuration options explained**

    **Project Title:**
    * Change `PROJ_TITLE` to your preferred project title.

    **Index Table:**
    * To add a 6th column: `NB=1`
    * To customize the 6th column name: `NB_NAME='Your Preferred Name'`
    * To switch to date format instead of sequential numbering: `SEQ_NOTATION=1`
    * To allow gaps in sequential numbering: `SEQ_SPARSE=1`

    **Form:**
    * Customize `SITE_OPTIONS` with your preferred sites as a list of strings.
    * If there is only one item in the list, that site becomes the only option and default value.

4. **Customize README**

    ⚠️ **IMPORTANT:** The Index table, including its enclosing markdown comments, can be placed elsewhere but must not be modified in any other way or deleted.

    Feel free to make any other changes to README, including the title and description of your project.

## Usage

1. Open the project folder on VS Code, if not already.

2. Open `every_entry.ipynb` in the root directory.

3. Execute the cell containing the python code or `Run All` to display the form interface.

4. Fill in the fields and click the submit button.

    🎉 Congratulations! You're a day closer to achieving your goal!

## System Administration

### **Configuration Updates**

⚠️ **Note:** Configuration updates after initialization will be supported in a future version.

If you need to modify your project settings after initialization:

* The upcoming feature will support configuration updates through `every_update.ipynb`.
* This will allow you to change project settings without starting from scratch.
* Currently, some settings like Index Table structure can only be set during initialization.

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/eevveerryyddaayy-template/releases](https://github.com/ggeerraarrdd/eevveerryyddaayy-template/releases)

### Initial Release

* `eevveerryyddaayy` is the templatized version of [`SQL Everyday`](https://github.com/ggeerraarrdd/sql-everyday).

## Future Work

* Filter for the `enhancement` label in [Issues](https://github.com/ggeerraarrdd/eevveerryyddaayy-template/issues).

## License

* [MIT License](https://github.com/ggeerraarrdd/eevveerryyddaayy/blob/main/LICENSE)

## Contributing

* This project is not accepting contributions at this time.

## Acknowledgments

* Coeus

## Screenshots

![eevveerryyddaayy](docs/screenshot1.png)

![eevveerryyddaayy](docs/screenshot2.png)

## Frontispiece

Buddy Holly and The Crickets performing "That'll Be The Day" [Still from broadcast]. The Ed Sullivan Show. CBS, December 1, 1957.
