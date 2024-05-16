import tkinter as tk
import pyttsx3

# display configuration
display1 = tk.Tk()
display1.geometry("800x400")
display1.title("Text to Speech")
display1.resizable(False, False)


def speak():
    speech1 = pyttsx3.init()
    speech1.say(text1.get(1.0, tk.END))
    text1.delete(1.0, tk.END)
    text1.insert(1.0, "You can enter a text here for the machine to speak")
    speech1.runAndWait()


# text area and buttons
text1 = tk.Text(display1)
text1.place(x=8, y=8, height=386, width=750)

run_button = tk.Button(display1,
                       text="Run",
                       command=speak)
run_button.place(x=762, y=8, width=36, height=185)

exit_button = tk.Button(display1,
                        text="Exit",
                        command=quit,
                        bg="red",
                        fg="black",
                        relief="sunken",
                        borderwidth=3,
                        activebackground="blue",
                        activeforeground="red")
exit_button.place(x=762, y=200, width=36, height=194)


display1.mainloop()
