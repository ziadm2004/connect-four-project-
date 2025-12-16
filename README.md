# 🎮 Connect 4 – Python AI Project

This project is an implementation of the **Connect 4 game** using **Python** and **Pygame**.  
It includes a complete graphical interface, sound effects, and an AI opponent based on  
the **Minimax algorithm with Alpha-Beta pruning**, as required in the Artificial Intelligence course.

---

## ⭐ Features
- Two game modes:
  - **Player vs Player**
  - **Player vs AI** (Easy – Medium – Hard – Expert)
- Full GUI with images & clickable buttons  
- Sound effects for all interactions (drop, win, lose, button, etc.)
- Move validation & preview indicator  
- Win detection (horizontal, vertical, diagonal)  
- Tie detection  
- Clean modular code using classes (GUI – Logic – AI – Audio – Main)

---

## 📁 Project Structure

| File / Folder | Description |
|---------------|-------------|
| **main.py** | Game controller + state handling |
| **gui.py** | All screens, buttons, drawing board & pieces |
| **logic.py** | Game rules, player turns, win detection |
| **ai.py** | Minimax + Alpha-Beta + heuristic evaluation |
| **audio.py** | Sound management & playback |
| **pictures/** | All required images |
| **sounds/** | All required audio files |

---

## 📦 Requirements

### Install required libraries:
```
pip install pygame
pip install pyinstaller   # optional for building .exe
```

### Built-in modules (no installation needed):
```
time, os, sys, math, random
```

---

## ▶ Running the Game

Make sure these folders exist:

### **pictures/**
```
intro_screen.png
start_screen.png
mode_selection.png
difficulty_selection.png
win_screen.png
lose_screen.png
tie_screen.png
menu_end.png
```

### **sounds/**
```
drop.wav
ai_move.wav
win.wav
lose.wav
error.wav
button.wav
```

### Then run:
```
python main.py
```

---

## 🤖 AI Summary

The AI system is built using:

- **Minimax algorithm**
- **Alpha-Beta pruning**
- **Immediate win / block move detection**
- **Heuristic evaluation based on:**
  - Center column advantage
  - 2-in-a-row / 3-in-a-row opportunities
  - Blocking opponent threats

---

## 🎯 Project Goal

This implementation satisfies all course requirements:

- Game environment & interactive interface  
- Input validation  
- Human vs AI gameplay  
- Minimax + Alpha-Beta  
- Clean modular code  
- Proper documentation & structured project  

---

# 👥 Team Contribution (Course Requirement)

Although the project was developed individually, the work is divided according  
to the required team-based structure.

---

## 👤 **Ziad Shawky — Lead Developer & Project Owner**

### ✔ Responsibilities:
- Designed the complete GUI and all game screens  
- Implemented full game logic (board, turns, win detection)  
- Developed the Minimax + Alpha-Beta AI system  
- Created the audio manager and added all sound effects  
- Built the main game controller & state machine  
- Created button coordinates using image analysis tools  
- Added error handling & input validation  
- Structured and organized all modules  
- Wrote the README & project documentation  
- Managed the full GitHub repository

---

# 🧩 Team Structure (Required by Instructor)

## 👤 Student A – GUI Designer
- Designing all screens  
- Positioning buttons & layout  
- Implementing drawing functions in **gui.py**

## 👤 Student B – Logic Developer
- Building board system  
- Implementing full win detection  
- Managing player turn logic  

## 👤 Student C – AI Engineer
- Implementing **Minimax**  
- Applying **Alpha-Beta pruning**  
- Writing heuristic evaluation  
- Implementing difficulty levels  

## 👤 Student D – Audio & Interaction
- Managing sound effects  
- Adding feedback sounds  
- Integrating UI interaction audio  

## 👤 Student E – Integration & Project Lead
- Writing **main.py**  
- Linking GUI + Logic + AI + Audio  
- Testing and debugging  
- Documentation & GitHub commits  

---

### ✔ Final Note
> **All tasks were completed by a single developer (myself), but divided according to the project’s required team structure.**

