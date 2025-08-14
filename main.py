import sentry_sdk

sentry_sdk.init(
    dsn="https://o4509841606115328.ingest.de.sentry.io/4509841611161680",
    send_default_pii=True,
)

print("Starting application...")
division_by_zero = 1 / 0
print("Application running successfully")
