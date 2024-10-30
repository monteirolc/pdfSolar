from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
# My files
from utils import convert, percent


def routine():
    c = canvas.Canvas("filename.pdf", pagesize=A4)
    # Draw principal image of the project
    c.drawImage(
        x=0,
        y=0,
        image="./base/images/Principal.png",
        height=A4[1],
        width=A4[0])
    # Add new page in model
    c.showPage()
    # Draw the project image of commercial proposal
    c.drawImage(
        x=percent(A4[0], 15),
        y=percent(A4[1], 50),
        image="./base/images/Original_Logo.png",
        height=convert(A4[1], 106.11),
        width=convert(A4[0], 200)
    )
    # Print text of commercial proposal
    c.setFillColorRGB(50, 125, 211)
    c.setFont("Times-Roman", 70)
    c.drawString(x=percent(A4[0], 26), y=percent(A4[1], 30),
                 text="PROPOSTA")
    c.drawString(x=percent(A4[0], 22), y=percent(A4[1], 23),
                 text="COMERCIAL")

    c.setFont("Times-Roman", 30)
    c.drawString(x=percent(A4[0], 50), y=percent(A4[1], 15),
                 text="002-24")

    # Add new page in model
    c.showPage()
    c.setFont("Times-Roman", 25)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(x=percent(A4[0], 50), y=percent(A4[1], 15),
                 text="Dados cadastrais")
    c.save()


if __name__ == "__main__":
    routine()
