# personal_settings

quick way to sync my settings between devices

## How to use it?
Pull this repo to a new device, and:
- create soft link to .vimrc file
- create soft link to .ssh/config file

## to-do list
- do something similar for a .bashrc script
- update files in vscode folder
- update files in windows_terminal folder

## Notes
Probably a good idea to create a script to automate all of that

### security
ssh setup only syncs ssh prompts, creating a useful workspace with consistent alias names. All the private ssh keys should be put in the .ssh/keys directory. It is a manual process for security reasons. 

