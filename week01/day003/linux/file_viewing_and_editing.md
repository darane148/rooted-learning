# Week 1 - Day 3 - File Viewing & Editing Commands

## 🧠 Objective

To understand how to view, read, and edit files in Linux using different commands, and how each tool behaves differently based on use cases.

---

# 📌 Commands Covered
```

cat
```
```

less
```
```

more
```
```

nano
```
```

vim
```

# 🔹 1. cat (Concatenate)

## commands:
```

cat file.txt
```
```
 
cat file1.txt file2.txt
```  

## Use Cases:

- View file content  
- Combine multiple files  
- Quick reading (small files)  

## Insight:
- Displays full content at once  
- Not suitable for large files  

-----

# 🔹 2. less (Advanced Viewer)

## commands:
```

less file.txt
```  

## Use Cases:

- View large files  
- Scroll up and down  

## Controls:
- q → quit  
- /word → search  

## Insight:
- Best tool for reading large files  

-----

# 🔹 3. more (Basic Viewer)

## commands:
```

more file.txt
```

## Use Cases:

- View file page by page  

## Insight:
- Only scroll down  
- Limited compared to less  

-----

# 🔹 4. nano (Simple Editor)

## commands:
```

nano file.txt
```  

## Use Cases:

- Create and edit files  
- Beginner-friendly  

## Controls:
- CTRL + O → save  
- CTRL + X → exit  

## Insight:
- Easy to use  
- Good for quick edits  

-----

# 🔹 5. vim (Advanced Editor)

## commands:
```

vim file.txt  
```
## Modes:
- Normal mode  
- Insert mode `i` 
- Command mode `:wq`, `:q!`  

## Use Cases:

- Advanced editing  
- Used by professionals  

## Insight:
- Powerful but complex  

-----

# 🔍 Observations

- cat is fast but limited  
- less is best for large files  
- nano is easy for beginners  
- vim is powerful but needs practice  

-----

# 🧪 Practice

- Viewed files using cat, less, more  
- Edited files using nano  
- Practiced basic vim navigation  

-----

# 📸 Proof

Screenshots of file viewing and editing commands are added in the screenshots folder.

-----

# ⚠️ Mistakes

- Confused between less and more  
- Difficulty exiting vim  

-----

# 🧠 Key Learning

Different tools serve different purposes:
- Quick view → cat  
- Large file → less  
- Editing → nano / vim  

-----

# 💡 Hacker Use

- Reading system logs (/var/log)  
- Editing configuration files  
- Analyzing sensitive data  

-----

# 🚀 Next Plan

- Learn process management commands (ps, top, kill)
