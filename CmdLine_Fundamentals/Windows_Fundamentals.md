<h1 align="center">
Windows Command Line Fundamentals
</h1>

OSX and Linux operating systems are both based on Unix and share many of the same 
terminal commands.

Windows has an entirely different kernel (base) and has traditionally had its own 
command-line syntax for MS-DOS and command prompt.

However, Powershell has adopted aliases that mimic the most common Unix commands.

**Powershell** ships with all modern Windows systems (since Windows 7) and is a 
superior shell to command prompt. It compares favorably with Unix-based shells, 
such as bash.

Most of the commands listed for Mac OSX is similar to Windows. The main difference 
would be the **touch** command. Within Windows, the following command will work 
similarly to the touch command in Powershell:

    function touch {New-Item -ItemType File -Name ($args[0])}

Normally, the command to create a new file within Powershell is:

    New-Item -ItemType filename.py
