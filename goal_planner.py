def goal_planner(goal, amount, years):

    monthly_savings = amount / (years * 12)

    return {
        "goal": goal,
        "target_amount": amount,
        "years": years,
        "monthly_savings_required": monthly_savings
    }
