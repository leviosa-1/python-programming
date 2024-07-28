import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# Function to generate the certificate
def generate_certificate():
    name = name_entry.get()
    event = event_entry.get()

    # Load the certificate template image
    template_image = Image.open("template.png")
    draw = ImageDraw.Draw(template_image)

    # Specify the font and font size for the text
    font = ImageFont.truetype("arial.ttf", 48)

    # Calculate the text position
    text_width, text_height = draw.textsize(name, font=font)
    text_x = (template_image.width - text_width) / 2
    text_y = 400

    # Add the name and event text to the certificate
    draw.text((text_x, text_y), name, fill="black", font=font)
    draw.text((text_x, text_y + 100), event, fill="black", font=font)

    # Save the generated certificate
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    template_image.save(save_path)

    # Display success message
    status_label.config(text="Certificate generated successfully!")

# Create the main window
window = tk.Tk()
window.title("Certificate Generator")

# Create labels and entry fields for name and event
name_label = tk.Label(window, text="Recipient Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

event_label = tk.Label(window, text="Event Name:")
event_label.pack()
event_entry = tk.Entry(window)
event_entry.pack()

# Create the "Generate Certificate" button
generate_button = tk.Button(window, text="Generate Certificate", command=generate_certificate)
generate_button.pack()

# Create a label to display status messages
status_label = tk.Label(window, text="")
status_label.pack()

# Start the Tkinter event loop
window.mainloop()
