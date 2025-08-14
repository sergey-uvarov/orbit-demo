import sentry_sdk

# Fixed DSN format for demo purposes
sentry_sdk.init(
    dsn="https://12345@o67890.ingest.sentry.io/12345",
    send_default_pii=True,
)

print("Starting application...")
# Fixed: Changed from division by zero to a valid division operation
result = 1 / 2
print(f"Division operation completed: 1 / 2 = {result}")
print("Application running successfully")
