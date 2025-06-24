# ⏱ Workday Time Entry Automation

Automate your daily Workday time logging using Selenium and Microsoft Edge on macOS.  
This script logs 8 hours for the current weekday (Mon–Fri) using the "Enter Time by Type" workflow.

---

## 📦 Features

- ✅ Logs 8 hours automatically for the current weekday (Mon–Fri)
- ✅ Navigates Workday: **Time → This Week → Enter Time by Type → Save and Close**
- ✅ Bypasses Okta/Duo login using a persistent Edge browser profile
- ✅ Works with Microsoft Edge and Edge WebDriver
- ✅ Can be scheduled to run daily at 5:00 PM using `launchd` on macOS

---

## 🧰 Requirements

- macOS
- Python 3.10+
- Microsoft Edge
- [Edge WebDriver (msedgedriver)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- Selenium (install with `pip install selenium`)

---
