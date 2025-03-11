from pywinauto.findwindows import find_elements

# 查找当前所有窗口
elements = find_elements()
for elem in elements:
    print(f"Title: {elem.name}, Class: {elem.class_name}, Process ID: {elem.process_id}")