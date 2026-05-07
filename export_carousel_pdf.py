"""
Export AjnaLens LinkedIn Carousel directly to PDF using ReportLab.
10 square slides · 1080×1080 pt (15"×15" @72dpi)
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white, black
from reportlab.lib.units import inch
from reportlab.lib.utils import simpleSplit

# ── Constants ─────────────────────────────────────────────────────────────────
W = H = 1080   # square slide in points

BG      = HexColor("#080E1A")
CARD    = HexColor("#0F1C2E")
ORANGE  = HexColor("#FF6B1A")
ORANGE2 = HexColor("#FF8C42")
WHITE_C = HexColor("#FFFFFF")
GRAY    = HexColor("#A0ADBD")
GOLD    = HexColor("#FFD700")
GREEN   = HexColor("#44FF88")
BLUE_C  = HexColor("#44BBFF")
RED_DIM = HexColor("#1A0808")
GREEN_DIM=HexColor("#103F20")
BLUE_DIM= HexColor("#102C3F")
ORANGE_DIM=HexColor("#3F1A06")

OUT = "/home/user/Thefirstone/AjnaLens_LinkedIn_Carousel.pdf"


# ── Helpers ───────────────────────────────────────────────────────────────────

def new_page(c, bg=BG):
    c.showPage()
    c.setFillColor(bg)
    c.rect(0, 0, W, H, fill=1, stroke=0)

def rect(c, x, y, w, h, fill=CARD, stroke=None, sw=0):
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke)
        c.setLineWidth(sw)
        c.rect(x, y, w, h, fill=1, stroke=1)
    else:
        c.rect(x, y, w, h, fill=1, stroke=0)

def text(c, txt, x, y, size=18, bold=False, color=WHITE_C, align="left", max_width=None):
    c.setFillColor(color)
    font = "Helvetica-Bold" if bold else "Helvetica"
    c.setFont(font, size)
    if align == "center":
        c.drawCentredString(x, y, txt)
    elif align == "right":
        c.drawRightString(x, y, txt)
    else:
        c.drawString(x, y, txt)

def multiline(c, txt, x, y, size=16, bold=False, color=WHITE_C, leading=None, max_width=900, align="left"):
    """Draw multi-line text, returns y after last line."""
    if leading is None:
        leading = size * 1.35
    font = "Helvetica-Bold" if bold else "Helvetica"
    c.setFont(font, size)
    c.setFillColor(color)
    for line in txt.split("\n"):
        words = simpleSplit(line, font, size, max_width)
        for word_line in words:
            if align == "center":
                c.drawCentredString(x + max_width/2, y, word_line)
            else:
                c.drawString(x, y, word_line)
            y -= leading
    return y

def label(c, txt, x, y, color=ORANGE):
    text(c, txt.upper(), x, y, size=20, bold=True, color=color)

def rule(c, x, y, w=200, h=8):
    rect(c, x, y, w, h, fill=ORANGE)

def slide_num(c, n, total=10):
    text(c, f"{n} / {total}", W - 80, 35, size=18, color=GRAY, align="right")

def logo(c):
    text(c, "AjnaLens", 60, 35, size=20, bold=True, color=ORANGE)

def card(c, x, y, w, h, fill=CARD):
    rect(c, x, y, w, h, fill=fill)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDES
# ══════════════════════════════════════════════════════════════════════════════

def s01_cover(c):
    # bg stripe
    rect(c, W-200, 0, 200, H, fill=HexColor("#0B1523"))
    rect(c, 0, 0, 10, H, fill=ORANGE)

    label(c, "AjnaLens  ·  LinkedIn Lead Magnet", 60, H-60)
    multiline(c, "Your best engineer\ncan't be at\n50 sites.", 60, H-160,
              size=88, bold=True, max_width=800)
    multiline(c, "Their expertise can.", 60, H-530, size=72, bold=True,
              color=ORANGE, max_width=800)
    rule(c, 60, H-630, 320)
    multiline(c, "Swipe to see how India's top manufacturers\neliminated expert dependency — permanently.",
              60, H-660, size=28, color=GRAY, max_width=820)
    text(c, "→  Swipe", 60, H-790, size=24, bold=True, color=ORANGE2)
    logo(c); slide_num(c, 1)


def s02_problem(c):
    rect(c, 0, 0, 10, H, fill=ORANGE)
    label(c, "The Problem", 60, H-60)
    multiline(c, "The Expert\nDependency Trap", 60, H-160, size=74, bold=True, max_width=900)
    rule(c, 60, H-370, 300)

    items = [
        ("💸  1 breakdown. 1 expert. 200 km away.", "Hours of downtime. High travel cost. OEE destroyed."),
        ("🧓  Senior knowledge walks out the door.", "Every retirement takes irreplaceable expertise with it."),
        ("📉  Junior techs freeze without supervision.", "Errors, rework, and unsafe workarounds follow."),
        ("📞  Your current fix? A phone call.", "Blind troubleshooting over video — slow and unreliable."),
    ]
    y = H - 410
    for bold_line, sub in items:
        card(c, 60, y-130, 960, 130)
        multiline(c, bold_line, 80, y-30, size=22, bold=True, color=WHITE_C, max_width=920)
        multiline(c, sub, 80, y-75, size=19, color=GRAY, max_width=920)
        y -= 160
    logo(c); slide_num(c, 2)


def s03_shift(c):
    rect(c, 0, 0, 10, H, fill=ORANGE)
    label(c, "The Shift", 60, H-60)
    multiline(c, "From 'wait for the expert'\nto 'expert in their ear'",
              60, H-160, size=60, bold=True, max_width=900)
    rule(c, 60, H-370, 300)

    # BEFORE card
    card(c, 60, 80, 460, 570, fill=HexColor("#1A0808"))
    text(c, "BEFORE", 80, 620, size=20, bold=True, color=HexColor("#FF5555"))
    before = ["📞  Phone call to HQ expert",
              "⏳  Wait hours (or days)",
              "✈️  Expert flies to site",
              "🔧  Fix. Finally.",
              "💸  ₹50K+ downtime cost"]
    y = 570
    for s in before:
        text(c, s, 80, y, size=20, color=HexColor("#FFBBBB"))
        y -= 82

    # AFTER card
    card(c, 560, 80, 480, 570, fill=HexColor("#081A0E"))
    text(c, "AFTER  ·  AjnaVidya", 580, 620, size=20, bold=True, color=HexColor("#44FF88"))
    after = ["🥽  Smart glasses stream live video",
             "👁️  Remote expert sees everything",
             "✍️  Expert annotates in real-time",
             "✅  Tech resolves. Minutes.",
             "💰  Zero travel. Zero wait."]
    y = 570
    for s in after:
        text(c, s, 580, y, size=20, color=HexColor("#BBFFCC"))
        y -= 82

    text(c, "VS", W//2, 365, size=30, bold=True, color=ORANGE, align="center")
    logo(c); slide_num(c, 3)


def s04_product(c):
    rect(c, 0, 0, 10, H, fill=ORANGE)
    label(c, "The Solution", 60, H-60)
    multiline(c, "AjnaVidya\nConnected Worker", 60, H-160, size=72, bold=True, max_width=900)
    rule(c, 60, H-380, 340)
    text(c, "Three things it does — nothing else matters more:", 60, H-420, size=24, color=GRAY)

    features = [
        ("01", "Live Annotated Video Assist",
         "Expert sees exactly what the field tech sees. Draws arrows,\ncircles, highlights — in real-time. No guesswork."),
        ("02", "Hands-Free SOP Overlays",
         "Step-by-step visual instructions on actual equipment.\nTech follows the overlay. No manual, no memory required."),
        ("03", "Automatic Proof-of-Work Capture",
         "Every step logged with photo, timestamp, and signature.\nFully audit-ready. Zero paperwork."),
    ]
    y = H - 470
    for num, title, desc in features:
        card(c, 60, y-190, 960, 185)
        rect(c, 60, y-190, 130, 185, fill=ORANGE_DIM)
        text(c, num, 125, y-100, size=52, bold=True, color=ORANGE, align="center")
        rect(c, 200, y-175, 6, 160, fill=ORANGE)
        text(c, title, 220, y-50, size=24, bold=True)
        multiline(c, desc, 220, y-90, size=19, color=GRAY, max_width=780)
        y -= 215
    logo(c); slide_num(c, 4)


def s05_results(c):
    rect(c, 0, 0, 10, H, fill=ORANGE)
    label(c, "The Results", 60, H-60)
    text(c, "Numbers that matter.", 60, H-150, size=72, bold=True)
    rule(c, 60, H-265, 280)

    stats = [
        ("45%",  "Reduction in OMS downtime\n& expert dependency"),
        ("0",    "On-site expert visits needed\nfor Tier-1 troubleshooting"),
        ("3×",   "Faster first-call resolution\nvs phone-based support"),
        ("100%", "Audit-ready proof-of-work\nautomatically captured"),
    ]
    positions = [(60,360),(560,360),(60,80),(560,80)]
    for (x, y), (num, lbl) in zip(positions, stats):
        card(c, x, y, 470, 270)
        rect(c, x, y+263, 470, 7, fill=ORANGE)
        text(c, num, x+235, y+170, size=96, bold=True, color=ORANGE, align="center")
        multiline(c, lbl, x+10, y+100, size=20, color=GRAY, max_width=450, align="center")
    logo(c); slide_num(c, 5)


def s06_clients(c):
    rect(c, 0, 0, 10, H, fill=ORANGE)
    label(c, "Live Deployments", 60, H-60)
    multiline(c, "India's best trust AjnaLens.", 60, H-160, size=64, bold=True, max_width=960)
    rule(c, 60, H-330, 300)

    clients = [
        ("🚗 Tata Motors",    "Remote Assistance + Guided Assembly\nTruck Plant, Pimpri · 3 live POCs"),
        ("⚡ Suzlon Energy",   "AI Smart Glasses for wind OMS technicians\n45% downtime reduction — proven"),
        ("🔩 SKF Engineering","Remote Assistance SaaS · Bangalore plant\n6-month pilot · Live"),
        ("🔧 Hyundai India",  "CAVE VR — hand & head tracking\nAdvanced assembly simulation"),
        ("💡 UnoMinda",       "Remote Assistance + AR Headsets pilot\nHaryana plant · In deployment"),
        ("🏛 1,500+ ITIs",    "AjnaXR Simulators — welding, painting\nLargest XR skilling deployment in India"),
    ]
    positions = [(60,530),(560,530),(60,310),(560,310),(60,90),(560,90)]
    for (x,y), (name, detail) in zip(positions, clients):
        card(c, x, y, 470, 200)
        text(c, name, x+16, y+162, size=22, bold=True)
        multiline(c, detail, x+16, y+120, size=18, color=GRAY, max_width=435)
    logo(c); slide_num(c, 6)


def s07_hardware(c):
    rect(c, 0, 0, 10, H, fill=ORANGE)
    label(c, "The Hardware", 60, H-60)
    multiline(c, "AjnaX AI Smart Glasses", 60, H-160, size=68, bold=True, max_width=920)
    rule(c, 60, H-340, 340)
    text(c, '"Light as your spectacles. Powerful as your best engineer."',
         60, H-385, size=24, color=ORANGE2)

    specs = [
        ("🧠 AI Mentor on-device",     "Trained on your SOPs. Ask in Hindi, English, or Marathi. Get live guidance."),
        ("📷 Camera + Computer Vision","Identifies equipment and fault patterns without manual lookup."),
        ("📡 Bandwidth-friendly",       "Works on 4G / spotty networks at remote field sites."),
        ("🔊 Voice-first interface",    "Hands stay on the equipment. Voice logs, queries, confirmations."),
        ("⚡ Edge AI processing",        "Core SOP guidance runs on-device. No cloud dependency."),
    ]
    y = H - 440
    for title, desc in specs:
        card(c, 60, y-125, 960, 118)
        text(c, title, 80, y-38, size=22, bold=True)
        text(c, desc, 80, y-82, size=19, color=GRAY)
        y -= 145
    logo(c); slide_num(c, 7)


def s08_stack(c):
    rect(c, 0, 0, 10, H, fill=ORANGE)
    label(c, "The Full Stack", 60, H-60)
    multiline(c, "Remote Assistance\nis just the start.", 60, H-160, size=68, bold=True, max_width=920)
    rule(c, 60, H-380, 300)
    text(c, "AjnaLens covers the full industrial lifecycle:", 60, H-420, size=24, color=GRAY)

    phases = [
        ("TRAIN",    ORANGE,     ORANGE_DIM,  "VR Safety Simulations  ·  VR Skill & SOP Training  ·  1,500+ simulators live"),
        ("EXECUTE",  BLUE_C,     BLUE_DIM,    "AR Remote Assistance  ·  Guided Assembly  ·  AR Inspection & VLO"),
        ("OPTIMIZE", GREEN,      GREEN_DIM,   "OMS / CXO Dashboard  ·  Agentic AI Layer  ·  Real-time analytics"),
    ]
    y = H - 470
    for phase, color, dim, items in phases:
        card(c, 60, y-185, 960, 178)
        rect(c, 60, y-185, 155, 178, fill=dim)
        text(c, phase, 137, y-100, size=22, bold=True, color=color, align="center")
        rect(c, 222, y-172, 6, 158, fill=color)
        text(c, items, 240, y-90, size=20, color=WHITE_C)
        y -= 210
    logo(c); slide_num(c, 8)


def s09_credibility(c):
    rect(c, 0, 0, 10, H, fill=ORANGE)
    label(c, "Why AjnaLens", 60, H-60)
    multiline(c, "Built at IIT Bombay.\nTrusted by India.", 60, H-160, size=68, bold=True, max_width=920)
    rule(c, 60, H-380, 300)

    creds = [
        ("🎓 IIT Bombay, 2014",      "India's sovereign XR + AI stack · Deep-tech origin"),
        ("📜 40+ Patents",            "Across XR, AI, and spatial computing"),
        ("👥 5 Lakh+ Learners",       "Upskilled across industrial & vocational programmes"),
        ("🏭 1,500+ Simulators",      "9 Indian states · Largest XR skilling deployment"),
        ("🏆 CES 2023 Innovation",    "AWE Auggie Award · iDEX Ministry of Defence"),
        ("💰 Lenskart & Paytm backed","Maharashtra Defence & Aerospace Venture Fund"),
    ]
    positions = [(60,530),(560,530),(60,310),(560,310),(60,90),(560,90)]
    for (x,y), (title, sub) in zip(positions, creds):
        card(c, x, y, 470, 200)
        text(c, title, x+16, y+162, size=22, bold=True)
        multiline(c, sub, x+16, y+115, size=19, color=GRAY, max_width=435)
    logo(c); slide_num(c, 9)


def s10_cta(c):
    rect(c, 0, H-16, W, 16, fill=ORANGE)
    card(c, 50, 80, W-100, H-120)

    label(c, "Next Step", 90, H-110, color=ORANGE2)
    multiline(c, "Want to see this\nat your plant?", 90, H-200, size=80, bold=True, max_width=900)
    rule(c, 90, H-510, 440)
    multiline(c,
              "Book a 20-minute live demo.\n"
              "We'll show you Remote Assistance running on actual\n"
              "smart glasses — your SOPs, your equipment, your team.",
              90, H-545, size=26, color=GRAY, max_width=900)

    # contact block
    rect(c, 90, 140, W-180, 170, fill=HexColor("#15283F"))
    text(c, "📧  prashantpandey@ajnalens.com", 115, 272, size=26, bold=True)
    text(c, "📱  +91 70219 08581   ·   🌐  www.ajnalens.com", 115, 216, size=22, color=GRAY)

    text(c, "Prashant Pandey  ·  Lead Enterprise, B2G & B2D  ·  AjnaLens",
         W//2, 90, size=18, color=GRAY, align="center")
    slide_num(c, 10)


# ══════════════════════════════════════════════════════════════════════════════

def main():
    c = canvas.Canvas(OUT, pagesize=(W, H))
    c.setTitle("AjnaLens – LinkedIn Lead Magnet Carousel")

    # Page 1 needs special handling (first page)
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    s01_cover(c)

    new_page(c); s02_problem(c)
    new_page(c); s03_shift(c)
    new_page(c); s04_product(c)
    new_page(c); s05_results(c)
    new_page(c); s06_clients(c)
    new_page(c); s07_hardware(c)
    new_page(c); s08_stack(c)
    new_page(c); s09_credibility(c)
    new_page(c); s10_cta(c)

    c.save()
    print(f"✅  PDF saved → {OUT}")
    print(f"   10 slides · 1080×1080 pt square · Ready for LinkedIn upload")


if __name__ == "__main__":
    main()
