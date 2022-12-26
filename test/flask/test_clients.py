import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from ecg_analysis import parse_data, heartrate_analysis
import base64
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import requests


def convert_file_to_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding="utf-8")
    return b64_string


def resize_display(image_path):
    image = Image.open(image_path)
    image = image.resize((image.width // 2, image.height // 2))
    photo = ImageTk.PhotoImage(image)
    label= tk.Label(root, image=photo)
    label.image = photo
    return label


def analyze_data(data_path):
    time, voltage, high_voltages = parse_data(data_path)
    result_metrics = heartrate_analysis(time, voltage)
    global hr_input
    hr_input = result_metrics["mean_hr_bpm"]
    tk.Label(root, text="The mean heart rate is: " + str(hr_input)).grid(
            column=5, row=2, padx=10, pady=10
        )
    plt.close()
    plt.plot(time, voltage)
    plt.savefig("ECG_trace.png")

def clear_image():
    global label_m
    label_m.destroy()
    global medim
    medim = None
    ttk.Label(root, text="     new medical image wait to update    ").grid(
        column=0, row=7, padx=10, pady=10
    )
def clear_name():
    patient_name_entry.delete(0, "end")
    global patientname
    patientname = ""
    ttk.Label(root, text="       new ECG data wait to update    ").grid(
        column=0, row=6, padx=10, pady=10
    )

def clear_reco():
    rec_no_entry.delete(0, "end")
    global recno
    recno = None

def clear_ecg():
    global label_e
    label_e.destroy()
    ttk.Label(root, text="       new ECG data wait to update    ").grid(
        column=0, row=8, padx=10, pady=10
    )
    global hr_input
    hr_input = None
    global ECGtrace
    ECGtrace = None
    tk.Label(root, text="The mean heart rate waiting for update").grid(
            column=5, row=2, padx=10, pady=10
        )

def main_window():
    root = tk.Tk()
    root.title("Patient-Side window welcome you!")
    # set size of the window
    root.geometry("1200x900")

    global patientname
    patientname = None
    global hr_input
    hr_input = None
    global medim
    medim = None
    global ECGtrace
    ECGtrace = None

    # input patient name
    ttk.Label(root, text="Patient Name : ").grid(column=0, row=0, padx=10, pady=10)
    patientname = tk.StringVar()
    patient_name_entry = ttk.Entry(root, width=20, textvariable=patientname)
    patient_name_entry.grid(column=1, row=0, padx=10, pady=10)
    print(patientname.get())

    # input patient medical record number.
    ttk.Label(root, text="Patient Medical Record Number : ").grid(
        column=0, row=1, padx=10, pady=10
    )
    recno = tk.StringVar()
    rec_no_entry = ttk.Entry(root, width=20, textvariable=recno)
    rec_no_entry.grid(column=1, row=1, padx=10, pady=10)
    print(recno.get())


    # select medical image
    def select_image():
        image_path = filedialog.askopenfilename()
        global medim
        medim = convert_file_to_b64(image_path)
        global label_m
        # for second time selection of image
        label_m=resize_display(image_path)
        label_m.grid(column=4, row=1, padx=10, pady=10)


    # image show section label
    ttk.Label(root, text="Medical image : ").grid(
        column=4, row=0, padx=10, pady=10
    )
    ttk.Label(root, text="ECG trace : ").grid(column=5, row=0, padx=10, pady=10)

    # image button
    ttk.Label(root, text="Select and display medical image : ").grid(
        column=0, row=2, padx=10, pady=10
    )
    med_im_button = ttk.Button(root, text="Browse", command=lambda: select_image())
    med_im_button.grid(column=1, row=2, padx=10, pady=10)


    def select_data():
        data_path = filedialog.askopenfilename()
        analyze_data(data_path)
        global ECGtrace
        ECGtrace = convert_file_to_b64("ECG_trace.png")
        global label_e
        label_e=resize_display("ECG_trace.png")
        label_e.grid(column=5, row=1, padx=10, pady=10)

    # ECG data button
    ttk.Label(root, text="Select a ECG data for analysis (csv): ").grid(
        column=0, row=3, padx=10, pady=10
    )
    ecg_button = tk.Button(root, text="Browse", command=select_data)
    ecg_button.grid(column=1, row=3, padx=10, pady=10)

    # save
    server = "http://localhost:5000"


    def save_patient_info():
        if recno.get():
            save_patient()
            save_medical_image()
            save_ECG_data()
        else:
            tkinter.messagebox.showwarning(
                "Missing record number", "Please enter an record number."
            )


    def save_patient():
        if patientname.get() == "":
            return
        else:
            url = server + "/new_patientname"
            x = requests.post(url, json=[recno.get(), patientname.get()])
            ttk.Label(root, text=x.text).grid(column=0, row=6, padx=10, pady=10)


    def save_medical_image():
        if medim is None:
            return
        else:
            url = server + "/new_medim"
            x = requests.post(url, json=[recno.get(), medim])
            msg = x.text
            ttk.Label(root, text=msg).grid(column=0, row=7, padx=10, pady=10)


    def save_ECG_data():
        if hr_input is None:
            return
        else:
            url = server + "/new_ECG"
            x = requests.post(url, json=[recno.get(), hr_input, ECGtrace])
            msg = x.text
            ttk.Label(root, text=msg).grid(column=0, row=8, padx=10, pady=10)


    # save button
    save_button = ttk.Button(
        root, text="Save", command=lambda: save_patient_info()
    )
    save_button.grid(column=0, row=5, padx=10, pady=10)


    def clear_image():
        global label_m
        label_m.destroy()
        global medim
        medim = None
        ttk.Label(root, text="     new medical image wait to update    ").grid(
            column=0, row=7, padx=10, pady=10
        )
    def clear_name():
        patient_name_entry.delete(0, "end")
        global patientname
        patientname = ""
        ttk.Label(root, text="       new ECG data wait to update    ").grid(
            column=0, row=6, padx=10, pady=10
        )

    def clear_reco():
        rec_no_entry.delete(0, "end")
        global recno
        recno = None

    def clear_ecg():
        global label_e
        label_e.destroy()
        ttk.Label(root, text="       new ECG data wait to update    ").grid(
            column=0, row=8, padx=10, pady=10
        )
        global hr_input
        hr_input = None
        global ECGtrace
        ECGtrace = None
        tk.Label(root, text="The mean heart rate waiting for update").grid(
                column=5, row=2, padx=10, pady=10
            )

    ttk.Button(root, text="Clear", command=lambda: clear_name()).grid(
        column=2, row=0, padx=10, pady=10
    )
    ttk.Button(root, text="Clear", command=lambda: clear_reco()).grid(
        column=2, row=1, padx=10, pady=10
    )
    ttk.Button(root, text="Clear", command=lambda: clear_image()).grid(
        column=2, row=2, padx=10, pady=10
    )
    ttk.Button(root, text="Clear", command=lambda: clear_ecg()).grid(
        column=2, row=3, padx=10, pady=10
    )


    # close button to close the window
    close_button = ttk.Button(root, text="Close", command=root.destroy)
    close_button.grid(column=2, row=5, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_window()
