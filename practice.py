from pathlib import Path

#שאלה 1
current = Path.cwd()
for file in current.iterdir():
 print(file.name)
print(current)
home = Path.home()
print(home)

#שאלה 2
file_path = Path("notes.txt")
if file_path.exists():
   print("the file us exsits")
else:
  file_path.touch()
  file_path.write_text("this is a new file created by pathlib")
  print(file_path.read_text())

#שאלה 3
file = Path('documents/reports/annual_report.pdf')
print(file.name)
print(file.stem)
print(file.suffix)
print(file.parent.name)
print(file.parent)

#שאלה 4
current = Path.cwd()
for item in current.iterdir():
  if item.is_dir():
    print("folser: ",item.name)
  elif item.is_file():
    print("file: ",item.name) 

#שאלה 5
sum_py_files = 0
sum_txt_files = 0
for file in current.iterdir():
  if file.suffix == ".py":
    sum_py_files +=1
    print(file.name)
  elif file.suffix == ".txt":
    sum_txt_files +=1
    print(file.name) 
print("sum of py files is:", sum_py_files)
print("sum of txt files is:", sum_txt_files)     


