import sentry_sdk

sentry_sdk.init(
    dsn="https://o4509841606115328.ingest.de.sentry.io/4509841611161680",
    send_default_pii=True,
)

print("Starting application...")
try:
    division_by_zero = 1 / 0
except ZeroDivisionError:
    print("Caught division by zero error - handling gracefully")
    sentry_sdk.capture_message("Division by zero attempted but handled", level="warning")
print("Application running successfully")
