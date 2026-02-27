# --- Line 75: Update the content file path ---
with open("emails/OutreachArgentina-20260227.html", encoding="utf-8") as f:
    outreach_html = f.read()

# --- Line 91: Update the subject and variables ---
subject = "GLOBALMIX launches in Argentina — Join the network"
html = template.render(
    newsletter_title=subject,
    name=name,
    background_color="#F5F5F5",
    brand_color="#E136C4",
    email_content_from_file=outreach_html
)

# --- Line 100: Update the message subject ---
msg["Subject"] = subject
