from enum import Enum

class TransactionalEmailType(Enum):
    """Enum for transactional email types."""
    WELCOME = "welcome"
    # trunk-ignore(bandit/B105)
    PASSWORD_RESET = "password_reset"
    ACCOUNT_VERIFICATION = "account_verification"
    INVITATION = "invitation"
    NOTIFICATION = "notification" 