<!-- markdownlint-disable MD041 -->
[![GitHub release](https://img.shields.io/github/v/release/ggeerraarrdd/eevveerryyddaayy)](https://github.com/ggeerraarrdd/eevveerryyddaayy/releases)
[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/ggeerraarrdd/ggeerraarrdd/graphs/commit-activity)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1efb93fd6a00425a9753ac43e73067a6)](https://app.codacy.com/gh/ggeerraarrdd/eevveerryyddaayy/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![codecov](https://codecov.io/gh/ggeerraarrdd/eevveerryyddaayy/graph/badge.svg?token=6IYLEF6I2Q)](https://codecov.io/gh/ggeerraarrdd/eevveerryyddaayy)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ggeerraarrdd_eevveerryyddaayy&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ggeerraarrdd_eevveerryyddaayy)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
<!-- markdownlint-enable MD041 -->

# eevveerryyddaayy

A Github template repository for documenting technical skill-building challenges

## Table of Contents

> [!NOTE]
> ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

* [Description](#description)
* [Target Users](#target-users)
* [Features](#features)
* [Project Structure](#project-structure)
* [Quick Start](#quick-start)
* [Local Setup](#local-setup)
  * [Prerequisites](#prerequisites)
  * [Dependencies](#dependencies)
  * [Installation](#installation)
  * [Configuration](#configuration)
* [Usage](#usage)
* [Production Setup](#production-setup)
* [System Administration](#system-administration)
* [Author(s)](#authors)
* [Version History](#version-history)
  * [Release Notes](#release-notes)
  * [Initial Release](#initial-release)
* [Future Work](#future-work)
* [License](#license)
* [Contributing](#contributing)
* [Acknowledgments](#acknowledgments)
* [Screenshots](#screenshots)

## Description

_eevveerryyddaayy_ is a GitHub template repository. It is the templatized version of [_SQL Everyday_](https://github.com/ggeerraarrdd/sql-everyday), a personal skill-building challenge that necessitated an automated and streamlined framework to enable consistent daily practice and to manage an ever-growing coding portfolio.

_eevveerryyddaayy_ automates many of the tedious manual work associated with the documentation process, such as handling file creation and organizing project materials. This frees up more time on what matters most—the actual learning.

![The Crickets](assets/images/the_crickets.png)
_(Everyday, it's a gettin' closer / Goin' faster than a roller coaster / Skills like yours will surely come my way, a-hey, a-hey-hey / Skills like yours will surely come my way)_

## Target Users

_eevveerryyddaayy_ is intended for **self-directed learners**, such as:

* **Those** committing to consistent technical skill practice.
* **Those** seeking to track their progress for quick reference, knowledge retention and accountability.
* **Those** wanting their record of daily practice organized into an accessible portfolio.
* **Those** hoping to automate as much of the project management as possible.

## Features

* 🌐 **Portfolio Builder** - Transforms a Github repository into a coding portfolio website with README.md serving as the homepage
* 📝 **Automated File Management** - Creates and organizes daily practice files
* 🗂️ **Automated Indexing** - Creates and maintains a table of contents of your files for quick reference and access
* ✨ **Dynamic Markdown Tables** - Intelligently adjust column widths to accommodate new content, maintaining alignment and readability
* 📊 **Daily Progress Tracking** - Visualizes your learning journey in tabular form
* 📚 **Solution Repository** - Showcases different approaches to programming challenges
* ⚡ **Jupyter Notebook Interface** - Simplifies data entry through a form-like template

## Project Structure

```text
eevveerryyddaayy/
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
├── settings/
│   ├── start.ipynb
│   └── update.ipynb
│   
├── solutions/
│
├── tests/
│
├── EEVVEERRYYDDAAYY.ipynb
│
├── .github
├── .vscode
├── assets/
├── docs/
├── .gitignore
├── .pylintrc
├── LICENSE
├── README.md
└── requirements.txt
```

## Quick Start

1. **Create a repository from template**

   * Use GitHub's [template feature](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) with this repository.

2. **Clone and set up locally**

    ```bash
    # Clone the repository
    git clone https://github.com/ggeerraarrdd/eevveerryyddaayy.git

    # Set up environment and install dependencies
    cd eevveerryyddaayy
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    pip install -r requirements.txt
    ```

3. **Initialize project**

   * Open `settings/start.ipynb` in VS Code.
   * Run all cells to initialize with default settings.

4. **Start using**
   * Open `EEVVEERRYYDDAAYY.ipynb`.
   * Run the cells to display the form interface.
   * Fill in your first entry and click the submit button.

## Local Setup

### Prerequisites

* **Python 3.12**
  * Not tested on other versions
* **VS Code** as your development environment
* Familiarity with **Jupyter Notebooks**
* **Jupyter extension** for VS Code
  * Required for running notebook files
  * **IMPORTANT**: Install specifically version `v2024.11.0` - not tested on any other version
  * From VS Code marketplace: Extensions icon → ⚙️ icon next to Jupyter → Install Another Version → Select v2024.11.0

### Dependencies

* See `requirements.txt`

### Installation

1. **Follow Github's documentation on [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)**

2. **Clone the new repository**

    ```bash
    git clone your-repository-url
    ```

3. **Set up a Python virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

### Configuration

1. **Default settings**

    **Project Title:**
    * The default title is "[ ] Everyday". **You can choose a different title.**

    **Index Table:**
    * The default index table has 5 columns. **You can add a 6th column.**
    * The default name of an activated sixth column is "NB". **You can choose a different name.**
    * The first column uses sequential numbering as default (e.g. "001", "002"). **You can switch to date format.**
    * The rows show no gaps when a day is missed. **You can allow gaps to mark missed days for accountability.**

    **Form:**
    * The default Site list in the Form includes [Codewars](https://www.codewars.com/), [DataLemur](https://datalemur.com/) and [LeetCode](https://leetcode.com/). **You can add or remove.**
  
2. **Initialize project: Option 1: With Default Settings**

    1. Open the `start.ipynb` notebook in the `settings` directory.
    2. Run all code cells by clicking `Run All`.
    3. Skip to #4.

3. **Initialize project: Option 2: With Custom Settings**

    1. Open the `start.ipynb` notebook in the `settings` directory.
    2. Modify the code cell containing configuration settings (see #4 for details of options):

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

        **Configuration options explained**

        ```text
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
        ```

    3. Run all code cells by clicking `Run All`.

4. **Customize README.md**

    After the project has been initialized, `README.template.md` should be the new `README.md` in the root directory. A copy of the previous `README.md` with the project documentation is stored in `docs`.

    Feel free to make changes to the new `README.md`, including the title and description of your project.

    ⚠️ **IMPORTANT:** The Index table, including its enclosing markdown comments, can be placed elsewhere but must not be modified in any other way or deleted.

## Usage

1. Open the project folder on VS Code, if not already.

2. Open `EEVVEERRYYDDAAYY.ipynb` in the root directory.

3. Execute the cell containing the python code or `Run All` to display the form interface.

4. Fill in the fields and click the submit button.

5. **Update your portfolio.**

   **Using VS Code:**

   * Click on the Source Control icon in the sidebar (or press `Ctrl+Shift+G`)
   * Review changed files in the "Changes" section
   * Hover over "Changes" and click the `+` to stage all changes (or stage individual files)
   * Enter a commit message like "Add daily entry #[number]"
   * Click the checkmark to commit
   * Click on the "..." menu and select "Push"

   **Using Terminal:**

   ```bash
   git add .
   git commit -m "Add daily entry #[number]"
   git push origin main
   ```

6. 🎉 Congratulations! You're a day closer to achieving your goal!

## Production Setup

This application primarily runs in the user's local environment using VS Code and Jupyter notebooks. However, the GitHub repository serves as the "production environment" for the portfolio aspect of the project.

## System Administration

### **Configuration Updates**

⚠️ **Note:** Configuration updates after initialization will be supported in a future version.

If you need to modify your project settings after initialization:

* The upcoming feature will support configuration updates through `update.ipynb` in the `settings` directory.
* This will allow you to change project settings without starting from scratch.
* Currently, some settings like Index Table structure can only be set during initialization.

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/eevveerryyddaayy/releases](https://github.com/ggeerraarrdd/eevveerryyddaayy/releases)

### Initial Release

* _eevveerryyddaayy_ is the templatized version of [_SQL Everyday_](https://github.com/ggeerraarrdd/sql-everyday).

## Future Work

* Filter for the `enhancement` label in [Issues](https://github.com/ggeerraarrdd/eevveerryyddaayy/issues).

## License

* [MIT License](https://github.com/ggeerraarrdd/eevveerryyddaayy/blob/main/LICENSE)

## Contributing

* This project is not accepting contributions at this time.

## Acknowledgments

* Coeus

## Screenshots

![eevveerryyddaayy](assets/images/screenshot1.png)

![eevveerryyddaayy](assets/images/screenshot2.png)

## Frontispiece

Buddy Holly and The Crickets performing "That'll Be The Day" [Still from broadcast]. The Ed Sullivan Show. CBS, December 1, 1957.
