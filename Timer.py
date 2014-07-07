import time
import Tkinter

class Timer(Tkinter.Frame):
    
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.mode = "stopped"
        self.start_time = 0
        self.elapsed_time = 0
        root.wm_title('Simple Python Stopwatch')
        self.create_buttons()
        self.update_timeText()

    def create_buttons(self):
        self.timeText = Tkinter.Label(root, text="00:00:00", font=("Calibri", 100))
        self.timeText.pack()

        self.start_pause_unpause_Button = Tkinter.Button(root, text='Start', command=self.start_pause_unpause)
        self.start_pause_unpause_Button.pack()

        reset_button = Tkinter.Button(root, text='Reset', command=self.reset)
        reset_button.pack()

        quit_button = Tkinter.Button(root, text='Quit', command=self.exit)
        quit_button.pack()

    def set_time(self, hours, minutes, seconds):
        pattern = '{0:02d}:{1:02d}:{2:02d}'
        timeString = pattern.format(hours, minutes, seconds)
        self.timeText.configure(text=timeString)
        
    def update_timeText(self):
        if self.mode == "running":
            time_elapsed = time.time() - self.start_time + self.elapsed_time
            seconds = int(time_elapsed % 60)
            minutes = int((time_elapsed/60) % 60)
            hours = int((time_elapsed/3600) % 60)
            self.set_time(hours, minutes, seconds)
        self.after(100, self.update_timeText)

    def start_pause_unpause(self):
        if self.mode == "stopped":
            self.start_time = time.time()
            self.mode = "running"
            self.start_pause_unpause_Button.config(text="Pause")
        elif self.mode == "running":
            self.elapsed_time = self.elapsed_time + time.time() - self.start_time
            self.mode = "stopped"
            self.start_pause_unpause_Button.config(text="Resume")

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.set_time(0,0,0)
        self.start_pause_unpause_Button.config(text="Start")

    def exit(self):
        root.destroy()


root = Tkinter.Tk()
app = Timer(master=root)

app.mainloop()
