import argparse
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

EC_LEVELS = {
    "L": ERROR_CORRECT_L,  # ~7% error correction
    "M": ERROR_CORRECT_M,  # ~15% (default)
    "Q": ERROR_CORRECT_Q,  # ~25%
    "H": ERROR_CORRECT_H,  # ~30%
}

def make_qr(data: str, out: Path, box_size: int, border: int, ec_level: str, fill: str, back: str):
    qr = qrcode.QRCode(
        version=None,  # auto size
        error_correction=EC_LEVELS[ec_level],
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color=back)
    img.save(out)
    return out

def parse_args():
    p = argparse.ArgumentParser(description="Simple QR code generator.")
    p.add_argument("data", help="Text/URL to encode")
    p.add_argument("-o", "--out", default="qr.png", help="Output filename (e.g., qr.png)")
    p.add_argument("--box", type=int, default=10, help="Pixel size of each module (box)")
    p.add_argument("--border", type=int, default=4, help="Border width in modules")
    p.add_argument("--ec", choices=list(EC_LEVELS.keys()), default="M", help="Error correction level")
    p.add_argument("--fill", default="black", help="QR foreground color (e.g., black, #123456)")
    p.add_argument("--back", default="white", help="Background color")
    return p.parse_args()

def main():
    args = parse_args()
    out_path = make_qr(
        args.data,
        Path(args.out),
        args.box,
        args.border,
        args.ec,
        args.fill,
        args.back
    )
    print(f"Saved -> {out_path.resolve()}")

if __name__ == "__main__":
    main()
