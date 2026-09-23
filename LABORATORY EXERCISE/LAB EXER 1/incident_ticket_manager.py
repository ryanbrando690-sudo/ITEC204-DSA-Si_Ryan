"""
ITEC 204 - Data Structures and Algorithms
Laboratory Activity 1: IT Automation Incident Ticket Manager

Data Structure Used: List (a linear data structure)
Each ticket is stored as a dictionary with keys: 'id', 'bot', 'description'
inside a Python list called `tickets`.

Operations implemented:
1. Add a new incident ticket
2. Display all active incident tickets
3. Search for a ticket by Incident ID
4. Remove a resolved ticket
5. Display the total number of active tickets
"""

# The list that holds all active incident tickets (our linear data structure)
tickets = []

# Sample data provided in the activity, used for quick testing
SAMPLE_TICKETS = [
    {"id": "INC1392939", "bot": "BOT-Inventory", "description": "Failed to generate the daily report"},
    {"id": "INC1392940", "bot": "BOT-Email", "description": "Failed to send the scheduled notification"},
    {"id": "INC1392941", "bot": "BOT-DataSync", "description": "Encountered an error during data transfer"},
    {"id": "INC1392942", "bot": "BOT-Invoice", "description": "Failed to process an invoice"},
    {"id": "INC1392943", "bot": "BOT-Report", "description": "Failed to generate the weekly report"},
    {"id": "INC1392944", "bot": "BOT-FileTransfer", "description": "Failed to upload the required file"},
    {"id": "INC1392945", "bot": "BOT-DataEntry", "description": "Encountered an error while entering records"},
    {"id": "INC1392946", "bot": "BOT-Backup", "description": "Failed to complete the scheduled backup"},
    {"id": "INC1392947", "bot": "BOT-Validation", "description": "Failed to validate the submitted records"},
    {"id": "INC1392948", "bot": "BOT-Notification", "description": "Failed to send the system alert"},
]


def add_ticket():
    """Adds a new incident ticket to the list."""
    print("\n--- Add New Incident Ticket ---")
    incident_id = input("Enter Incident ID: ").strip()

    # Prevent duplicate Incident IDs
    for ticket in tickets:
        if ticket["id"] == incident_id:
            print(f"Ticket {incident_id} already exists. Ticket not added.")
            return

    bot = input("Enter Bot name: ").strip()
    description = input("Enter Short Description: ").strip()

    new_ticket = {"id": incident_id, "bot": bot, "description": description}
    tickets.append(new_ticket)
    print(f"Ticket {incident_id} added successfully.")


def display_tickets():
    """Displays all active incident tickets."""
    print("\n--- Active Incident Tickets ---")
    if not tickets:
        print("No active incident tickets.")
        return

    print(f"{'Incident ID':<15}{'Bot':<20}{'Short Description'}")
    print("-" * 65)
    for ticket in tickets:
        print(f"{ticket['id']:<15}{ticket['bot']:<20}{ticket['description']}")


def search_ticket():
    """Searches for a specific ticket using its Incident ID."""
    print("\n--- Search Incident Ticket ---")
    incident_id = input("Enter Incident ID to search: ").strip()

    for ticket in tickets:
        if ticket["id"] == incident_id:
            print("Ticket found:")
            print(f"  Incident ID : {ticket['id']}")
            print(f"  Bot         : {ticket['bot']}")
            print(f"  Description : {ticket['description']}")
            return

    print(f"No ticket found with Incident ID: {incident_id}")


def remove_ticket():
    """Removes a resolved incident ticket using its Incident ID."""
    print("\n--- Remove Resolved Ticket ---")
    incident_id = input("Enter Incident ID to remove: ").strip()

    for ticket in tickets:
        if ticket["id"] == incident_id:
            tickets.remove(ticket)
            print(f"Ticket {incident_id} removed successfully.")
            return

    print(f"No ticket found with Incident ID: {incident_id}")


def count_tickets():
    """Displays the total number of active incident tickets."""
    print("\n--- Total Active Tickets ---")
    print(f"Total active incident tickets: {len(tickets)}")


def load_sample_data():
    """Loads the 10 sample tickets provided in the activity, for quick testing."""
    print("\n--- Loading Sample Data ---")
    loaded = 0
    for sample in SAMPLE_TICKETS:
        # Avoid duplicates if sample data is loaded more than once
        if not any(t["id"] == sample["id"] for t in tickets):
            tickets.append(sample.copy())
            loaded += 1
    print(f"{loaded} sample ticket(s) loaded.")


def print_menu():
    print("\n===== IT AUTOMATION INCIDENT TICKET MANAGER =====")
    print("1. Add a new incident ticket")
    print("2. Display all active incident tickets")
    print("3. Search for an incident ticket")
    print("4. Remove a resolved incident ticket")
    print("5. Display total number of active tickets")
    print("6. Load sample data (10 test tickets)")
    print("7. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_ticket()
        elif choice == "2":
            display_tickets()
        elif choice == "3":
            search_ticket()
        elif choice == "4":
            remove_ticket()
        elif choice == "5":
            count_tickets()
        elif choice == "6":
            load_sample_data()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
