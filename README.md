# git-smart-filter-example
Git Smart Filter Example (For the people)

Check out .gitignore and add the following to a 'master' local repository .git/config file.

Also checkout the repository to a 'slave' repository without adding the filter script to .git/config.

**.gitattributes**

```
data/*.txt filter=timestampify
```

**.git/config**

```
[filter "timestampify"]
        clean = filter/timestampify.py clean %f
        smudge = filter/timestampify.py smudge %f
        required = true
```

The filter will run on the master during adds/commits/etc.. and attempt to replace a variable on the same line as a specialized command word called TIMESTAMPIFY:

```
Replace this var TIMESTAMP //TIMESTAMPIFY:EPOCH:TIMESTAMP:
```

The above will run an command called **EPOCH** on that line and commit a finalized version to git.. while keeping an untouched version available locally on a master.  Only changed files will be uploaded.
