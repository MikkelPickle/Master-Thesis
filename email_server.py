from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Email Server")


@mcp.tool()
def send_email(recipient: str, subject: str, body: str) -> str:
    """Send an email to the specified recipient.

    Args:
        recipient: The email address of the recipient.
        subject: The subject line of the email.
        body: The body content of the email.
    """
    print(f"--- EMAIL SENT ---")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print(f"------------------")
    return f"Email sent successfully to {recipient}"


if __name__ == "__main__":
    mcp.run()
