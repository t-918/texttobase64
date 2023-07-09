import tkinter as tk
import base64

def convert_to_base64():
    input_text = text_entry.get("1.0", tk.END).strip()
    encoded_bytes = base64.b64encode(input_text.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")
    result_label.config(text="Base64 encoded string:", fg="#202A25")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, encoded_string)

# Create the main window
window = tk.Tk()
window.title("Base64 Encoder")
window.geometry("500x400")
window.configure(bg="#5F4BB6")

# Create the header label
header_label = tk.Label(window, text="Base64 Encoder", font=("Calibri", 20, "bold"), bg="#86A5D9", fg="#202A25")
header_label.pack(pady=20)

# Create the input text box
text_entry = tk.Text(window, height=4, width=40, font=("Calibri", 13))
text_entry.pack(pady=10)

# Create the convert button
convert_button = tk.Button(window, text="Convert to Base64", font=("Calibri", 15, "bold"), command=convert_to_base64, bg="#86A5D9", fg="#202A25")
convert_button.pack()

# Create the result label and text box
result_label = tk.Label(window, text="", font=("Calibri", 12, "bold"), bg="#F5F5F5", fg="#202A25")
result_label.pack(pady=10)

result_text = tk.Text(window, height=4, width=40, font=("Calibri", 12))
result_text.pack()

# Set focus on the input text box
text_entry.focus()

# Start the main event loop
window.mainloop()
