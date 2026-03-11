import re

def extract_emails(input_file, output_file):
    with open(input_file) as f:
        content = f.read()

    pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    emails = list(dict.fromkeys(re.findall(pattern, content)))

    with open(output_file, "w") as f:
        f.write("\n".join(emails))

    print(f"Found {len(emails)} email(s) → saved to '{output_file}'")

extract_emails("contacts.txt", "emails.txt")