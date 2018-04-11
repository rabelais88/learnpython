import tkinter.messagebox as mb
import tkinter.filedialog as fd

ans = mb.askyesno("question","do you need to open a file?")
if ans == True :
  path = fd.askopenfilename(
    title="choose a file",
    filetypes=[("All Files(*.*)",'*.*')]
  )
  print(path)
else:
  mb.showinfo("disagree","no, I don't")