# VakilDesk Assessment Test

## Project Structure

```
PROJECT/
│
├── src/
│   ├── task3_django_app/    # Django application for Task 3
│   ├── task1_web_scraper.py
│   ├── task2_csv_processor.py
│   ├── task4_rate_limiter.py
│   ├── task5_aggregate_data.py
│   ├── task6_duplicate.py
│   └── user_data.csv        # CSV file for data processing tasks
│
├── .gitignore
└── requirements.txt         # Project dependencies
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/crazycodeop/VakilDesk_assignment.git
   cd VakilDesk_assignment
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Tasks

### Task 1: Web Scraper
```
python src/task1_web_scraper.py
```

### Task 2: CSV Processor
```
python src/task2_csv_processor.py
```

### Task 3: Django App

1. Navigate to the Django app directory:
   ```
   cd src/task3_django_app
   ```

2. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Populate the database with sample data:
   ```
   python manage.py populate_db
   ```

4. Run the server:
   ```
   python manage.py runserver
   ```

5. Access the application:
   Visit http://localhost:8000/orders/top-customers/ to see the top 5 customers.

### Task 4: Rate Limiter
```
python src/task4_rate_limiter.py
```

### Task 5: Data Aggregator
```
python src/task5_aggregate_data.py
```

### Task 6: Duplicate Handler
```
python src/task6_duplicate.py
```

## Task Descriptions

### Task 1: Web Scraper
A Python script that scrapes news headlines from a specified news website.

### Task 2: CSV Processor
A script that processes the user_data.csv file, performing data manipulation and analysis.

### Task 3: Django App
A Django application that implements a specific functionality (details to be added).

### Task 4: Rate Limiter
A Python implementation of a rate limiting algorithm.

### Task 5: Data Aggregator
A script that aggregates and analyzes data from multiple sources.

### Task 6: Duplicate Handler
A script that identifies and handles duplicate data entries.

## Additional Notes

- Ensure you have Python 3.7+ installed on your system.
- The `user_data.csv` file in the `src/` directory is used for data processing tasks. Ensure it's present and correctly formatted before running related scripts.
- The `.vscode/` directory contains VS Code specific settings. You can ignore this if you're using a different IDE.
- If you encounter any issues with the Django app, make sure you've applied all necessary migrations and that the database is properly set up.
