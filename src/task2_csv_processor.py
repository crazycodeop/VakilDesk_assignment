import csv
import re

def clean_csv_data(input_file, output_file):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    unique_users = {}
    
    # reading csv file
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = row['user_id']
            email = row['email']
            
            # checking if email is valid
            if email_regex.match(email):
                # storing latest entry of a user, removing duplicates
                if user_id not in unique_users or row['timestamp'] > unique_users[user_id]['timestamp']:
                    unique_users[user_id] = row
    
    # writing cleaned data to new csv file
    with open(output_file, 'w', newline='') as file:
        if unique_users:
            fieldnames = unique_users[next(iter(unique_users))].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in unique_users.values():
                writer.writerow(row)

if __name__ == "__main__":
    input_csv = './src/user_data.csv'
    output_csv = './src/cleaned_user_data.csv'
    clean_csv_data(input_csv, output_csv)
    print(f"Cleaned data has been written to {output_csv}")