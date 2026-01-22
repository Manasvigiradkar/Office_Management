def add_employee(name, role):
    return f"Employee {name} added as {role}"

def remove_employee(name):
    return f"Employee {name} removed"

if __name__ == "__main__":
    print(add_employee("Amit", "Manager"))
    print(remove_employee("Riya"))
