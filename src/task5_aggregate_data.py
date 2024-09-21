from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    result = {}
    for item in data:
        if key in item:
            group_key = item[key]
            if group_key not in result:
                result[group_key] = []
            result[group_key].append(item)
    
    return {k: aggregator(v) for k, v in result.items()}

if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30, "city": "New York", "occupation": "Engineer"},
        {"name": "Bob", "age": 25, "city": "Los Angeles", "occupation": "Designer"},
        {"name": "Charlie", "age": 35, "city": "New York", "occupation": "Teacher"},
        {"name": "David", "age": 28, "city": "Los Angeles", "occupation": "Developer"},
        {"name": "Eve", "age": 22, "city": "Chicago", "occupation": "Student"},
        {"name": "Frank", "age": 40, "city": "New York", "occupation": "Manager"},
        {"name": "Grace", "age": 32, "city": "Chicago", "occupation": "Doctor"},
        {"name": "Henry", "age": 45, "city": "Los Angeles", "occupation": "Lawyer"},
        {"name": "Ivy", "age": 27, "city": "New York", "occupation": "Artist"},
        {"name": "Jack", "age": 33, "city": "Chicago", "occupation": "Engineer"},
        {"name": "Kate", "age": 29, "city": "New York", "occupation": "Nurse"},
        {"name": "Leo", "age": 26, "city": "Los Angeles", "occupation": "Photographer"},
        {"name": "Mia", "age": 31, "city": "Chicago", "occupation": "Writer"},
        {"name": "Nora", "age": 24, "city": "New York", "occupation": "Chef"},
        {"name": "Oscar", "age": 38, "city": "Los Angeles", "occupation": "Architect"},
        {"name": "Paul", "age": 27, "city": "Chicago", "occupation": "Scientist"},
        {"name": "Quinn", "age": 22, "city": "New York", "occupation": "Intern"},
        {"name": "Rita", "age": 34, "city": "Los Angeles", "occupation": "Social Worker"},
        {"name": "Sam", "age": 36, "city": "Chicago", "occupation": "Accountant"},
        {"name": "Tina", "age": 30, "city": "New York", "occupation": "Analyst"},
    ]

    # count the number of people in each city
    result = aggregate_data(data, "city", len)
    print("Number of people in each city:", result)

    # calculate the average age in each city
    def average_age(items):
        return round(sum(item["age"] for item in items) / len(items), 2)
    
    result = aggregate_data(data, "city", average_age)
    print("Average age in each city:", result)

    # unique occupations in each city
    def unique_occupations(items):
        return list(set(item["occupation"] for item in items))
    
    result = aggregate_data(data, "city", unique_occupations)
    print("Unique occupations in each city:", result)

    # youngest person in each city
    def youngest_person(items):
        return min(items, key=lambda x: x["age"])["name"]
    
    result = aggregate_data(data, "city", youngest_person)
    print("Youngest person in each city:", result)