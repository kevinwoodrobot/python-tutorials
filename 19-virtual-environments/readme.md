

Virtual Environemnt Steps 
1. set up environmental variables for location of python.exe 
2. python --version to check it works 
3. python -m venv myEnvName  
4. .\myEnvName\Scripts\activate
May see this error 
.\myEnvName\Scripts\activate : File G:\My Drive\youtube\python\virtual-environments\myEnvName\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies 

5. Go to ctrl + shift + p for settings.json and choose Open user settings json and add the lines below 
found from [here](https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl/67420296#67420296)

``` markdown
"terminal.integrated.profiles.windows": {
  "PowerShell": {
    "source": "PowerShell",
    "icon": "terminal-powershell",
    "args": ["-ExecutionPolicy", "Bypass"]
  }
},
"terminal.integrated.defaultProfile.windows": "PowerShell",
```

6. Close powershell windows to refresh and try again. You will see a (myEnvName) show up in the terminal in blue to mean you are in the environment 
