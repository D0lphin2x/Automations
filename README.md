# ⏱ Workday Time Logger Automation (macOS + Selenium)

This Python script automatically logs 8 hours of time in Workday using Selenium and Microsoft Edge. It is designed to be run daily at a set time (e.g., 5 PM) and handles the login and time entry for you, bypassing 2FA via a persistent browser profile.

---

## 📦 Features

- Automates login and navigation to the Workday time entry screen  
- Detects the current weekday and fills in "8" for that day (Mon–Fri only)  
- Works with persistent login using a custom Edge browser profile  
- Can be scheduled to run daily via macOS `launchd`

---

## 🧰 Requirements

- macOS  
- Python 3.7+  
- [Microsoft Edge](https://www.microsoft.com/edge)  
- [Edge WebDriver (msedgedriver)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  
- Selenium:
  ```bash
  pip install selenium
🔧 Setup Instructions
1. Clone this Repository
bash
Copy
Edit
git clone git@github.com:D0lphin2x/Automations.git 
cd workday-automation
2. Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install selenium
3. Download msedgedriver
Download the correct version of msedgedriver and put it in a known path like:

swift
Copy
Edit
/Users/YOURNAME/Downloads/msedgedriver
4. Configure Your Script
Open the script file and update:

options.add_argument("--user-data-dir=PATH/TO/YOUR/AUTOMATION/PROFILE")
→ Use a custom folder path (e.g., /Users/YOURNAME/edge_automation_profile)

service = Service("PATH/TO/YOUR/msedgedriver")
→ Path to your downloaded msedgedriver

driver.get("REPLACEWITHYOURJOB.com")
→ Replace with your actual Workday login URL (e.g., https://www.myworkday.com/mantech/d/home.htmld)

🧪 First-Time Use
Run the script and follow the first-time instructions in the script (you’ll see input() prompts).

Manually log in through the browser once (this creates a saved profile).

Once you’ve successfully logged in and closed the browser, comment out the initial setup block and uncomment the automation block.

⏰ Automating Daily Execution (macOS only)
1. Create a shell script (e.g., run_workday.sh)
bash
Copy
Edit
#!/bin/zsh
cd /path/to/your/project
source venv/bin/activate
python workday.py
Make it executable:

bash
Copy
Edit
chmod +x run_workday.sh
2. Create a launchd plist
Save this as:
~/Library/LaunchAgents/com.billy.workdayautomation.plist

xml
Copy
Edit
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.billy.workdayautomation</string>

  <key>ProgramArguments</key>
  <array>
    <string>/path/to/your/run_workday.sh</string>
  </array>

  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key>
    <integer>17</integer>
    <key>Minute</key>
    <integer>0</integer>
  </dict>

  <key>RunAtLoad</key>
  <true/>

  <key>StandardOutPath</key>
  <string>/tmp/workday.log</string>
  <key>StandardErrorPath</key>
  <string>/tmp/workday.err</string>
</dict>
</plist>
Then load the agent:

bash
Copy
Edit
launchctl load ~/Library/LaunchAgents/com.billy.workdayautomation.plist
It will now run automatically at 5 PM every day.

🚨 Notes
Make sure your Edge profile saves your login session (bypasses Duo/Okta after first time).

Avoid running the script on weekends (it skips Saturday and Sunday by default).

This script does not store passwords or any credentials directly — all authentication is done via the saved Edge profile.
