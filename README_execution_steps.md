# Partner Signup Automation Script

Automates the end-to-end signup flow for the Authorized Partner platform using Selenium WebDriver and the Mail.tm API for temporary email and OTP retrieval.

## Prerequisites

- Python 3.8+
- Google Chrome browser (latest version)
- Internet connection

## Setup & Installation

```bash
# Clone or navigate to the project directory
cd vrit_task

# Install required dependencies
pip install requests selenium webdriver-manager
```

## How to Run

```bash
python signup_automation_script
```

The script will:

1. Generate a random temporary email and phone number.
2. Launch Chrome and navigate to the signup page.
3. Fill in personal details (name, email, phone, password).
4. Wait for the OTP email to arrive via Mail.tm API and auto-fill it.
5. Complete Agency Details, Professional Experience, and Verification steps.
6. Upload required certificates (`registration.pdf`, `education.pdf` from the `uploads/` folder).
7. Submit the form and print success/failure status.

### Expected Output

```
Using email: testXXXXXXXX@web-library.net
Using phone: 98XXXXXXXX
Waiting for OTP email...
OTP received: 123456
Filling Agency Details...
Filling Professional Experience...
Filling Verification and Preferences...
Signup completed successfully!
```

## Environment Details

| Component | Version / Name |
|-----------|---------------|
| Language | Python 3.8+ |
| Browser | Google Chrome (latest) |
| ChromeDriver | Managed automatically by `webdriver-manager` |
| HTTP Client | `requests` |
| Temporary Email API | Mail.tm (`https://api.mail.tm`) |
| Target URL | `https://authorized-partner.vercel.app/` |

### Key Dependencies

| Package | Purpose |
|---------|---------|
| `selenium` | Browser automation |
| `webdriver-manager` | Automatic ChromeDriver binary management |
| `requests` | API calls to Mail.tm for temp email & OTP |

## Test Data & Accounts

| Field | Value Used | Notes |
|-------|-----------|-------|
| First Name | Bibek | Static |
| Last Name | Limbu | Static |
| Email | `test{8 digits}@web-library.net` | Dynamically generated via Mail.tm |
| Phone | `98{8 random digits}` | Dynamically generated |
| Password | `Password@123` | Static |
| Agency Name | No_Agency | Static |
| Role in Agency | Intern | Static |
| Agency Email | agency@yopmail.com | Static |
| Agency Website | www.agency.com | Static |
| Agency Address | Kathmandu, Nepal | Static |
| Region | Nepal | Static |
| Years of Experience | 3 years | Static |
| Students Recruited Annually | 3000 | Static |
| Focus Area | Undergraduate admissions to Canada. | Static |
| Success Metrics | 85 | Static |
| Services | Visa Processing | Static |
| Business Registration | REG12345 | Static |
| Preferred Country | Australia | Static |
| Institution Type | Universities | Static |
| Certification | Bachelor in Computer Science | Static |
| Upload Files | `uploads/registration.pdf`, `uploads/education.pdf` | Must exist locally |

## Project Structure

```
vrit_task/
├── signup_automation_script   # Main automation script
├── README_execution_steps.md  # This file
└── uploads/
    ├── registration.pdf       # Company registration certificate
    └── education.pdf          # Educational certificate
```

## Notes

- Mail.tm accounts are disposable and do not require real registration.
- The OTP polling loop waits up to 60 seconds (checking every 3 seconds) for the verification email.
- File uploads require `registration.pdf` and `education.pdf` to be present inside the `uploads/` directory relative to the script.
- The script uses `os.path.abspath()` to resolve file paths, so it must be run from the project root.
