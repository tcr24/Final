from pathlib import Path
from app.core.config import settings
from app.utils.email import send_email

def send_pro_upgrade_email(email_to: str, username: str) -> None:
    subject = f"{settings.PROJECT_NAME} - Professional Status Upgrade"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "pro_upgrade.html") as f:
        template_str = f.read()
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={"project_name": settings.PROJECT_NAME, "username": username},
    )
