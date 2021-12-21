# Python file renamer
**A simple python script for renaming files without weird characters.**

Had a lot of files with chinese and shitty characters so I made this script for renaming them.

The `[0001]` is because I had less than 10k files, and if a file is called `"阴茎"` and the next one is called `"性别"`, both files would be stored as `"--"`, so I use a numeric id to make sure they have different names.

It uses a "character whitelist" to know which characters are safe to rename. In this case `string.printable`.
