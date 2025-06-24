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
