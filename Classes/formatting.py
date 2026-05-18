BOLD      = "\033[1m"
DIM       = "\033[2m"
ITALIC    = "\033[3m"
UNDERLINE = "\033[4m"
RESET     = "\033[0m"

RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"

def progress_bar(ratio, width=20):
    ratio = max(0.0, min(ratio, 1.0))
    filled = int(ratio * width)
    bar = "█" * filled + "░" * (width - filled)
    color = GREEN if ratio > 0.66 else YELLOW if ratio > 0.33 else RED
    return f"{color}[{bar}]{RESET} {ratio*100:.1f}%"