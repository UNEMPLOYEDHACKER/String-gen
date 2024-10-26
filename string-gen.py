from pyrogram import Client
import os
import sys
import json
# Banner
banner = """
    dMMMMMP  .aMMMb   dMP     .aMMMb   .aMMMb   dMMMMb
   dMP      dMP"dMP  dMP     dMP"VMP  dMP"dMP  dMP dMP
  dMMMP    dMMMMMP  dMP     dMP      dMP dMP  dMP dMP
 dMP      dMP dMP  dMP     dMP.aMP  dMP.aMP  dMP dMP
dMP      dMP dMP  dMMMMMP  VMMMP"   VMMMP"  dMP dMP
|----------------------------------------------------|
|---------++++String Session Generator++++-----------|
|             °°°°°°°°°°°°°°°°°°°°°°°°               |
|Author :-Mr.Night                                   |
|Credit :-@Indian_Hacker_Group                       |
|____________________________________________________|
"""
def get_input(prompt, is_int=False):
    """Helper to get user input with validation."""
    while True:
        user_input = input(prompt)
        if is_int:
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input, please enter a number.")
        else:
            if user_input:
                return user_input
            else:
                print("Input cannot be empty. Please try again.")
def generate_string_session():
    print(banner)
    # Get API credentials (with validation)
    api_id = get_input("Enter your API ID: ", is_int=True)
    api_hash = get_input("Enter your API Hash: ")
    # Get the session file name
    session_name = get_input("Enter a custom session name please: ")
    # File path for the session
    session_file = f"{session_name}.session"
    # Check if session already exists
    if os.path.exists(session_file):
        print(f"A session file named '{session_name}.session' already exists.")
        overwrite = get_input("Do you want to overwrite it? (yes/no): ").lower()
        if overwrite not in ["yes", "y"]:
            print("Exiting without overwriting.")
            sys.exit(0)
    # Create a new Pyrogram client instance for session creation
    try:
        app = Client(session_name, api_id=api_id, api_hash=api_hash)
        print("Client created successfully. Starting the client...")
        # Start the Pyrogram client
        with app:
            # Generate the string session
            session_string = app.export_session_string()
            # Print the session string
            print("\nYour Telegram String Session:\n")
            print(session_string)
            print("\nKeep this string safe and secure.")
            # Save session string to a file if needed
            save_to_file = get_input("Do you want to save the session string to a file? (yes/no): ").lower()
            if save_to_file in ["yes", "y"]:
                file_path = f"{session_name}_session.txt"
                with open(file_path, "w") as f:
                    f.write(session_string)
                print(f"Session string saved to {file_path}.")
            else:
                print("Session string not saved to file.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
if __name__ == "__main__":
    generate_string_session()
