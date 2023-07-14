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
- Track which practitioner is using which gemstone or crystal, and with which member.


## Tables for Database

### 1. Gemstones Table: This table will store details about each gemstone or crystal in the collection.

- ID: A unique identifier for each gemstone or crystal.
- Name: The name of the gemstone or crystal.
- Color: The color of the gemstone or crystal.
- Properties: Spiritual properties associated with the gemstone or crystal.
- Availability: Whether the gemstone or crystal is currently available or in use.

### 2. Practitioners Table: This table will store details about each practitioner.

- ID: A unique identifier for each practitioner.
- Name: The name of the practitioner.
- Specialization: The practitioner's area of specialization or expertise.

### 3. Members Table: This table will store details about each member.

- ID: A unique identifier for each member.
- Name: The name of the member.

### 4. Usage Table: This table will track the usage of each gemstone or crystal.

- ID: A unique identifier for each usage record.
- Gemstone ID: The ID of the gemstone or crystal being used.
- Practitioner ID: The ID of the practitioner using the gemstone or crystal.
- Member ID: The ID of the member with whom the gemstone or crystal is being used.
- Start Date: The date and time when the gemstone or crystal was taken for use.
- End Date: The date and time when the gemstone or crystal was returned.

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
