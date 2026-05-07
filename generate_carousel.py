"""
AjnaLens LinkedIn Lead Magnet Carousel Generator
10 slides · Square (10"×10") · Dark tech theme
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# ── Brand colours ──────────────────────────────────────────────────────────────
BG_DARK    = RGBColor(0x08, 0x0E, 0x1A)   # #080E1A  deep navy
BG_CARD    = RGBColor(0x0F, 0x1C, 0x2E)   # #0F1C2E  card navy
ORANGE     = RGBColor(0xFF, 0x6B, 0x1A)   # #FF6B1A  AjnaLens orange
ORANGE_MUT = RGBColor(0xFF, 0x8C, 0x42)   # lighter orange for accents
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
GRAY       = RGBColor(0xA0, 0xAD, 0xBD)   # #A0ADBD  muted text
GOLD       = RGBColor(0xFF, 0xD7, 0x00)   # stat highlight

SLIDE_W = Inches(10)
SLIDE_H = Inches(10)


def new_prs():
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs


def blank_slide(prs):
    layout = prs.slide_layouts[6]   # completely blank
    slide  = prs.slides.add_slide(layout)
    return slide


def fill_bg(slide, color: RGBColor):
    bg   = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_rect(slide, left, top, width, height, fill_color=None, line_color=None, line_width=Pt(0)):
    shape = slide.shapes.add_shape(
        1,   # MSO_SHAPE_TYPE.RECTANGLE
        left, top, width, height
    )
    shape.line.width = line_width
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    if line_color:
        shape.line.color.rgb = line_color
    else:
        shape.line.fill.background()
    return shape


def add_text(slide, text, left, top, width, height,
             font_size=Pt(18), bold=False, color=WHITE,
             align=PP_ALIGN.LEFT, wrap=True):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf    = txBox.text_frame
    tf.word_wrap = wrap
    p  = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size  = font_size
    run.font.bold  = bold
    run.font.color.rgb = color
    run.font.name  = "Calibri"
    return txBox


def add_label(slide, text, left, top, width=Inches(4), color=ORANGE):
    """Small ALL-CAPS category label."""
    add_text(slide, text.upper(), left, top, width, Inches(0.35),
             font_size=Pt(11), bold=True, color=color, align=PP_ALIGN.LEFT)


def orange_rule(slide, left, top, width=Inches(1), height=Inches(0.055)):
    """Thin horizontal orange accent rule."""
    add_rect(slide, left, top, width, height, fill_color=ORANGE)


def slide_number(slide, n, total=10):
    add_text(slide, f"{n} / {total}",
             Inches(8.5), Inches(9.55), Inches(1.4), Inches(0.4),
             font_size=Pt(10), color=GRAY, align=PP_ALIGN.RIGHT)


def logo_tag(slide):
    """Bottom-left AjnaLens wordmark."""
    add_text(slide, "AjnaLens",
             Inches(0.35), Inches(9.55), Inches(2.5), Inches(0.4),
             font_size=Pt(11), bold=True, color=ORANGE, align=PP_ALIGN.LEFT)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE BUILDERS
# ══════════════════════════════════════════════════════════════════════════════

def slide_01_cover(prs):
    """Hook: The expert dependency problem."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)

    # large diagonal accent block top-right
    add_rect(s, Inches(6.5), Inches(0), Inches(3.5), Inches(4),
             fill_color=RGBColor(0x0F, 0x1C, 0x2E))
    add_rect(s, Inches(8.2), Inches(0), Inches(1.8), Inches(10),
             fill_color=RGBColor(0x0B, 0x15, 0x23))

    # orange accent stripe
    add_rect(s, Inches(0), Inches(0), Inches(0.07), Inches(10),
             fill_color=ORANGE)

    # label
    add_label(s, "Lead Magnet · AjnaLens", Inches(0.35), Inches(0.45))

    # headline
    add_text(s,
             "Your best engineer\ncan't be at\n50 sites.",
             Inches(0.35), Inches(1.2), Inches(7.8), Inches(3.8),
             font_size=Pt(52), bold=True, color=WHITE)

    # sub-headline
    add_text(s,
             "Their expertise can.",
             Inches(0.35), Inches(4.85), Inches(7.8), Inches(1.0),
             font_size=Pt(42), bold=True, color=ORANGE)

    orange_rule(s, Inches(0.35), Inches(6.1), Inches(2.2))

    add_text(s,
             "Swipe to see how India's top manufacturers\neliminated expert dependency — permanently.",
             Inches(0.35), Inches(6.3), Inches(7.5), Inches(1.4),
             font_size=Pt(17), color=GRAY)

    # swipe CTA
    add_text(s, "→  Swipe",
             Inches(0.35), Inches(7.9), Inches(3), Inches(0.5),
             font_size=Pt(14), bold=True, color=ORANGE_MUT)

    logo_tag(s)
    slide_number(s, 1)


def slide_02_problem(prs):
    """The Expert Dependency Trap."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(0.07), Inches(10), fill_color=ORANGE)

    add_label(s, "The Problem", Inches(0.35), Inches(0.45))
    add_text(s, "The Expert\nDependency Trap",
             Inches(0.35), Inches(0.95), Inches(9), Inches(1.8),
             font_size=Pt(44), bold=True, color=WHITE)
    orange_rule(s, Inches(0.35), Inches(2.75), Inches(2.0))

    pain_points = [
        ("💸", "1 breakdown. 1 expert. 200 km away.",         "Hours of downtime. High travel cost. OEE destroyed."),
        ("🧓", "Senior knowledge walks out the door.",         "Every retirement takes irreplaceable expertise with it."),
        ("📉", "Junior techs freeze without supervision.",     "Errors, rework, and unsafe workarounds follow."),
        ("📞", "Your current fix? A phone call.",              "Blind troubleshooting over video — slow and unreliable."),
    ]

    for i, (icon, bold_line, sub) in enumerate(pain_points):
        top = Inches(3.0 + i * 1.55)
        add_rect(s, Inches(0.35), top, Inches(9.3), Inches(1.3),
                 fill_color=BG_CARD)
        add_text(s, icon + "  " + bold_line,
                 Inches(0.55), top + Inches(0.1), Inches(8.9), Inches(0.55),
                 font_size=Pt(14), bold=True, color=WHITE)
        add_text(s, sub,
                 Inches(0.55), top + Inches(0.6), Inches(8.9), Inches(0.55),
                 font_size=Pt(12), color=GRAY)

    logo_tag(s)
    slide_number(s, 2)


def slide_03_shift(prs):
    """Before vs After — the shift."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(0.07), Inches(10), fill_color=ORANGE)

    add_label(s, "The Shift", Inches(0.35), Inches(0.45))
    add_text(s, "From 'wait for the expert'\nto 'expert in their ear'",
             Inches(0.35), Inches(0.95), Inches(9.3), Inches(1.8),
             font_size=Pt(38), bold=True, color=WHITE)
    orange_rule(s, Inches(0.35), Inches(2.75), Inches(2.0))

    # BEFORE card
    add_rect(s, Inches(0.35), Inches(3.0), Inches(4.3), Inches(5.6),
             fill_color=RGBColor(0x1A, 0x08, 0x08))
    add_text(s, "BEFORE",
             Inches(0.55), Inches(3.15), Inches(3.8), Inches(0.45),
             font_size=Pt(12), bold=True, color=RGBColor(0xFF, 0x55, 0x55))
    before_steps = ["📞  Phone call to HQ expert",
                    "⏳  Wait hours (or days)",
                    "✈️  Expert flies to site",
                    "🔧  Fix. Finally.",
                    "💸  ₹50K+ travel + downtime cost"]
    for i, step in enumerate(before_steps):
        add_text(s, step,
                 Inches(0.55), Inches(3.75 + i * 0.88), Inches(3.9), Inches(0.7),
                 font_size=Pt(13), color=RGBColor(0xFF, 0xBB, 0xBB))

    # AFTER card
    add_rect(s, Inches(5.05), Inches(3.0), Inches(4.6), Inches(5.6),
             fill_color=RGBColor(0x08, 0x1A, 0x0E))
    add_text(s, "AFTER  ·  AjnaVidya",
             Inches(5.25), Inches(3.15), Inches(4.1), Inches(0.45),
             font_size=Pt(12), bold=True, color=RGBColor(0x44, 0xFF, 0x88))
    after_steps = ["🥽  Smart glasses stream live video",
                   "👁️  Remote expert sees everything",
                   "✍️  Expert annotates in real-time",
                   "✅  Tech resolves on-site. Minutes.",
                   "💰  Zero travel. Zero waiting."]
    for i, step in enumerate(after_steps):
        add_text(s, step,
                 Inches(5.25), Inches(3.75 + i * 0.88), Inches(4.1), Inches(0.7),
                 font_size=Pt(13), color=RGBColor(0xBB, 0xFF, 0xCC))

    # vs divider
    add_text(s, "VS",
             Inches(4.35), Inches(5.55), Inches(0.7), Inches(0.7),
             font_size=Pt(18), bold=True, color=ORANGE, align=PP_ALIGN.CENTER)

    logo_tag(s)
    slide_number(s, 3)


def slide_04_product(prs):
    """AjnaVidya Connected Worker — how it works."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(0.07), Inches(10), fill_color=ORANGE)

    add_label(s, "The Solution", Inches(0.35), Inches(0.45))
    add_text(s, "AjnaVidya\nConnected Worker",
             Inches(0.35), Inches(0.95), Inches(9.3), Inches(1.8),
             font_size=Pt(42), bold=True, color=WHITE)
    orange_rule(s, Inches(0.35), Inches(2.75), Inches(2.2))

    add_text(s, "Three things it does — nothing else matters more:",
             Inches(0.35), Inches(2.95), Inches(9.3), Inches(0.6),
             font_size=Pt(15), color=GRAY)

    features = [
        ("01", "Live Annotated Video Assist",
         "Expert sees exactly what the field tech sees. Draws arrows, circles, highlights — in real-time. No guesswork."),
        ("02", "Hands-Free SOP Overlays",
         "Step-by-step visual work instructions on the actual equipment. Tech follows the overlay. No manual, no memory required."),
        ("03", "Automatic Proof-of-Work Capture",
         "Every step logged with photo, timestamp, and signature. Fully audit-ready. No paperwork."),
    ]

    for i, (num, title, desc) in enumerate(features):
        top = Inches(3.7 + i * 2.0)
        add_rect(s, Inches(0.35), top, Inches(9.3), Inches(1.75),
                 fill_color=BG_CARD)
        add_text(s, num,
                 Inches(0.5), top + Inches(0.15), Inches(0.7), Inches(1.2),
                 font_size=Pt(28), bold=True, color=ORANGE, align=PP_ALIGN.CENTER)
        add_rect(s, Inches(1.35), top + Inches(0.25), Inches(0.05), Inches(1.2),
                 fill_color=ORANGE)
        add_text(s, title,
                 Inches(1.55), top + Inches(0.12), Inches(7.9), Inches(0.55),
                 font_size=Pt(16), bold=True, color=WHITE)
        add_text(s, desc,
                 Inches(1.55), top + Inches(0.65), Inches(7.9), Inches(0.95),
                 font_size=Pt(12.5), color=GRAY)

    logo_tag(s)
    slide_number(s, 4)


def slide_05_hardware(prs):
    """AjnaX Smart Glasses — the hardware."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(0.07), Inches(10), fill_color=ORANGE)

    add_label(s, "The Hardware", Inches(0.35), Inches(0.45))
    add_text(s, "AjnaX AI Smart Glasses",
             Inches(0.35), Inches(0.95), Inches(9.3), Inches(1.2),
             font_size=Pt(44), bold=True, color=WHITE)
    orange_rule(s, Inches(0.35), Inches(2.1), Inches(2.2))

    add_text(s, '"Light as your spectacles. Powerful as your best engineer."',
             Inches(0.35), Inches(2.3), Inches(9.3), Inches(0.7),
             font_size=Pt(16), color=ORANGE_MUT)

    specs = [
        ("🧠", "AI Mentor on-device",       "Trained on your SOPs. Ask in Hindi, English, or Marathi. Get step-by-step answers live."),
        ("📷", "Camera + Computer Vision",  "Identifies equipment, model numbers, and fault patterns without manual lookup."),
        ("📡", "Bandwidth-friendly",         "Works on low-connectivity field sites. Optimised for 4G / spotty networks."),
        ("🔊", "Voice-first interface",      "Hands stay on the equipment. Voice logs, voice queries, voice confirmations."),
        ("⚡", "Edge AI processing",          "Computation on-device. No cloud dependency for core SOP guidance."),
    ]

    for i, (icon, title, desc) in enumerate(specs):
        top = Inches(3.2 + i * 1.28)
        add_rect(s, Inches(0.35), top, Inches(9.3), Inches(1.12),
                 fill_color=BG_CARD)
        add_text(s, icon + "  " + title,
                 Inches(0.55), top + Inches(0.08), Inches(9.0), Inches(0.45),
                 font_size=Pt(14), bold=True, color=WHITE)
        add_text(s, desc,
                 Inches(0.55), top + Inches(0.55), Inches(9.0), Inches(0.5),
                 font_size=Pt(12), color=GRAY)

    logo_tag(s)
    slide_number(s, 5)


def slide_06_results(prs):
    """Numbers that matter — ROI stats."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(0.07), Inches(10), fill_color=ORANGE)

    add_label(s, "The Results", Inches(0.35), Inches(0.45))
    add_text(s, "Numbers that matter.",
             Inches(0.35), Inches(0.95), Inches(9.3), Inches(1.0),
             font_size=Pt(46), bold=True, color=WHITE)
    orange_rule(s, Inches(0.35), Inches(1.9), Inches(1.8))

    stats = [
        ("45%",  "Reduction in OMS downtime\n& expert dependency"),
        ("0",    "On-site expert visits needed\nfor Tier-1 troubleshooting"),
        ("3×",   "Faster first-call resolution\nvs phone-based support"),
        ("100%", "Audit-ready proof-of-work\nautomatically captured"),
    ]

    for i, (num, label) in enumerate(stats):
        col = i % 2
        row = i // 2
        left = Inches(0.35 + col * 4.85)
        top  = Inches(2.5 + row * 3.4)
        add_rect(s, left, top, Inches(4.55), Inches(3.0),
                 fill_color=BG_CARD)
        add_rect(s, left, top, Inches(4.55), Inches(0.07),
                 fill_color=ORANGE)
        add_text(s, num,
                 left + Inches(0.2), top + Inches(0.3), Inches(4.1), Inches(1.5),
                 font_size=Pt(64), bold=True, color=ORANGE, align=PP_ALIGN.CENTER)
        add_text(s, label,
                 left + Inches(0.15), top + Inches(1.85), Inches(4.2), Inches(1.0),
                 font_size=Pt(13), color=GRAY, align=PP_ALIGN.CENTER)

    logo_tag(s)
    slide_number(s, 6)


def slide_07_clients(prs):
    """Who's already using this."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(0.07), Inches(10), fill_color=ORANGE)

    add_label(s, "Live Deployments", Inches(0.35), Inches(0.45))
    add_text(s, "India's best trust\nAjnaLens.",
             Inches(0.35), Inches(0.95), Inches(9.3), Inches(1.8),
             font_size=Pt(46), bold=True, color=WHITE)
    orange_rule(s, Inches(0.35), Inches(2.75), Inches(2.0))

    clients = [
        ("🚗", "Tata Motors",          "Remote Assistance + Guided Assembly\nTruck Plant, Pimpri · 3 live POCs"),
        ("⚡", "Suzlon Energy",         "AI Smart Glasses for wind O&M technicians\nProven 45% downtime reduction"),
        ("🔩", "SKF Engineering",       "Remote Assistance SaaS (6-month pilot)\nBangalore plant · Live"),
        ("🔧", "Hyundai Motor India",  "CAVE VR setup — hand & head tracking\nAdvanced assembly simulation"),
        ("💡", "UnoMinda",             "Remote Assistance + AR Headsets pilot\nHaryana plant · In deployment"),
        ("🏛", "1,500+ ITIs / 9 States", "AjnaXR Station Simulators — welding, painting\nLargest XR skilling deployment in India"),
    ]

    for i, (icon, name, detail) in enumerate(clients):
        col = i % 2
        row = i // 2
        left = Inches(0.35 + col * 4.85)
        top  = Inches(3.1 + row * 2.15)
        add_rect(s, left, top, Inches(4.55), Inches(1.9),
                 fill_color=BG_CARD)
        add_text(s, icon + "  " + name,
                 left + Inches(0.15), top + Inches(0.1), Inches(4.2), Inches(0.55),
                 font_size=Pt(14), bold=True, color=WHITE)
        add_text(s, detail,
                 left + Inches(0.15), top + Inches(0.65), Inches(4.2), Inches(1.1),
                 font_size=Pt(11.5), color=GRAY)

    logo_tag(s)
    slide_number(s, 7)


def slide_08_stack(prs):
    """The full AjnaLens stack."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(0.07), Inches(10), fill_color=ORANGE)

    add_label(s, "The Full Stack", Inches(0.35), Inches(0.45))
    add_text(s, "Remote Assistance\nis just the start.",
             Inches(0.35), Inches(0.95), Inches(9.3), Inches(1.8),
             font_size=Pt(42), bold=True, color=WHITE)
    orange_rule(s, Inches(0.35), Inches(2.75), Inches(2.0))

    add_text(s, "AjnaLens covers the full industrial lifecycle:",
             Inches(0.35), Inches(2.95), Inches(9.3), Inches(0.55),
             font_size=Pt(15), color=GRAY)

    phases = [
        ("TRAIN",    ORANGE,                        RGBColor(0x3F, 0x1A, 0x06), ["VR Safety Simulations", "VR Skill & SOP Training", "1,500+ simulators live"]),
        ("EXECUTE",  RGBColor(0x44, 0xBB, 0xFF),   RGBColor(0x10, 0x2C, 0x3F), ["AR Remote Assistance", "Guided Assembly", "AR Inspection & VLO"]),
        ("OPTIMIZE", RGBColor(0x44, 0xFF, 0x88),   RGBColor(0x10, 0x3F, 0x20), ["OMS / CXO Dashboard", "Agentic AI Layer", "Real-time analytics"]),
    ]

    for i, (phase, color, dim_color, items) in enumerate(phases):
        top = Inches(3.7 + i * 2.0)
        add_rect(s, Inches(0.35), top, Inches(9.3), Inches(1.8),
                 fill_color=BG_CARD)
        add_rect(s, Inches(0.35), top, Inches(1.5), Inches(1.8),
                 fill_color=dim_color)
        add_text(s, phase,
                 Inches(0.38), top + Inches(0.6), Inches(1.4), Inches(0.6),
                 font_size=Pt(13), bold=True, color=color, align=PP_ALIGN.CENTER)
        bullet_text = "  ·  ".join(items)
        add_text(s, bullet_text,
                 Inches(2.0), top + Inches(0.6), Inches(7.5), Inches(0.6),
                 font_size=Pt(13), color=WHITE)

    logo_tag(s)
    slide_number(s, 8)


def slide_09_credibility(prs):
    """Why AjnaLens? Credibility slide."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)
    add_rect(s, Inches(0), Inches(0), Inches(0.07), Inches(10), fill_color=ORANGE)

    add_label(s, "Why AjnaLens", Inches(0.35), Inches(0.45))
    add_text(s, "Built at IIT Bombay.\nTrusted by India.",
             Inches(0.35), Inches(0.95), Inches(9.3), Inches(1.8),
             font_size=Pt(44), bold=True, color=WHITE)
    orange_rule(s, Inches(0.35), Inches(2.75), Inches(2.0))

    creds = [
        ("🎓", "IIT Bombay Deep-Tech Origin",    "Founded 2014 · India's sovereign XR + AI stack"),
        ("📜", "40+ Patents Filed",              "Across XR, AI, and spatial computing"),
        ("👥", "5 Lakh+ Learners Upskilled",     "Across industrial and vocational programmes"),
        ("🏭", "1,500+ Simulators Live",          "9 Indian states · largest XR skilling deployment"),
        ("🏆", "CES 2023 Innovation Award",       "AWE Auggie Award · iDEX Ministry of Defence"),
        ("💰", "Backed by Lenskart & Paytm",     "Founders + Maharashtra Defence & Aerospace VC Fund"),
    ]

    for i, (icon, title, sub) in enumerate(creds):
        col = i % 2
        row = i // 2
        left = Inches(0.35 + col * 4.85)
        top  = Inches(3.1 + row * 2.15)
        add_rect(s, left, top, Inches(4.55), Inches(1.9),
                 fill_color=BG_CARD)
        add_text(s, icon + "  " + title,
                 left + Inches(0.15), top + Inches(0.1), Inches(4.2), Inches(0.55),
                 font_size=Pt(13), bold=True, color=WHITE)
        add_text(s, sub,
                 left + Inches(0.15), top + Inches(0.65), Inches(4.2), Inches(1.1),
                 font_size=Pt(12), color=GRAY)

    logo_tag(s)
    slide_number(s, 9)


def slide_10_cta(prs):
    """CTA — Book a demo."""
    s = blank_slide(prs)
    fill_bg(s, BG_DARK)

    # Full-width orange top bar
    add_rect(s, Inches(0), Inches(0), Inches(10), Inches(0.12), fill_color=ORANGE)

    # Large background card
    add_rect(s, Inches(0.35), Inches(0.8), Inches(9.3), Inches(7.5),
             fill_color=BG_CARD)

    add_label(s, "Next Step", Inches(0.7), Inches(1.15), color=ORANGE_MUT)

    add_text(s, "Want to see this\nat your plant?",
             Inches(0.7), Inches(1.65), Inches(8.6), Inches(2.4),
             font_size=Pt(46), bold=True, color=WHITE)

    orange_rule(s, Inches(0.7), Inches(4.0), Inches(3.0))

    add_text(s,
             "Book a 20-minute live demo.\n"
             "We'll show you Remote Assistance running on actual\n"
             "smart glasses — your SOPs, your equipment, your team.",
             Inches(0.7), Inches(4.2), Inches(8.6), Inches(1.8),
             font_size=Pt(16), color=GRAY)

    # Contact block
    add_rect(s, Inches(0.7), Inches(6.1), Inches(8.6), Inches(1.6),
             fill_color=RGBColor(0x15, 0x28, 0x3F))

    add_text(s, "📧  prashantpandey@ajnalens.com",
             Inches(0.95), Inches(6.25), Inches(8.0), Inches(0.55),
             font_size=Pt(15), bold=True, color=WHITE)
    add_text(s, "📱  +91 70219 08581   ·   🌐  www.ajnalens.com",
             Inches(0.95), Inches(6.8), Inches(8.0), Inches(0.55),
             font_size=Pt(13), color=GRAY)

    add_text(s, "Prashant Pandey  ·  Lead Enterprise, B2G & B2D  ·  AjnaLens",
             Inches(0.35), Inches(9.55), Inches(9.3), Inches(0.4),
             font_size=Pt(10), color=GRAY, align=PP_ALIGN.CENTER)

    slide_number(s, 10)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    prs = new_prs()

    slide_01_cover(prs)
    slide_02_problem(prs)
    slide_03_shift(prs)
    slide_04_product(prs)
    slide_05_hardware(prs)
    slide_06_results(prs)
    slide_07_clients(prs)
    slide_08_stack(prs)
    slide_09_credibility(prs)
    slide_10_cta(prs)

    out = "/home/user/Thefirstone/AjnaLens_LinkedIn_Carousel.pptx"
    prs.save(out)
    print(f"✅  Saved → {out}")
    print(f"   10 slides · Square 10\"×10\" · Upload as PDF to LinkedIn")
    print()
    print("To convert to PDF (Linux):")
    print("  libreoffice --headless --convert-to pdf AjnaLens_LinkedIn_Carousel.pptx")


if __name__ == "__main__":
    main()
