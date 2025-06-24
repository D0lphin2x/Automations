# ⏱ Workday Time Entry Automation

Automate your daily Workday time logging using Selenium and Edge on macOS. This script logs 8 hours for the current weekday (Mon–Fri) in the "Enter Time by Type" view.

---

## 📦 Features

- ✅ Automatically logs 8 hours to today's date (Mon–Fri)
- ✅ Navigates through Workday: Time → This Week → Enter Time by Type → Save
- ✅ Bypasses Okta/MFA with a saved browser profile
- ✅ Works with Microsoft Edge and Edge WebDriver
- ✅ Schedules automatically to run every weekday at 5 PM

---

## 🧰 Requirements

- macOS
- Python 3.10+
- Microsoft Edge
- Edge WebDriver (msedgedriver)
- Selenium (`pip install selenium`)

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/Automations.git
cd Automations
2. Create Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install selenium
3. Install Edge WebDriver
Download from: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Extract and place somewhere safe (e.g., ~/Downloads/msedgedriver)

⚙️ Configure workday.py
Open the workday.py file and edit these lines:

a. Set Edge Profile Path
python
Copy
Edit
options.add_argument("--user-data-dir=/Users/USERNAME/edge_automation_profile")
This folder stores your login session so you don’t need to enter Duo/MFA every day.

b. Set msedgedriver Path
python
Copy
Edit
service = Service("/Users/USERNAME/Downloads/msedgedriver")
c. Set Your Workday URL
python
Copy
Edit
driver.get("https://www.myworkday.com/YOURCOMPANY/d/home.htmld")
🧪 First-Time Setup (Session Capture)
Run the script:

bash
Copy
Edit
python workday.py
Log in manually with your username, password, and Okta/Duo if needed.

Once you're logged in and see your Workday homepage, press Enter in Terminal — the window will close.

Now edit workday.py to comment out the first-time setup section and uncomment the automation block (already included in comments).

✅ Running the Script
Once your session is saved:

bash
Copy
Edit
python workday.py
It will:

Click Time

Choose "This Week"

Click "Enter Time by Type"

Find the correct weekday input

Enter 8

Click "Save and Close"

⏰ Automate Daily with launchd (macOS Only)
1. Create a Shell Script
Create run_workday.sh in the same folder:

bash
Copy
Edit
#!/bin/zsh
cd /Users/USERNAME/Path/To/Automations
source venv/bin/activate
python workday.py
Make it executable:

bash
Copy
Edit
chmod +x run_workday.sh
2. Create a Launch Agent
Create this file:
~/Library/LaunchAgents/com.username.workdayautomation.plist

Paste this:

xml
Copy
Edit
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.username.workdayautomation</string>

  <key>ProgramArguments</key>
  <array>
    <string>/Users/USERNAME/Path/To/Automations/run_workday.sh</string>
  </array>

  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key>
    <integer>17</integer>
    <key>Minute</key>
    <integer>0</integer>
  </dict>

  <key>StandardOutPath</key>
  <string>/tmp/workday.log</string>
  <key>StandardErrorPath</key>
  <string>/tmp/workday.err</string>

  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
3. Load the Agent
bash
Copy
Edit
launchctl load ~/Library/LaunchAgents/com.username.workdayautomation.plist
(Optional) To start it manually:

bash
Copy
Edit
launchctl start com.username.workdayautomation
Check logs:

bash
Copy
Edit
cat /tmp/workday.log
cat /tmp/workday.err
