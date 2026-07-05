import random

# This function displays the interactive user menu.
# It is called in the main function to display the menu.

def show_menu():
    """Prints the interactive user menu."""
    print("\n" + "="*30)
    print("      SMART EXPENSE TRACKER   ")
    print("="*30)
    print("1. Set/View Monthly Budget")
    print("2. Add an Expense")
    print("3. View Expenses by Category")
    print("4. View Budget Report & Insights")
    print("5. Get Financial Tip of the Day")
    print("6. Exit")
    print("="*30)




# This function ensures the user inputs a valid positive float.

def get_valid_number(prompt):
    """Ensures the user inputs a valid positive float."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Please enter a positive amount.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number")




# This function adds a transaction to a specific category.

def add_expense(expenses_dict):
    """Adds a transaction to a specific category."""
    print("\n--- Add New Expense ---")
    category = input("Enter category (e.g., Food, Rent, Entertainment): ").strip().capitalize()
    amount = get_valid_number(f"Enter amount spent on {category}: ")
    
    # If the category doesn't exist yet, create a new list for it
    if category not in expenses_dict:
        expenses_dict[category] = []
        
    expenses_dict[category].append(amount)
    print(f"Successfully added {amount:.2f} to '{category}'!")







# This function displays the monthly budget report.
# It also provides insights based on the user's spending habits.
# It also provides insights based on the user's spending habits.

def view_report(budget, expenses_dict):
    print("\n--- Monthly Budget Report ---\n")

    total_spent = 0

    for category, amounts in expenses_dict.items():
        category_total = sum(amounts)
        total_spent += category_total
        print(f"{category}: {category_total:.2f}")
    
    print("-" * 30)
    print(f"Total Spent: {total_spent:.2f}")

    if budget > 0:
        remaining = budget - total_spent
        print(f"Remaining Budget: {remaining:.2f}")
        percentage = (total_spent / budget) * 100
        print(f"You have used {percentage:.1f}% of your budget.")

        if percentage > 80:
            print("⚠️  Alert: You are close to exceeding your budget!")
        elif percentage > 100:
            print("❌ Alert: You have exceeded your budget!")
        else:
            print("✅ Good job! You are within your budget.")
    else:
        print("No budget set yet.")


    if budget > 0:
        if total_spent > budget * 0.75:
            print("\n💡 AI Insight: You are spending quickly! Consider reviewing your 'Wants' categories.")
        else:
            print("\n💡 AI Insight: Great job! Your spending is balanced.")
    
    # Exception Handling for the case when budget is zero and total_spent is also zero
    try:
        percentage = (total_spent / budget) * 100
    except ZeroDivisionError:
        percentage = 0 
    
    
    
    
    
    

# Main Function starts here.
# It is the entry point of the program.

def main():
    user_budget = 0
    expenses = {
        'Food': [],
        'Rent': [],
        'Entertainment': [],
        'Transportation': [],
        'Shopping': [],
        'Other': [] 
    }
    tips = [
        "Track small purchases; they add up quickly!",
        "Try the 50/30/20 rule: 50% Needs, 30% Wants, 20% Savings.",
        "Cook at home this week to slash your food expenses.",
        "Before buying an item, wait 48 hours to see if you still want it." 
        "Setting an emergency fund is a great way to handle unexpected expenses without derailing your budget."
        "Review your bank statements regularly to stay on top of your spending habits."
        "Automating your savings can help you reach your financial goals faster."
    ]

    print("Welcome to your personal Python Expense Tracker!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            if user_budget == 0:
                user_budget = get_valid_number("Enter your monthly budget: ")
                print(f"Budget set to {user_budget:.2f}")
            else:
                print(f"Current budget: {user_budget:.2f}")
                change = input("Do you want to change it? (yes/no): ").strip().lower()
                if change == 'yes':
                    user_budget = get_valid_number("Enter new monthly budget: ")
                    print(f"Budget updated to {user_budget:.2f}")
                else:
                    print("Keeping the old budget")
        
        elif choice == '2':
            add_expense(expenses)

        elif choice == '3':
            print("\n--- Expenses by Category ---")
            total_spent = 0
            for category, amounts in expenses.items():
                category_total = sum(amounts)
                total_spent += category_total
                print(f"{category}: {category_total:.2f}")
            print(f"\nTotal Spent Across All Categories: {total_spent:.2f}")

        elif choice == '4':
            view_report(user_budget, expenses)
            
        elif choice == '5':
            print("\n--- Financial Tip of the Day ---")
            if not tips:
                print("No tips available.")
            else:
                print(random.choice(tips))
            
        elif choice == '6':
            print("\nThank you for using the Smart Expense Tracker.\nStay financially smart!")
            break
        else:
            print("Invalid choice! Please try again. Please select a number between 1 and 6.")
            

        
            
                
    
# Run the main function to start the program    
if __name__ == "__main__":
    main()


    