import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

points = []
img = None
clone = None
window_name = "Click to Select Points"

orig_w = None
orig_h = None
target_w = None
target_h = None


def ask_target_size():
    """يسمح للمستخدم بإدخال المقاس الجديد فقط"""
    global target_w, target_h

    win = tk.Toplevel()
    win.title("Enter Target Size")

    tk.Label(win, text="Enter target size (e.g., 700 700):", font=("Arial", 12)).pack()

    entry = tk.Entry(win, font=("Arial", 14))
    entry.pack()

    def set_size():
        global target_w, target_h
        
        try:
            tw, th = map(int, entry.get().split())
            target_w, target_h = tw, th
            print(f"\n[+] Target size set to: {target_w} x {target_h}")
            win.destroy()
        except:
            print("❌ Invalid input. Example: 700 700")

    tk.Button(win, text="OK", command=set_size).pack(pady=10)


def select_image():
    """تحميل الصورة وقراءة حجمها تلقائيًا"""
    global img, clone, points, orig_w, orig_h

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if not file_path:
        return

    img = cv2.imread(file_path)
    clone = img.copy()
    points = []

    # قراءة الحجم الأصلي تلقائيًا
    orig_h, orig_w = img.shape[:2]
    print(f"\n[+] Original Image Size Detected: {orig_w} x {orig_h}")

    cv2.imshow(window_name, img)
    cv2.setMouseCallback(window_name, click_event)


def click_event(event, x, y, flags, param):
    """التقاط نقطتين من الصورة"""
    global points, img, clone, orig_w, orig_h, target_w, target_h

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"[+] Point {len(points)}: ({x}, {y})")

        cv2.circle(img, (x, y), 4, (0, 0, 255), -1)
        cv2.imshow(window_name, img)

        if len(points) == 2:
            (x1, y1), (x2, y2) = points
            width = x2 - x1
            height = y2 - y1

            print("\n=== ORIGINAL RECT ===")
            print(f"pygame.Rect({x1}, {y1}, {width}, {height})")

            if target_w and target_h:
                scale_x = target_w / orig_w
                scale_y = target_h / orig_h

                new_x = round(x1 * scale_x)
                new_y = round(y1 * scale_y)
                new_w = round(width * scale_x)
                new_h = round(height * scale_y)

                print("\n=== SCALED RECT ===")
                print(f"pygame.Rect({new_x}, {new_y}, {new_w}, {new_h})")

            print("======================\n")

            points = []
            img = clone.copy()
            cv2.imshow(window_name, img)


# GUI
root = tk.Tk()
root.title("Coordinate Extractor Tool")

tk.Button(root, text="Upload Image", command=select_image, font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Set Target Size", command=ask_target_size, font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Upload image → Enter target size → Click two points", font=("Arial", 12)).pack()

root.mainloop()
