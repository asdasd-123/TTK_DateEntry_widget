## TTK_DateEntry_widget
A ttk widget extention to allow date inputting with validation and retrieval.
Contains option for either grey-filling it with text that will dissappear or 
actuall pre-filling the date.

# Example of how to create the widget.
```python
root = tk.TK()

date1 = DateEntry(root, prefill=False, text="Enter Date Here: YYYY-MM-DD")

date2 = DateEntry(root, prefill=True, text="2019-02-19")
```

# How to retrieve data from the widget.
Get the full date as a datetime object:
```python
full_date = date1.get_date()

Year, Month, and Day:

year = date1.year

month = date1.month

day = date1.day
```

# How to check is date in box is valid.
```python
if date1.is_valid:

    print("date1 is valid")
```
