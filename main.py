import datetime

parents_list = []
vaccine_schedule = {
    "Hepatitis B": "At Birth",
    "Polio": "2 months",
    "DTP": "2 months",
    "Hib": "2 months",
    "Rotavirus": "2 months",
    "MMR": "12-15 months"
}

appointment_records = []

class Parent:
    def __init__(self, parent_name, child_name):
        self.parent_name = parent_name
        self.child_name = child_name
        self.notification_list = []

    def display_vaccine_schedule(self):
        print(f"\nVaccination schedule for {self.child_name}:")
        for vaccine, age in vaccine_schedule.items():
            print(f"{vaccine}: {age}")

    def display_appointments(self):
        print(f"\nScheduled Appointments for {self.child_name}:")
        for appointment in appointment_records:
            if appointment.parent == self:
                print(f"Vaccine: {appointment.vaccine}, Date: {appointment.date}")

    def add_notification(self, vaccine_name, appointment_date):
        self.notification_list.append({"vaccine": vaccine_name, "date": appointment_date})

    def show_notifications(self):
        print(f"\nNotifications for {self.child_name}:")
        for notification in self.notification_list:
            print(f"Vaccine: {notification['vaccine']}, Date: {notification['date']}")


class Appointment:
    def __init__(self, parent, vaccine, date):
        self.parent = parent
        self.vaccine = vaccine
        self.date = date


def register_new_parent():
    parent_name = input("Enter your name: ")
    child_name = input("Enter your child's name: ")
    new_parent = Parent(parent_name, child_name)
    parents_list.append(new_parent)
    print(f"Successfully registered {parent_name}.")
    return new_parent


def schedule_vaccine(parent):
    print("\nAvailable Vaccines:")
    for vaccine in vaccine_schedule:
        print(vaccine)

    selected_vaccine = input("\nSelect a vaccine for the appointment: ")
    appointment_date = input("Enter the appointment date (YYYY-MM-DD): ")

    try:
        appointment_date = datetime.datetime.strptime(appointment_date, "%Y-%m-%d")
    except ValueError:
        print("Incorrect date format. Please try again.")
        return

    new_appointment = Appointment(parent, selected_vaccine, appointment_date)
    appointment_records.append(new_appointment)
    parent.add_notification(selected_vaccine, appointment_date)
    print(f"Appointment scheduled for {selected_vaccine} on {appointment_date.strftime('%Y-%m-%d')}.")
    

def main():
    print("Welcome to the Child Vaccination Management System V1")

    active_parent = None
    while True:
        print("\nMenu Options:")
        print("1. Register Parent")
        print("2. View Vaccination Schedule")
        print("3. Schedule Vaccination Appointment")
        print("4. View Scheduled Appointments")
        print("5. View Notifications")
        print("6. Exit")

        user_choice = input("Please select an option: ")

        if user_choice == '1':
            active_parent = register_new_parent()

        elif user_choice == '2':
            if active_parent:
                active_parent.display_vaccine_schedule()
            else:
                print("Please register first.")

        elif user_choice == '3':
            if active_parent:
                schedule_vaccine(active_parent)
            else:
                print("Please register first.")

        elif user_choice == '4':
            if active_parent:
                active_parent.display_appointments()
            else:
                print("Please register first.")

        elif user_choice == '5':
            if active_parent:
                active_parent.show_notifications()
            else:
                print("Please register first.")

        elif user_choice == '6':
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()