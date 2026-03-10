def analyze_finances(income, expenses, savings, debt):

    savings_ratio = (income - expenses) / income if income else 0

    result = {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "debt": debt,
        "savings_ratio": savings_ratio
    }

    return result
