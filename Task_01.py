
import tkinter as tk

def convert_temperature():
  """Performs the temperature conversion based on user selection."""
  try:
    temperature = float(entry.get())
    if scale_from.get() == "Celsius" and scale_to.get() == "Fahrenheit":
      result = (temperature * 9/5) + 32
    elif scale_from.get() == "Celsius" and scale_to.get() == "Kelvin":
      result = temperature + 273.15
    elif scale_from.get() == "Fahrenheit" and scale_to.get() == "Celsius":
      result = (temperature - 32) * 5/9
    elif scale_from.get() == "Fahrenheit" and scale_to.get() == "Kelvin":
      result = (temperature - 32) * 5/9 + 273.15
    elif scale_from.get() == "Kelvin" and scale_to.get() == "Celsius":
      result = temperature - 273.15
    elif scale_from.get() == "Kelvin" and scale_to.get() == "Fahrenheit":
      result = (temperature - 273.15) * 9/5 + 32
    else:
      result = "Invalid selection"

    result_label.config(text=f"{result:.2f}")

  except ValueError:
    result_label.config(text="Invalid input. Please enter a number.")

# Create main window
window = tk.Tk()
window.title("Temperature Converter")

# Input label and entry
input_label = tk.Label(window, text="Enter temperature:")
input_label.grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=5, pady=5)

# From scale dropdown
scale_from_label = tk.Label(window, text="From:")
scale_from_label.grid(row=1, column=0, padx=5, pady=5)
scale_from = tk.StringVar(window)
scale_from.set("Celsius")  # Default value
scale_from_dropdown = tk.OptionMenu(window, scale_from, "Celsius", "Fahrenheit", "Kelvin")
scale_from_dropdown.grid(row=1, column=1, padx=5, pady=5)

# To scale dropdown
scale_to_label = tk.Label(window, text="To:")
scale_to_label.grid(row=2, column=0, padx=5, pady=5)
scale_to = tk.StringVar(window)
scale_to.set("Fahrenheit") # Default value
scale_to_dropdown = tk.OptionMenu(window, scale_to, "Celsius", "Fahrenheit", "Kelvin")
scale_to_dropdown.grid(row=2, column=1, padx=5, pady=5)

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Result label
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()