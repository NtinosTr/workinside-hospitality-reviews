from django import template

register = template.Library()

DEPT_ICONS = {
    "Front Office": "🛎️",
    "Housekeeping": "🧹",
    "F&B": "🍽️",
    "Kitchen": "👨‍🍳",
    "Bar": "🍹",
    "Spa": "💆",
    "Engineer": "🛠️",
    "Security": "🛡️",
    "HR": "📋",
}

@register.filter
def dept_icon(name):
    return DEPT_ICONS.get(name, "🏨")
import hashlib

@register.filter
def pastel_color(text):
    # Generate a consistent pastel color from text
    hash_val = int(hashlib.md5(text.encode()).hexdigest(), 16)
    r = (hash_val % 128) + 100
    g = ((hash_val >> 8) % 128) + 100
    b = ((hash_val >> 16) % 128) + 100
    return f"rgb({r}, {g}, {b})"
