import unittest

from backend.config import get_mail_settings


class MailSettingsTests(unittest.TestCase):
    def test_missing_password_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, "MAIL_PASSWORD"):
            get_mail_settings({"MAIL_USERNAME": "mail@example.com", "MAIL_FROM": "mail@example.com"})

    def test_blank_password_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, "MAIL_PASSWORD"):
            get_mail_settings({
                "MAIL_USERNAME": "mail@example.com",
                "MAIL_PASSWORD": " ",
                "MAIL_FROM": "mail@example.com",
            })

    def test_returns_environment_values(self):
        values = {
            "MAIL_USERNAME": "mail@example.com",
            "MAIL_PASSWORD": "test-placeholder",
            "MAIL_FROM": "mail@example.com",
        }
        self.assertEqual(get_mail_settings(values), values)


if __name__ == "__main__":
    unittest.main()
