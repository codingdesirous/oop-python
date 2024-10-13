def main():
    try:
  
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("The number is 42.\n")
            file.write("This is the third line of text.\n")
        print("File created and initial content written successfully.")

       
        with open("my_file.txt", 'r') as file:
            content = file.read()
        print("\nContents of 'my_file.txt' after writing:")
        print(content)

       
        with open("my_file.txt", 'a') as file:
            file.write("Appending line 4 to the file.\n")
            file.write("Line 5 with another number: 100.\n")
            file.write("This is the final appended line 6.\n")
        print("\nAdditional lines appended successfully.")

        
        with open("my_file.txt", 'r') as file:
            updated_content = file.read()
        print("\nContents of 'my_file.txt' after appending:")
        print(updated_content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have the required permissions to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile handling operation completed.")

if __name__ == "__main__":
    main()
