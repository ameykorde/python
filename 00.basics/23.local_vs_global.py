# local_global_variables.py

# Global variable
global_variable = "I am a global variable"


def example_function():
    # Local variable
    local_variable = "I am a local variable"

    print("Inside the function:")
    print(f"Global variable: {global_variable}")  # Can access global variable
    print(f"Local variable: {local_variable}")  # Can access local variable


def modify_global():
    global global_variable  # This allows us to modify the global variable inside the function
    global_variable = "I have been modified globally!"


def main():
    print("Before function call:")
    print(f"Global variable: {global_variable}")  # Accessing global variable
    try:
        print(f"Local variable: {local_variable}")  # This will raise an error since local_variable is not defined here
    except NameError as e:
        print(f"Error: {e}")  # Catch error if local variable is not accessible

    example_function()  # Calling the function to show local and global variable access

    # Modifying the global variable
    modify_global()

    print("\nAfter modifying global variable:")
    print(f"Global variable: {global_variable}")  # Modified global variable
    # The local variable is not accessible here, so it's not printed


if __name__ == "__main__":
    main()

'''
Before function call:
Global variable: I am a global variable
Error: name 'local_variable' is not defined

Inside the function:
Global variable: I am a global variable
Local variable: I am a local variable

After modifying global variable:
Global variable: I have been modified globally!

'''