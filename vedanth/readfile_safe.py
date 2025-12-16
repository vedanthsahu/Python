filename = input("Enter filename: ").strip()

try:
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()

except FileNotFoundError:
    print("File not found. Please check the filename.")

except PermissionError:
    print("Permission denied. You do not have access to this file.")

except UnicodeDecodeError:
    print("The file is not a valid UTF-8 text file.")

except Exception as e:
    print("Unexpected error:", type(e).__name__, e)

else:
    print("\nFile content:\n")
    print(data)
