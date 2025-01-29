# eevveerryyddaayy-dev

A Github template repository for documenting technical skill-building challenges

## Description

> [!NOTE]
> ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.
<!-- markdownlint-disable MD028 -->

<!-- markdownlint-enable MD028 -->
> [!NOTE]
> This is the documentation for the [`eevveerryyddaayy-template`](https://github.com/ggeerraarrdd/) repository.

`eevveerryyddaayy` is a Github template repository intended for those who want to simplify the process of documenting their self-learning journey. Whether you are a student fresh out of college or an experienced developer in the workforce, this platform helps track your daily practice, skill-building challenges or technical interview preparation progress in one organized space.

Think of it as a portfolio-builder. `eevveerryyddaayy` automates the process of file creation, organizing and storing, as well as indexing your record of personal achievements and development over time. This streamlining allows you to spend more time on what matters most - the actual learning.

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

* 📝 Automated File Management - Creates and organizes daily practice files
* 🗂️ Automated Indexing - Creates and maintains a table of contents of your files for quick reference and access
* 📊 Daily Progress Tracking - Visualizes your learning journey in tabular form
* 📚 Solution Repository - Showcases different approaches to programming challenges
* 📖 Educational Notes - Documents key programming concepts and techniques
* ⚡ Jupyter Notebook Interface - Simplifies data entry through a form-like template

## Project Structure

```text
eevveerryyddaayy-template/
│
├── src/
│   ├── __init__.py
│   │
│   ├── main/
│   │   ├── __init__.py
│   │   │
│   │   ├── config/
│   │   │   └── __init__.py
│   │   │
│   │   ├── helpers/
│   │   │   └── __init__.py
│   │   │
│   │   ├── templates/
│   │   │
│   │   ├── main.py
│   │   └── notebook.py
│   │
│   └── tests/
│       └── __init__.py
│
├── solutions/
│
├── eevveerryyddaayy.ipynb
│
├── docs/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Prerequisites

* Python 3.12 (not tested on other versions)
* Familiarity with Jupyter Notebooks

## Getting Started

### Dependencies

* See `requirements.txt`

### Installation

1. **Follow Github's documentation on [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)**

    * The template repository is located at [`eevveerryyddaayy-template`](/README.md).

2. **Clone the repository**

    ```bash
    git clone https://github.com/ggeerraarrdd/eevveerryyddaayy.git
    ```

3. **Navigate into the project directory**

    ```bash
    cd eevveerryyddaayy-template # For example
    ```

4. **Create and activate a virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

5. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Default Index table settings**

    * The table contains 5 default columns. **You can add a 6th column.**
    * The name of an activated sixth column is "NB". **You can choose a different name.**
    * The first column uses sequential numbering (e.g. "001", "002"). **You can switch to date format.**

    If you don't want to change these default settings, skip to #3.
  
2. **Customize Index table settings**

    1. Open the `.env` file (with default settings) in the root directory

        ```python
        # Extra Column
        NB=0
        NB_NAME="NB"

        # Sequential Numbering
        SEQ_NOTATION=0
        ```

    2. Add your preferred settings

        * To add a 6th column: `NB=1`
        * To change its default name: `NB_NAME="Your Preferred Name"`
        * To switch to date format: `NB=1`

    **NOTE:** These settings cannot be changed after the project has been initialized (see Usage #2).

3. **Personalize README**

    Feel free to make any changes to README, including the title and description of your project.

> [!IMPORTANT]  
> The markdown comments around the Index table must not be modified or deleted.

### Usage

1. Open `eevveerryyddaayy.ipynb` in the root directory.

2. Execute the cell containing the python code or `Run All` to display the form interface.

    **NOTE:** The project is initialized when this is done for the first time.

3. Fill in the fields and click the submit button.

    Congratualtions! 🎉 You're a day closer to achieving your goal! 🎯

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/eevvrryyddaayy-template/releases](https://github.com/ggeerraarrdd/eevveerryyddaayy-template/releases)

### Initial Release

* `eevveerryyddaayy` is the templetized version of [`SQL Everyday`](https://github.com/ggeerraarrdd/sql-everyday).

## Future Work

* Implement `SEQ_SPARSE`
* Enhance error handling
* Enhance configuration and input validations
* Add unit tests

## License

* [MIT License](https://github.com/ggeerraarrdd/sql-everyday/blob/main/LICENSE)

## Contributing

* TBD

## Acknowledgments

* TBD

## Screenshots

![eevveerryyddaayy](docs/screenshot1.png)

## Frontispiece

Buddy Holly and The Crickets performing "That'll Be The Day" [Still from broadcast]. The Ed Sullivan Show. CBS, December 1, 1957.
