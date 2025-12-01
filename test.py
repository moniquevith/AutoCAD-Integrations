from pyautocad import Autocad, APoint

# automatically connect to open acad
acad = Autocad(create_if_not_exists=True)

acad = Autocad()

target_table = None
search_text = "Test Table".lower()

for obj in acad.iter_objects():
    if obj.ObjectName == "AcDbTable":
        cols = obj.Columns
        for col in range(cols):
            cell_text = obj.GetText(0, col)
            if cell_text and search_text in cell_text.lower():
                target_table = obj
                print("Found matching table")
                break
        if target_table:
            target_table.SetText(1, 1, "Hello") # add text
            target_table.SetText(2, 1, "World")
            target_table.SetText(2, 2, "World")

            target_table.SetTextHeight(1, 40) # change font size to 40

            target_table.SetAlignment(1, 5) # middle centre align (5th selection)
            target_table.Update()

if not target_table:
    print("No table with 'test table' in header row found.")
else:
    print("Table identified successfully.")