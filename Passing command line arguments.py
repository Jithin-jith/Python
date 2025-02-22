import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple Python script to demonstrate command-line arguments.")
    
    # Adding arguments
    parser.add_argument("name", type=str, help="Your name") #Mandatory argument
    parser.add_argument("age", type=int, help="Your age")  #Mandatory argument
    parser.add_argument("--city", type=str, default="Unknown", help="Your city (optional)") #Optional argument

    # Parsing arguments
    args = parser.parse_args()

    # Using the arguments
    print(f"Hello, {args.name}! You are {args.age} years old and live in {args.city}.")

if __name__ == "__main__":
    main()
