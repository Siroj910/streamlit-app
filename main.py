import streamlit as lit
from database import get_schedules
from datetime import datetime, timedelta

# Page navigation
def main_page():
    lit.title("Lecture Reminder")

    tomorrow_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    lectures = get_schedules()

    lit.subheader(f"Upcoming Lectures for {tomorrow_date}:")
    if lectures:
        for time, theme in lectures:
            lit.write(f"📚 **{theme}** - 🕒 {time}")
    else:
        lit.write("No lectures scheduled for tomorrow.")

    # Download report option
    if lectures:
        report = "\n".join([f"{time} - {theme}" for time, theme in lectures])
        lit.download_button("Download Report", data=report, file_name="lecture_report.txt")

    # Navigation
    if lit.button("Go to Subscription Page"):
        lit.session_state["page"] = "Subscription"

def subscription_page():
    lit.title("Subscribe to Email Reminders")

    # Subscription form
    email = lit.text_input("Enter your email:")
    if lit.button("Subscribe"):
        if email:
            lit.success(f"Subscription successful for {email}!")
        else:
            lit.error("Please enter a valid email address.")

    if lit.button("Back to Lecture Reminder"):
        lit.session_state["page"] = "Lecture Reminder"

if "page" not in lit.session_state:
    lit.session_state["page"] = "Lecture Reminder"

if lit.session_state["page"] == "Lecture Reminder":
    main_page()

elif lit.session_state["page"] == "Subscription":
    subscription_page()
