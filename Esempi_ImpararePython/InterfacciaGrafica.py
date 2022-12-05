import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Hello TkInter!")
# window.resizable(False, False)
# window.configure(background="white")


def first_print():
    text = "Hello World!"
    text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 16))
    text_output.grid(row=0, column=1, sticky="W")

def second_function():
    text = "Nuovo Messaggio! Nuova Funzione!"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=1, column=1, padx=50, sticky="W")

first_button = tk.Button(text="Saluta!", command=first_print)
first_button.grid(row=0, column=0, sticky="W")

second_button = tk.Button(text="Seconda Funzione", command=second_function)
second_button.grid(row=1, column=0, pady=20, sticky="W")


if __name__ == "__main__":
    window.mainloop()
import tkinter as tk
import requests

window = tk.Tk()
window.geometry("900x550")
window.title("ASCII ART DOWNLOADER")
window.grid_columnconfigure(0, weight=1)


def download_ascii():
    if text_input.get():
        user_input = text_input.get()
        payload = {"text": user_input}
        response = requests.get("http://artii.herokuapp.com/make",
                                params=payload)
        text_response = response.text
    else:
        text_response = "Aggiungi una parola o una frase al campo input!"

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

    credits_label = tk.Label(window, text="ascii art by artii.herokuapp.com")
    credits_label.grid(row=4, column=0, sticky="S", pady=10)


welcome_label = tk.Label(window,
                         text="Welcome! Aggiungi una parola o una frase da scaricare:",
                         font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)

download_button = tk.Button(text="DOWNLOAD ASCII ART", command=download_ascii)
download_button.grid(row=2, column=0, sticky="WE", pady=10, padx=10)


if __name__ == "__main__":
    window.mainloop()