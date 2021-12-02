from tkinter import *
import os
import webbrowser
root = Tk()

def run(event):
    if ("yts" in userInput.get()):
        print("Seacrhing on youtube...")
        replace = userInput.get().replace("yts", "")
        final_replace = replace.replace(" ", "+")
        final = "https://www.youtube.com/results?search_query="+final_replace
        webbrowser.open(final)
        quit()

    elif "chrome" in userInput.get():
        path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.chrome.exe"
        os.startfile(path)
        quit()

    elif "code" in userInput.get():
        path = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)   
        quit()

    elif (("wtsp" in userInput.get()) or ("whtasapp" in userInput.get()) or ("Whatsapp" in userInput.get())):
        print(userInput.get())
        stream = "https://web.whatsapp.com/"
        webbrowser.open(stream)
        quit()  


    elif (("git" in userInput.get()) or ("gitbash" in userInput.get()) or ("gb" in userInput.get())):
        os.startfile("C:\\Program Files\\Git\\git-bash.exe") 
        quit()  

    elif (("exp" in userInput.get()) or ("explorer" in userInput.get())):
        stream = "C:\\Users\\admin\\Desktop"     
        os.startfile(stream)
        quit()

    elif (("yt" in userInput.get()) or ("youtube" in userInput.get())):
        print("YT")
        webbrowser.open("https://youtube.com/")       
        quit()

    elif("\\" in userInput.get()):
        replace = userInput.get().replace("\\","/")
        os.startfile(replace)
        print(replace)
        quit()

    else:
        stream1 = userInput.get().replace(" ", "+")
        mainStreamZ = "https://www.google.com/search?q="+stream1
        webbrowser.open(mainStreamZ)
        quit()




def googleSearch(event):
    stream1 = userInput.get().replace(" ", "+")
    mainStreamZ = "https://www.google.com/search?q="+stream1
    webbrowser.open(mainStreamZ)
    quit()

def youtubeSearch(event):
    replace = userInput.get().replace(" ", "+")
    final = "https://www.youtube.com/results?search_query="+replace
    webbrowser.open(final)
    quit()

def folder(event):
    replace = userInput.get().replace("\\","/")
    os.startfile(replace)
    print(replace)
    quit()


root.bind('<Return>', run)
root.bind('<Control-g>', googleSearch)
root.bind('<Control-y>', youtubeSearch)
root.bind('<Control-f>', folder)
root.geometry('300x150')
root.title("RunX")
# Label(text="Code: ")
userInput = StringVar()
e1 = Entry(root, textvariable=userInput)
e1.pack()
b1 = Button(root, text = "Run", command = run)
b1.pack()
b2 = Button(root, text = "Google Search", command = googleSearch)
b2.pack()
b3 = Button(root, text = "Youtube Search", command = youtubeSearch)
b3.pack()
root.mainloop()