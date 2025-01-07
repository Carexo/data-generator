# Data Generator

## Overview
This project is designed to generate various data related to studies, syllabuses, internships, webinars, meetings, and courses. It includes functionalities to generate random data for these entities and manage their relationships.

## Features
- Generate random studies with names, descriptions, limit places, and start years.
- Generate syllabuses for studies with random subjects and semesters.
- Generate internships with random start and end dates.
- Generate webinar participants with random available due dates and times.
- Generate meeting schedules and orders, ensuring no duplicate meeting-participant pairs.
- Generate course participants and orders, ensuring no duplicate course-participant pairs.

## Project Structure
- `config/`: Configuration files for products and users.
- `orders/`: Code for generating orders related to courses and meetings.
- `products/`: Code for generating studies, syllabuses, and internships.
- `users/`: Code for generating participants related to webinars and courses.
- `utils/`: Utility functions for generating random data.

## Installation
1. Clone the repository:
    ```sh
    git clone git@github.com:Carexo/data-generator.git
    ```

## Usage
### Generating Data
To generate data, run the following script:
```sh
make generate-all
```