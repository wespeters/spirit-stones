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

The specific commands supported by this CLI and their functionalities are defined in the `gemstones`, `members`, `practitioners`, and `usages` modules, which are described below.

#### `gemstones.py`

This file defines a series of command-line interface (CLI) commands. It uses the `click` library for creating these commands and SQLAlchemy for interacting with a database.

Here's a breakdown of the functions:

`add_gemstone(name, color, properties)`: This function is used to add a new gemstone to the database. It takes three arguments: name, color, and properties of the gemstone. A new `Gemstone` object is created with these attributes and the `availability` set to `True`, and then added to the session. The session is committed to save the changes to the database, and a success message is printed.

`remove_gemstone(id)`: This function removes a gemstone from the database. It uses the `id` argument to identify the gemstone. If a gemstone with the provided ID is found, it is removed from the session and the session is committed. A success message is printed; if no gemstone with the given ID is found, an error message is printed.

`update_gemstone(id, name, color, properties)`: This function updates the details of a gemstone in the database. It finds a gemstone by `id` and updates its `name`, `color`, and `properties`. After the session is committed, a success message is printed. If no gemstone with the given ID is found, an error message is printed.

`view_gemstone(id)`: This function retrieves and displays the details of a gemstone with a given `id`. If a gemstone with the provided ID is found, its details are printed; if not, an error message is printed.

`search_gemstone(query)`: This function is used to search the collection of gemstones by `id`, `name`, `color`, or `properties`. All gemstones matching the search query are retrieved and their details are printed.

`list_gemstones()`: This function retrieves and displays the details of all gemstones in the database.

Finally, all these functions are added to a list named `commands`, which is imported by the CLI script to add these commands to the main CLI command group.

#### `members.py`

This file also defines a set of command-line interface (CLI) commands.

Here's a description of its functions:

`add_member(name)`: This function adds a new member to the database. It takes one argument, `name`, creates a new `Member`` object with this name, adds it to the session, and commits the session. It then echoes a success message with the ID of the new member.

`update_member(id, name)`: This function updates the name of an existing member in the database. It takes two arguments: `id` to identify the member and `name` for the updated name. If a member with the given ID is found, its name is updated, the session is committed, and a success message is echoed. If no member with the given ID is found, an error message is echoed.

`remove_member(id)`: This function removes a member from the database. It takes one argument, `id`, to identify the member. If a member with the given ID is found, it is deleted from the session, the session is committed, and a success message is echoed. If no member with the given ID is found, an error message is echoed.

`list_members()`: This function retrieves and displays a list of all members in the database. For each member, it echoes the member's ID and name.

Lastly, all these functions are added to a list named `commands`, which is imported by the CLI script to add these commands to the main CLI command group.

#### `practitioners.py`

This file also defines a set of command-line interface (CLI) commands.

These are its functions:

`add_practitioner(name, specialization)`: This function adds a new practitioner to the database. It takes two arguments, `name` and `specialization`, creates a new `Practitioner` object with these values, adds it to the session, and commits the session. It then echoes a success message with the ID of the new practitioner.

`update_practitioner(id, name, specialization)`: This function updates the name and specialization of an existing practitioner in the database. It takes three arguments: `id` to identify the practitioner, and `name` and `specialization` for the updated values. If a practitioner with the given ID is found, their name and specialization are updated, the session is committed, and a success message is echoed. If no practitioner with the given ID is found, an error message is echoed.

`remove_practitioner(id)`: This function removes a practitioner from the database. It takes one argument, `id`, to identify the practitioner. If a practitioner with the given ID is found, it is deleted from the session, the session is committed, and a success message is echoed. If no practitioner with the given ID is found, an error message is echoed.

`list_practitioners()`: This function retrieves and displays a list of all practitioners in the database. For each practitioner, it echoes the practitioner's ID, name, and specialization.

Then, all these functions are added to a list named `commands`, which is imported by the CLI script to add these commands to the main CLI command group.

#### `usages.py`

This file also defines a set of command-line interface (CLI) commands. A usage record represents a particular instance of a gemstone being used by a member under the guidance of a practitioner.

Here are its functions:

`add_usage(gemstone_id, practitioner_id, member_id)`: This function adds a new usage record to the database. It takes three arguments, `gemstone_id`, `practitioner_id`, and `member_id`, creates a new `Usage` object with these values and the current date as the `start_date`, adds it to the session, and commits the session. It also updates the availability of the gemstone. It then echoes a success message with the ID of the new usage.

`update_usage(id, gemstone_id, practitioner_id, member_id, end_date)`: This function updates an existing usage record in the database. It takes five arguments: `id` to identify the usage, `gemstone_id`, `practitioner_id`, and `member_id` for the updated values, and `end_date` for the updated end date. If a usage record with the given ID is found, its values are updated, the session is committed, and a success message is echoed. It also updates the availability of the gemstone. If no usage record with the given ID is found, an error message is echoed.

`remove_usage(id)`: This function removes a usage record from the database. It takes one argument, `id`, to identify the usage. If a usage record with the given ID is found, it is deleted from the session, the session is committed, and a success message is echoed. If no usage record with the given ID is found, an error message is echoed.

`list_usages()`: This function retrieves and displays a list of all usage records in the database. For each usage, it echoes the usage's ID, gemstone ID, practitioner ID, member ID, start date, and end date.

Finally, as in the modules above, these functions are added to a list named `commands`, which is imported by the CLI script to add these commands to the main CLI command group.

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
