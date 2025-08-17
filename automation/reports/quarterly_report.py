from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def build_quarterly_pdf(path: str, title: str = "AutoInfra Capital - Quarterly Report"):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, title)
    c.setFont("Helvetica", 11)
    lines = [
        "KPI Highlights (demo):",
        "- Gross IRR: 18.3%",
        "- Deployed Capital: R325,000,000",
        "- ESG Score (avg): 71.2",
        "- Carbon Credits Issued (est): 42,100"
    ]
    y = height - 90
    for ln in lines:
        c.drawString(50, y, ln); y -= 18
    c.showPage()
    c.save()

if __name__ == "__main__":
    build_quarterly_pdf("quarterly_report_demo.pdf")
