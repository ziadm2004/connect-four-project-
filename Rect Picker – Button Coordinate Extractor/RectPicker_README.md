# 🎯 Rect Picker – Button Coordinate Extractor

A simple and powerful tool for extracting **button coordinates** from images.  
Designed for game developers and GUI designers who need precise **pygame.Rect()**  
positions for buttons, UI elements, or clickable regions.

---

## ⭐ Features
- Select any image (PNG, JPG, JPEG, BMP)
- Click two points to automatically generate:
  - Original pygame.Rect(x, y, width, height)
  - Scaled Rect for any target resolution
- Automatic detection of the image’s original size
- Easy GUI built with Tkinter
- Live preview of clicked points
- Instant console output of rectangle data

---

## 📌 What This Tool Solves
Manually guessing button coordinates for a GUI is inaccurate and time-consuming.

This tool allows you to:
- Click the **top-left** and **bottom-right** corners of any UI button
- Automatically generate its exact pygame.Rect()
- Scale coordinates automatically to **any resolution** (e.g., 1024×1024 → 700×700)

Perfect for:
- Pygame interfaces  
- Menu screens  
- Game buttons  
- Mobile UI mapping  
- Connect 4 / Chess / Tic-Tac-Toe projects  
- Any project requiring pixel-accurate rectangles  

---

## 🖼 How It Works
1. Click **Upload Image**
2. Select the UI image you want to measure
3. Click **Set Target Size** if you want scaling (optional)
4. Click two points on the image:
   - First click → top-left corner  
   - Second click → bottom-right corner  
5. The tool prints:
   - Original pygame.Rect
   - Scaled pygame.Rect (if target size set)

Example output:

```
=== ORIGINAL RECT ===
pygame.Rect(159, 451, 391, 143)

=== SCALED RECT ===
pygame.Rect(109, 309, 268, 98)
```

---

## 🛠 Requirements
```
opencv-python
tkinter (built-in)
numpy
```

Install OpenCV:

```bash
pip install opencv-python
```

---

## 🚀 Running the Tool

```
python rect_picker_tool.py
```

A window will appear with two buttons:
- **Upload Image**
- **Set Target Size**

---

## 🧱 File Structure

```
rect_picker_tool.py
```

No extra files required.

---

## 💡 Notes
- Works on any resolution
- Scaling is optional
- Output appears in both terminal AND image preview window
- Helps avoid trial-and-error in GUI development

---

## 👤 Developeed with ai 
Creator of Connect 4 AI Project and the Rect Picker Tool.
## 📜 License
Free to use and modify for educational and personal projects.
