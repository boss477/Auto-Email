MAIL_ENV_VARS = ("MAIL_USERNAME", "MAIL_PASSWORD", "MAIL_FROM")


def get_mail_settings(environ):
    """Return required mail configuration without providing credential defaults."""
    missing = [name for name in MAIL_ENV_VARS if not environ.get(name) or not environ[name].strip()]
    if missing:
        names = ", ".join(missing)
        raise RuntimeError(f"Required mail environment variables are missing: {names}")
    return {name: environ[name] for name in MAIL_ENV_VARS}
