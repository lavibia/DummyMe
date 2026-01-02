1. Download latest version of Git Bash
2. Set the user name
``` $ git config --global user.name "Your username"```
3. Set your email
```$ git config --global user.email "uremail@example.com"```
4. Generate SSH key
```$ ssh-keygen -t ed25519 -C "uremail@example.com"``` and follow instructions
5. Add the SSH Key to GitHub from its location
**Your public key has been saved in /c/Users/you/.ssh/id_ed25519.pub**

Now you are ready to clone your repo using the SSH link using ```git clone link```
