# Spirit Stones - Phase 3 CLI Project

***

## Introduction

This is a CLI application that manages a spiritual center's collection of gemstones
and crystals, for use by spirtual health practitioners with the center's members.

***

## Installation

Use `pipenv install` to install the dependencies and create the environment to run
Spirit Stones.

## Functionality/User Stories

As a user I want to be able to:
- Add new gemstones or crystals to the collection.
- Remove gemstones or crystals from the collection.
- Update details about a particular gemstone or crystal in the collection.
- Search for a gemstone or crystal based on various attributes (name, color, spiritual 
  properties, etc.)
- Display information about a particular gemstone or crystal.
- View a list of all gemstones.
- Track which practitioner is using which gemstone or crystal, and with which member.
- Add, update and delete usage sessions.
- Add, update, and delete members.
- View a list of all members.
- Add, update, and delete practitioners.
- View a list of all practitioners.



## Tables for Database

#### 1. Gemstones Table: This table will store details about each gemstone or crystal in the collection.

- ID: A unique identifier for each gemstone or crystal.
- Name: The name of the gemstone or crystal.
- Color: The color of the gemstone or crystal.
- Properties: Spiritual properties associated with the gemstone or crystal.
- Availability: Whether the gemstone or crystal is currently available or in use.

#### 2. Practitioners Table: This table will store details about each practitioner.

- ID: A unique identifier for each practitioner.
- Name: The name of the practitioner.
- Specialization: The practitioner's area of specialization or expertise.

#### 3. Members Table: This table will store details about each member.

- ID: A unique identifier for each member.
- Name: The name of the member.

#### 4. Usage Table: This table will track the usage of each gemstone or crystal.

- ID: A unique identifier for each usage record.
- Gemstone ID: The ID of the gemstone or crystal being used.
- Practitioner ID: The ID of the practitioner using the gemstone or crystal.
- Member ID: The ID of the member with whom the gemstone or crystal is being used.
- Start Date: The date and time when the gemstone or crystal was taken for use.
- End Date: The date and time when the gemstone or crystal was returned.

## File Descriptions

#### `cli.py`

This Python script defines a command-line interface (CLI) for a the application. It uses the `click` library, a Python package that simplifies the creation of command line interfaces. The script starts by importing the click module.

It then imports commands from several modules: `gemstones`, `members`, `practitioners`, and `usages`. Each of these modules contains a set of commands related to their respective domains (managing gemstones, members, practitioners, and usages).

The `@click.group()` decorator is used to create a new `click.Group` instance that serves as the main command of the CLI. The function `cli()` is a placeholder for this group. The docstring inside this function, `"""Welcome to Spirit Stones, the Gemstone Management Application!"""`, is displayed as a welcome message when the CLI is launched.

The script then iterates over the commands imported from the different modules and adds them to the main `cli` command group. This is done using the `add_command` method of the `cli` group. After this step, `cli` is a group of commands that can be invoked from the command line.

Finally, the script includes the usual Python idiom for launching the main function of the script: `if __name__ == '__main__':`. When the script is run directly (i.e., not imported as a module), it invokes `cli()`, which launches the CLI.

The specific commands supported by this CLI and their functionalities aree defined in the `gemstones`, `members`, `practitioners`, and `usages` modules, which are described below.

## Author

Created by Wes Peters

***

## License

MIT License

Copyright (c) [2023] [Wesley Peters]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
