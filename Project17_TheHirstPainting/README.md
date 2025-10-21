# 🎨 The Damien Hirst’s Dots Painting Program  

## 📘 Project Overview  
This project generates a **computerized replica of Damien Hirst’s dot paintings** using Python’s `turtle` graphics and `colorgram` libraries. It extracts dominant colors from an input image and arranges them into a uniform grid of colorful dots, simulating the British artist’s iconic “spot paintings.”  

The implementation demonstrates **modular design**, **randomized artistic variation**, and **basic computer graphics programming**. Through color extraction and grid-based composition, the program bridges **computational art** and **algorithmic creativity**.  

---

## 🧩 Key Features  
- 🎨 **Automatic Color Extraction** – Uses `colorgram` to extract dominant colors from an image.  
- 🟢 **Grid-Based Dot Generation** – Produces a grid of colored dots using `turtle`.  
- 🔄 **Randomized Color Selection** – Randomly selects colors for each dot to enhance visual diversity.  
- ⚙️ **Configurable Parameters** – Easily adjust the number of rows, columns, dot size, and spacing.  
- 💡 **Modular Design** – Encapsulates drawing logic within a single, reusable function.  

---

## 🧠 Object-Oriented and Functional Design Summary  

| **Component** | **Type** | **Responsibility** | **Description** |
|----------------|-----------|--------------------|-----------------|
| `hirst_dot_painting()` | Function | Core Drawing Routine | Generates a structured grid of dots using Turtle Graphics. |
| `colorgram` | Library | Color Extraction | Analyzes an input image and extracts dominant RGB color values. |
| `turtle` | Library | Visualization Engine | Handles drawing operations for dot placement and rendering. |
| `random` | Library | Randomization Control | Randomly selects dot colors from the extracted palette. |
| `Screen`, `Turtle` | Classes | Window & Cursor Management | Manage drawing space, cursor position, and window properties. |

---

## 🧰 Project Structure  
```plaintext
hirst_dots_painting/
│── main.py      # Main program logic
│── DamienHirstDotsPainting.jpg # Reference image for color extraction
│── README.md                 # Project documentation
```

## ⚙️ Parameter Configuration  

The following variables can be adjusted to customize the artwork:  

| **Parameter** | **Default Value** | **Description** |
|----------------|-------------------|-----------------|
| `rows` | `10` | Number of dot rows. |
| `cols` | `10` | Number of dot columns. |
| `dots_size` | `20` | Diameter of each dot (in pixels). |
| `horizontal_space` | `50` | Horizontal distance between dots. |
| `vertical_space` | `50` | Vertical distance between dot rows. |
| `number_of_colors` | `20` | Number of dominant colors extracted from the reference image. |

---

## 🧮 Example Output  
After execution, the program produces a **10×10 grid** of colorful dots inspired by Damien Hirst’s artwork.  
Each dot’s color is randomly chosen from the extracted palette, resulting in a unique artistic composition each time the program runs.

---

## 🖋️ Author  
**Jonathan Eduardo Castilla Zamora**  
---
