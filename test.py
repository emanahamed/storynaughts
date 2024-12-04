from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    name = input("What is your name? ")
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    age = calculate_age(dob)
    print(f"Hello {name}, I can see you are {age} years old.")

if __name__ == "__main__":
    main()