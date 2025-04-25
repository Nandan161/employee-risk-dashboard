# __main__.py
from .employee import Employee
from .team import Team

def main():
    e = Employee()
    print("All employee names and IDs:")
    print(e.names())

    t = Team()
    print("\nAll team names and IDs:")
    print(t.names())

if __name__ == "__main__":
    main()