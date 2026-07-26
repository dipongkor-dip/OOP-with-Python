try:
    # Code that might throw an error
    result = 10 / 0
except ZeroDivisionError as error:
    # Runs ONLY if a ZeroDivisionError happens
    print(f"Caught an error: {error}")
except Exception as error:
    # Fallback for any other standard exception
    print(f"General error: {error}")
else:
    # Runs ONLY if NO exception was thrown
    print("Everything went smoothly!")
finally:
    # ALWAYS runs (cleanup work like closing files/db connections)
    print("Cleanup complete.")
