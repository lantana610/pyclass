
# Question 1: Create a reusable function to clean feedback.
def clean_feedback(text):
    text = text.strip().lower()
    # Replace "speaker" with "presenter".
    text = text.replace("speaker", "presenter")
    text = " ".join(text.split())
    return text.title()
# Question 3: Read feedback safely using exception handling.
def display_feedback():
    try:
        # Open feedback.txt for reading.
        with open("feedback.txt", "r", encoding="utf-8") as file:
            # Print each feedback entry on a separate line.
            for line in file:
                print(line.rstrip("\n"))
    except FileNotFoundError:
        # Display the required message if the file does not exist.
        print("File not found. Please create feedback.txt first.")

    except PermissionError:
        # Display the required message if access is denied.
        print("Permission denied. Close the file and try again.")

    finally:
        # Display this message whether reading succeeds or fails.
        print("Operation completed.")


# Main function: Run the feedback-processing steps.
def main():
    # Question 1: Clean and display the original feedback.
    raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

    cleaned_feedback = clean_feedback(raw_feedback)

    # Display the final cleaned feedback using an f-string.
    print(f"Cleaned feedback: {cleaned_feedback}")

    # Question 2: Create a list containing three cleaned messages.
    feedback_list = [
        cleaned_feedback,
        clean_feedback(
            "  the workshop was GREAT and very helpful  "
        ),
        clean_feedback(
            " the examples were clear but time was short "
        )
    ]

    try:
        # Write the three messages to feedback.txt.
        # Mode "w" creates the file or overwrites its existing contents.
        with open("feedback.txt", "w", encoding="utf-8") as file:
            for feedback in feedback_list:
                file.write(feedback + "\n")

        # Read and display the original three feedback messages.
        print("\nOriginal feedback:")
        display_feedback()

        # Clean one additional feedback message.
        new_feedback = clean_feedback(
            " great session with useful activities "
        )

        # Append the new message without overwriting existing entries.
        with open("feedback.txt", "a", encoding="utf-8") as file:
            file.write(new_feedback + "\n")

        # Read and display the full updated feedback list.
        print("\nUpdated feedback:")
        display_feedback()

    except PermissionError:

        print("Permission denied. Close the file and try again.")
        return

    except OSError as error:
        # Handle other operating-system errors while saving feedback.
        print(f"Unable to save feedback: {error}")
        return

    # Question 4: Analyze the feedback and create a summary report.
    try:
        # Read all feedback entries from the saved file.
        with open("feedback.txt", "r", encoding="utf-8") as file:
            feedback_lines = file.readlines()

        # Count the total number of feedback entries.
        total_feedback = len(feedback_lines)


        great_mentions = 0

        # Convert each entry to lowercase before checking for "great".
    
        for line in feedback_lines:
            if "great" in line.lower():
                great_mentions += 1

        # Build the required summary using f-strings.
        summary = (
            f"=== Workshop Feedback Summary ===\n"
            f"Total Feedback: {total_feedback}\n"
            f"Mentions of 'Great': {great_mentions}\n"
        )

        # Write the summary to a new file named summary.txt.
        with open("summary.txt", "w", encoding="utf-8") as file:
            file.write(summary)

        # Display the same summary neatly on the console.
        print(f"\n{summary}", end="")

    except FileNotFoundError:
        # Handle a missing feedback file.
        print("File not found. Please create feedback.txt first.")

    except PermissionError:
        # Handle permission errors when reading or writing.
        print("Permission denied. Close the file and try again.")

    except OSError as error:
        # Handle other operating-system errors during summary creation.
        print(f"Unable to create summary: {error}")


# Run the program when this file is executed directly.
if __name__ == "__main__":
    main()