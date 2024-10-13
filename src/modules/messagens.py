class MessageTemplates:
    starting_monitoring = "🪙 Starting monitoring of quotation for {} ({}): $ {}\nTime of consult: {}"
    current_price = "🔍 The current quotation for {} ({}): $ {}."
    value_above = "⚠️ Important Notice!\nThe current value of {} ({}), exceeded the established limit.\n\n💰 Current Value: $ {:.2f}"
    value_below = "⚠️ Warning!\nThe current value of {} ({}), fell below the desired threshold.\n\n📉 Current Value: $ {:.2f}"
    threshold_reached = "✅ Notification!\nThe currency {} ({}) has reached the value you defined.\n\n🚀 Current Value: $ {:.2f}"
    reminder = "⏰ Reminder: Keep an eye on the quotation of cryptocurrency {} ({}).\nCurrent Value: $ {}."
