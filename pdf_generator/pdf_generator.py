# Python program to create
# a pdf file


from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=24)

# create a cell
pdf.cell(200, 10, txt="G", ln=1, align='C')

pdf.set_font("Arial", size=15)
# add another cell
pdf.cell(200, 10, txt="A B C D", ln=2, align='C')

pdf.set_line_width(0.5)
pdf.set_draw_color(r=0, g=0, b=0)
pdf.line(x1=180, y1=7, x2=120, y2=120)

# save the pdf with name .pdf
pdf.output("GFG.pdf")