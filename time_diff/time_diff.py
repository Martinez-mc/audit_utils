from datetime import datetime

def time_difference(start_time_str, end_time_str):
    # Define the time format
    time_format = "%I:%M %p"  # 12-hour format with AM/PM

    # Parse the input times
    start_time = datetime.strptime(start_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)

    # Calculate the difference
    time_diff = end_time - start_time

    # Convert the difference to decimal hours
    decimal_hours = time_diff.total_seconds() / 3600  # 3600 seconds in an hour

    return decimal_hours

# Example usage
start_time = "8:00 AM"
end_time = "4:30 PM"
difference = time_difference(start_time, end_time)
print(f"Hours: {difference:.2f}\nBreak Adjusted: {difference-1:.2f}")
