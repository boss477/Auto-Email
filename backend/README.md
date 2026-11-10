# Backend configuration

Install dependencies from `requirements.txt`, then copy `.env.example` to `.env` and fill in the mail account values locally. The application requires `MAIL_USERNAME`, `MAIL_PASSWORD`, and `MAIL_FROM`; it exits with a clear configuration error if any are missing. Keep `.env` out of version control. Set these values in the hosting provider's server-side environment settings for deployed instances.

If a mail app password was previously committed or published, revoke it in the account security settings and create a replacement there before restoring mail sending. Do not reuse the exposed value.
