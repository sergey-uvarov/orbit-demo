import sentry_sdk

sentry_sdk.init(
    dsn="https://o4509841606115328.ingest.de.sentry.io/4509841611161680",
    send_default_pii=True,
)

print("Starting application...")

# Perform safe division operation
numerator = 1
denominator = 2  # Changed from 0 to 2 to avoid division by zero

result = numerator / denominator
print(f"Division result: {numerator}/{denominator} = {result}")

print("Application running successfully")
