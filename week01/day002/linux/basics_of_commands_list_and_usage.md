# Week 1 - Day 2 - Linux Basic Commands (Usage & Variations)

## 🧠 Objective

To understand how basic Linux commands work, how they are used, and how the same command behaves differently based on options and use cases.

---

# 📌 Commands Covered
```

ls
```
```

pwd
```
```

cd
```
```

mkdir
```
```

rmdir
```
```

touch
```
```

cp
```
```

mv
```
```

rm
```

## 🔹 1. ls (List Files)

### Commands:

```

ls
```
```

ls -a
```
```

ls -l
```
```

ls -lh
```
```

ls -lrt\
```

## Use Cases:

- View files in directory
- View hidden files `-a`
- Detailed file info `-l`
- Human readable size `-lh`
- Sort by time `-lrt`

## Insight:
- Same command → different outputs based on flags
  

-----
# 🔹2. pwd (Present Working Directory)
## command:

```

pwd
```
## Use Cases:
- Shows current directory path

## Insight:
- Useful for navigation awareness
---

# 🔹 3. cd (Change Directory)

## commands
 ```

cd
```
```

cd folder_name
```
```

cd ~
```
```

cd ../../
```
```

cd -
```

## Use Cases:

- Move into folder `cd`
- Move to the named folder `cd /foldwername` for example `cd /home`
- Go to home directly `~`
- If your current location is `/home/user/Documents/Projects` and you run `cd ../../`
   - The first `../` moves you to `/home/user/Documents`
   - The second `../` moves you to `/home/user`
   - Your new working directory becomes `/home/user`
- Switch back to the previous directory you were in `-`

 ## Insight:
  - Relative vs absolute paths

-----


# 🔹 4. mkdir (Make Directory)

## commands:
```

mkdir test
```
```

mkdir folder1 folder2
```
```

mkdir -p parent/child
```
## Use Cases:

- Create single directory `mkdir test`
- Create multiple folders `mkdir folder1 folder2`
- Create nested folders `mkdir -p parent/child`
----

# 🔹 5. rmdir (Remove Directory)

## commands:
```

rmdir folder_name
```

## Use Case:
- deletes empty directory , Will NOT delete non-empty folders `rmdir folder_name`

----

# 🔹 6. touch (Create File)

## commands:
```

touch file.txt
```
```

touch file1.txt file2.txt
```

## Use Case:
- Create new file `touch file.txt`
- Update timestamp `touch file1.txt file2.txt`

----

# 🔹 7. cp (Copy)
## commands:
```

cp file.txt backup.txt
```
```

cp -r folder1 folder2
```

## Use Case:
- Copy file `cp file.txt backup.txt`
- Copy folders recursively `-r`

---
# 🔹 8. mv (Move / Rename)
## commands:
 ```

mv file.txt newfile.txt
```
```

mv file.txt /home/user/
```

## Use Case:
- Rename file `mv file.txt newfile.txt` this stands for `mv file old->name new name`
- Move file `mv file.txt /home/user/` this stands for  `mv file name->distination location`

---
# 🔹 9. rm (Remove)
## commands:
```

rm file.txt
```
```

rm -r folder
```
```

rm -rf folder
```

## Use Case:
- Delete file `rm file.txt` stands for `rm filename` 
- Delete folder`rm -r folder` stands for `rm folder name`
- Force delete `-rf`
- `rm -rf` is dangerous (no confirmation) full os will destroy with this one cammand


















