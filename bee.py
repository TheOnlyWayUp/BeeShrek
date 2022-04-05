with open("shrek_script.txt", "r") as shrek_script:
    shrek_script = shrek_script.read()

with open("bee_script.txt", "r") as bee_script:
    bee_lines = bee_script.read().splitlines()
    with open("fixed.txt", "w") as fixed:
        for line in bee_lines:
            line = line.replace("bee", shrek_script)
            fixed.write(shrek_script + "\n")
            
