
*Once upon a time,* there was a piece of software named Publisher 2007.  It could make web pages, and people could look at them on their computers.  Then along came another piece of software named IE8, which made a lot of useful web pages made with Publisher totally unusable because people couldn't see or use the navigation bar.

The people who made Publisher and IE8 didn't take the time to fix the problem, and left people angry at them.

So a lone hacker turned to his console, and came up with a little something to ease their suffering...


Scrubba: the Microsoft Publisher HTML navigation scrubber.
---

It's a little Python program that takes the nasty HTML/XML soup emitted by Publisher and does... very little, in fact, just enough to take out the conditional comment that causes the navigation image map to break.

Usage
===

Dowload and open `Scrubba.zip`.  Inside are some files, but the most important one is `Scrubba.exe`.  Drag a HTML files and even whole folders onto `Scrubba.exe` and revel as Scrubba copies and repairs them!

The intended use of Scrubba is for someone to publish their Publisher pages to a folder, drop the folder on Scrubba, and upload the scrubbed copy of the pages to their website.

Single files
===
Dropping a single HTML file onto `Scrubba.exe` will make a new file in the same place as the original file with `_scrubbed` at the end of the name.  So, if you have `index.htm`, and you drop that on Scrubba, you will have a new file in the folder that `index.htm` is in named `index_scrubbed.htm`.

Directories
===
Dropping a folder full of HTML files onto Scrubba will make a new folder in the same place as the original folder with `_scrubbed` at the end of the name, and then go through all of the HTML files in that folder and clean them.  So if you have a folder named `mysite` and drop that on Scrubba, there will be a new folder named `mysite_scrubbed` in the same place as `mysite`.  HTML files in the new folder will have the same names as the ones in `mysite`, but they will be scrubbed to work with IE8.

Building
---
Scrubba is a straightforward distutils-enabled project.  `Scrubba.zip` was made using `py2exe` with Python 2.6 on Windows Vista.  To make a new executable, run:

    % python setup.py py2exe

Per usual, the intermediate files are in `build` and the executable is in `dist`.
