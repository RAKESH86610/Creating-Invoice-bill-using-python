import os
import tkinter as tk
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog

class InvoiceGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice Generator By DataFlair")
        self.root.geometry("750x800")

        self.frame = Frame(self.root, bg="white")
        self.frame.place(x=80, y=20, width=600, height=700)

        Label(self.frame, text="Enter your company details ", font=("times new roman", 30, "bold"), bg="white", fg="green", bd=0).place(x=50, y=10)

        labels = ["Company Name", "Address", "City", "GST Number", "Date", "Contact", "Customer Name", "Authorized Signatory"]
        self.entries = []
        for i, label_text in enumerate(labels):
            Label(self.frame, text=label_text, font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=80 + i * 60)
            entry = Entry(self.frame, font=("times new roman", 15), bg="light grey")
            entry.place(x=270, y=80 + i * 60, width=300, height=35)
            self.entries.append(entry)

        Button(self.frame, text="Browse Files", font=("times new roman", 14), command=self.browse).place(x=270, y=560)
        Button(self.frame, text="Submit Details", command=self.generate_invoice, font=("times new roman", 14), fg="white", cursor="hand2", bg="#B00857").place(x=50, y=640, width=180, height=40)

    def browse(self):
        self.file_name = filedialog.askopenfilename(title="Select a File")
        if self.file_name:
            Label(self.frame, text=os.path.basename(self.file_name), font=("times new roman", 15)).place(x=270, y=600)

    def generate_invoice(self):
        if not hasattr(self, 'file_name') or not self.file_name:
            print("Please select a file.")
            return

        try:
            c = canvas.Canvas("Invoice by DataFlair.pdf", pagesize=(200, 250), bottomup=0)
            c.setFillColorRGB(0.8, 0.5, 0.7)

            c.line(70, 22, 180, 22)
            c.line(5, 45, 195, 45)
            c.line(15, 120, 185, 120)
            c.line(35, 108, 35, 220)
            c.line(115, 108, 115, 220)
            c.line(135, 108, 135, 220)
            c.line(160, 108, 160, 220)
            c.line(15, 220, 185, 220)

            c.translate(10, 40)
            c.scale(1, -1)
            c.drawImage(self.file_name, 0, 0, width=50, height=30)

            c.scale(1, -1)
            c.translate(-10, -40)

            c.setFont("Times-Bold", 10)
            c.drawCentredString(125, 20, self.entries[0].get())

            c.setFont("Times-Bold", 5)
            c.drawCentredString(125, 30, self.entries[1].get())
            c.drawCentredString(125, 35, self.entries[2].get() + ", India")
            c.setFont("Times-Bold", 6)
            c.drawCentredString(125, 42, "GST No:" + self.entries[3].get())

            c.setFont("Times-Bold", 8)
            c.drawCentredString(100, 55, "INVOICE")

            c.setFont("Times-Bold", 5)

            c.drawRightString(70, 70, "Invoice No. :")
            c.drawRightString(100, 70, "XXXXXXX")

            c.drawRightString(70, 80, "Date :")
            c.drawRightString(100, 80, self.entries[4].get())

            c.drawRightString(70, 90, "Customer Name :")
            c.drawRightString(100, 90, self.entries[6].get())

            c.drawRightString(70, 100, "Phone No. :")
            c.drawRightString(100, 100, self.entries[5].get())

            c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)

            c.drawCentredString(25, 118, "S.No.")
            c.drawCentredString(75, 118, "Orders")
            c.drawCentredString(125, 118, "Price")
            c.drawCentredString(148, 118, "Qty.")
            c.drawCentredString(173, 118, "Total")

            c.drawString(30, 230, "This is system generated invoice!!")

            c.drawRightString(180, 228, self.entries[7].get())
            c.drawRightString(180, 235, "Signature")

            c.showPage()
            c.save()
            print("Invoice generated successfully.")
        except Exception as e:
            print("Error generating invoice:", e)

def main():
    root = Tk()
    obj = InvoiceGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
