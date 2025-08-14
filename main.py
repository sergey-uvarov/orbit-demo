import sentry_sdk

# Sentry configuration (using a placeholder DSN for demo purposes)
# In production, replace with your actual Sentry DSN
try:
    sentry_sdk.init(
        dsn="https://12345@o67890.ingest.sentry.io/12345",  # Valid DSN format
        send_default_pii=True,
    )
except Exception as e:
    print(f"Sentry initialization failed: {e}")
    print("Continuing without Sentry...")

print("Starting application...")

# Perform safe division operation
numerator = 1
denominator = 2  # Changed from 0 to 2 to avoid division by zero

result = numerator / denominator
print(f"Division result: {numerator}/{denominator} = {result}")

print("Application running successfully")
