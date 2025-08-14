import sentry_sdk

# Fixed DSN format for demo purposes
sentry_sdk.init(
    dsn="https://12345@o67890.ingest.sentry.io/12345",
    send_default_pii=True,
)

print("Starting application...")
division_by_zero = 1 / 0
print("Application running successfully")
