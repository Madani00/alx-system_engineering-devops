# Bash Basics

## 1. Creating SSH Keys

```bash
ssh-keygen -t rsa -b 2048 -C "your_email@example.com"
```

* ssh-keygen: Command to generate SSH keys.
* -t rsa: Specifies the key type (RSA).
* -b 2048: Specifies the number of bits in the key (2048 bits is commonly used).
* -C "your_email@example.com": Adds a label/comment to identify the key.

## 2. Advantage of #!/usr/bin/env bash over #!/bin/bash
The #!/usr/bin/env bash allows using the Bash interpreter from the user's environment, providing flexibility in locating the Bash executable.

## 3. Using Loops
### While Loop
```
while [ condition ]; do
  # Code to execute
done
```
### Until Loop
```
until [ condition ]; do
  # Code to execute
done
```
## For Loop
```
for variable in list; do
  # Code to execute
done
```

## 4. Conditional Statements
### If Statement
```
if [ condition ]; then
  # Code to execute if condition is true
fi
```
### Else Statement
```
if [ condition ]; then
  # Code to execute if condition is true
else
  # Code to execute if condition is false
fi
```
### Elif Statement
```
if [ condition1 ]; then
  # Code to execute if condition1 is true
elif [ condition2 ]; then
  # Code to execute if condition2 is true
else
  # Code to execute if all conditions are false
fi
```
### Case Statement
```
case $variable in
  pattern1) # Code for pattern1 ;;
  pattern2) # Code for pattern2 ;;
  *) # Default code if no pattern matches ;;
esac
```
## 5. Using the Cut Command
```
cut -d delimiter -f fields file
```
* cut: Command to extract sections from each line of a file.
* -d delimiter: Specifies the delimiter character.
* -f fields: Specifies the fields to extract.
* file: The input file.
  
## 6. File Comparison Operators
* -eq: Equal to
* -ne: Not equal to
* -lt: Less than
* -le: Less than or equal to
* -gt: Greater than
* -ge: Greater than or equal to
Other Comparison Operators:
* ==: String equality in some contexts.
* !=: String inequality in some contexts.
Used in conditional statements to compare values.
