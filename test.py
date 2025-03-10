from pywinauto.findwindows import find_elements

elements = find_elements()
for elem in elements:
    print(f"Title: {elem.name}, Class: {elem.class_name}, Process ID: {elem.process_id}")
