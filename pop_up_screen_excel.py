import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=200, bg='lightsteelblue')
canvas1.pack()


def getExcel():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel(import_file_path)
    # print(df)


browseButton_Excel = tk.Button(text='Import Excel Files', command=getExcel,
                               bg='green', fg='white', font=('helvetica', 20, 'bold'))
canvas1.create_window(150, 100, window=browseButton_Excel)
root.mainloop()

# df - excel citit
