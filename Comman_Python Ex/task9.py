from datetime import datetime, timedelta
current_time = datetime.now()

# Adding 10 days
new_time = current_time + timedelta(days=10)
print(new_time)

# Subtracting 2 hours
new_time = current_time - timedelta(hours=2)
print(new_time)
