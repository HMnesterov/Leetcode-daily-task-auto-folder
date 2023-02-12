## Simple script for LeetCode daily task

## 

Launch
------

```
git clone https://github.com/BenitoSwaggolini/Leetcode-daily-task-auto-folder.git
python -m venv venv
.\venv\Scripts\activate
cd Leetcode-daily-task-auto-folder
pip install -r requirements.txt
pyinstaller --onefile main.py -w 
```
##
Add main.exe file in your auto launch and run it.
If your antivirus will block the script, then you should add file to whitelist 

Opportunities(over time, there will be more of them):
------

* Script will parse the LeetCode main page and take from it task name, task description and difficult.
* After this, he'll create folders for your future solution in your absolute path, which you settled
