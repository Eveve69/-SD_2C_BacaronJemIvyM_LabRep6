from tkinter import *
import tkinter.messagebox

class _TemperatureConversion(Frame):

    def__init__(self):
        Frame.__init__(self)

    # Calculates the Fahrenheit to Celsius conversion
    font = tkinter.font.Font(family = "Arial Black", size = 15)
    self._fahrLabel = Label(self, font = font, text = " Fahrenheit ")
    self._fahrLabel.grid(row = 0, column = 0)
    self._fahrVar = DoubleVar()
    font = tkinter.font.Font(family = "Arial", size = 13)
    self._FahrValue = Entry(self, font = font, fg = "blue", justify =      "center", width = 13,
                            textvariable = self._fahrVar, text = "32.0",)
    self._FahrValue.grid(row = 1, column = 0)

    # Calculates the Celsius to Fahrenheit conversion
    font = tkinter.font.Font(family = "Arial Black", size = 15)
    self._celsLabel = Label(self, font = font, text = " Celsius ")
    self._celsLabel.grid(row = 0, column = 1)
    self._celsVar = DoubleVar()
    font = tkinter.font.Font(family = "Arial", size = 13)
    self._CelsValue = Entry(self, font = font, fg = "red", justify = "center", width = 13,
                                 textvariable = self._celsVar)
    self._CelsValue.grid(row = 1, column = 1)

    # The command buttons
    self._button = Button(self, font = font,
                           text = " >>>> ",
                           command = self._FahrValueN)
    font = tkinter.font.Font(family = "Arial", size = 15)
    self._button.grid(row = 2, column = 0, columnspan = 1)

    self._button = Button(self, font = font,
                           text = " <<<< ",
                           command = self._CelsValue)
    font = tkinter.font.Font(family = "Arial", size = 15)
    self._button.grid(row = 2, column = 1, columnspan = 1)

    #### From here down is not to be indented
    #### Just indented to keep it in the window

def _fahrenheitToCelsius(self):
    Fahr = self._fahrVar.get()
    self._celsVar.set(((Fahr - 32)*5)/9)

def _celsiusToFahrenheit(CelsValue):
     Cels = CelsValue
     Fahr = ((Cels * 9) / 5) + 32
     print(Fahr)

def main():
    _TemperatureConversion().mainloop()
    FahrValue = float(input("Enter a Fahrenheit value to convert: "))
    FConvert = fahrenheitToCelsius(FahrValue)
    CelsValue = float(input("Enter a Celsius value to convert: "))
    CConvert = celsiusToFahrenheit(CelsValue)

if __name__=="__main__":
    main()
