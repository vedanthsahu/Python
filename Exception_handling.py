import os
import sys
import logging
import time
from functools import wraps


# 1. Fundamentals of Exceptions

# 1.1 What is an Exception?
# An exception is an event that disrupts the normal flow of a program. It can be handled to recover the program's execution.

# 1.2 Error vs Exception
# An error usually refers to a mistake in the code (like a syntax error), whereas exceptions occur during execution (runtime).

# 1.3 Exception Hierarchy (BaseException → Exception → Subclasses)
# Exception is derived from BaseException, and other exceptions like ValueError, TypeError, etc. inherit from Exception.

# 1.4 Built-in Exception Categories
# - Syntax Errors: Raised during parsing (e.g., missing colon or parentheses).
# - Runtime Errors: Raised when something goes wrong during execution (e.g., ValueError, ZeroDivisionError).
# - System-level Errors: Like MemoryError or KeyboardInterrupt.


# 2. try / except / else / finally — Control Flow Mastery

def demo_try_except():
    """Demonstrates try/except control flow and the first matching handler rule."""
    try:
        x = 1 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Caught a division by zero!")
    except Exception as e:
        print(f"Caught an exception: {e}")
    else:
        print("This won't run if an exception occurs.")
    finally:
        print("This block will always execute, no matter what.")

# 2.1 Execution Order
# First, try block is executed. If an exception is raised, it will match the first matching except block. 
# Finally, the finally block will always run.

# 2.2 Unreachable except Blocks (specific vs generic ordering)
# In the above example, the except blocks are ordered such that ZeroDivisionError is caught first, 
# and other exceptions won't be reached.

# 2.3 Finally Always Executes? (When It Doesn’t)
# - Infinite loops or OS-level terminations (e.g., kill -9).
# - Hard crashes will prevent the finally block from running.

def test_finally_execution():
    try:
        while True:  # Infinite loop to prevent the finally block from executing.
            pass
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt")
    finally:
        print("This won't execute due to infinite loop!")

# 3. Catching Exceptions Correctly

def divide_numbers(a, b):
    """Catches specific exceptions and logs them correctly."""
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error("Cannot divide by zero!")
        raise  # Re-raise the exception to propagate it
    except TypeError as e:
        logging.error("Invalid input type!")
    else:
        return result
    finally:
        print("End of operation.")

# 3.1 Single vs Multiple Except Blocks
# You can handle multiple exceptions either by using separate except blocks or grouping them into one.
# The above example shows how to handle both ZeroDivisionError and TypeError separately.

# 3.2 Grouping Multiple Exceptions
# except (TypeError, ValueError) would catch either TypeError or ValueError in the same block.

# 4. Custom Exceptions — Design & Best Practices

class InvalidOperationError(Exception):
    """Custom exception class to represent invalid operations."""
    def __init__(self, message="Invalid operation performed!"):
        self.message = message
        super().__init__(self.message)

def perform_operation(a, b, operation):
    """Raise a custom exception for invalid operations."""
    if operation not in ['add', 'subtract']:
        raise InvalidOperationError("Only 'add' or 'subtract' are allowed.")
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b

# 4.1 Creating Custom Exception Classes
# Custom exceptions are defined by inheriting from the built-in Exception class (not BaseException).

# 5. Raising Exceptions — Correct Usage

def validate_age(age):
    """Raises an exception if the provided age is invalid."""
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer.")
    return age

# 5.1 raise vs raise e
# raise e: It raises the exception with its traceback intact.
# raise ValueError("Custom error message"): Directly raises an exception.

# 5.2 Reraising Exceptions
def handle_user_input():
    try:
        age = validate_age("not an age")  # This will raise an exception
    except ValueError as e:
        print(f"Handling error: {e}")
        raise  # Reraise the exception

# 6. Exception Propagation & Stack Unwinding

def propagate_exception():
    try:
        1 / 0  # This will raise ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"Handled in the current function, but will propagate: {e}")
        raise  # Propagate the exception further up the stack

# 6.1 How Exceptions Bubble Up the Stack
# If an exception is not caught in the current function, it propagates up the call stack until it's caught.

# 7. Resource Safety & Context Management

class FileHandler:
    """A custom context manager to safely handle file operations."""
    def __enter__(self):
        self.file = open("example.txt", "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Exception occurred: {exc_type}, {exc_value}")
        self.file.close()

def write_to_file():
    with FileHandler() as file:
        file.write("Hello, World!")  # This will write to file safely

# 7.1 Why finally is not enough
# Using a context manager ensures that resources like files are always cleaned up properly, even if an exception occurs.

# 7.3 Context Managers
# The `__enter__` and `__exit__` methods define a context manager's behavior. 
# __enter__ handles the setup, and __exit__ handles the cleanup.

# 8. System-Level & OS Signals Interaction

import signal

def signal_handler(sig, frame):
    """Signal handler for graceful shutdown."""
    print(f"Received signal {sig}. Exiting gracefully.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# 8.1 Signal Handling
# The above example catches SIGINT (Ctrl+C) and exits gracefully.

# 9. Multi-Threading and Multi-Processing Exception Handling

import threading

def worker():
    try:
        1 / 0  # This will raise an exception in the thread
    except Exception as e:
        print(f"Exception in thread: {e}")

def start_threads():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# 10. Asynchronous Exception Handling

import asyncio

async def async_worker():
    await asyncio.sleep(1)
    raise ValueError("Async error occurred")

async def main():
    try:
        await async_worker()
    except ValueError as e:
        print(f"Caught async error: {e}")

# 11. Advanced Real-World Patterns

def retry_function():
    """Simulate a retry strategy with exponential backoff."""
    attempts = 3
    for attempt in range(attempts):
        try:
            # Simulate operation that could fail
            if attempt < 2:
                raise ValueError("Simulated failure")
            print("Operation successful")
            break
        except ValueError:
            print(f"Attempt {attempt + 1} failed. Retrying...")
            time.sleep(2 ** attempt)  # Exponential backoff

# 12. Exception Safety in Deployment Environments

def safe_shutdown():
    """Ensure graceful shutdown in a background worker process."""
    try:
        # Simulate worker process running
        raise KeyboardInterrupt  # Simulate signal to stop
    except KeyboardInterrupt:
        print("Graceful shutdown initiated.")

# 13. Rare / Expert-Level Topics

def complex_exception_handling():
    """Handling nested exceptions."""
    try:
        try:
            raise ValueError("Inner exception")
        except ValueError as e:
            print(f"Caught inner exception: {e}")
            raise KeyError("Outer exception")  # Raising outer exception
    except KeyError as e:
        print(f"Caught outer exception: {e}")

# 14. Anti-Patterns & Common Interview Traps

def anti_pattern_example():
    try:
        x = 1 / 0  # Divide by zero
    except:  # Don't ever do this!
        print("Swallowed all exceptions")

def main_execution():
    demo_try_except()
    test_finally_execution()
    divide_numbers(5, 0)
    validate_age(-5)
    handle_user_input()
    propagate_exception()
    write_to_file()
    start_threads()
    asyncio.run(main())
    retry_function()
    safe_shutdown()
    complex_exception_handling()
    anti_pattern_example()

if __name__ == "__main__":
    main_execution()
