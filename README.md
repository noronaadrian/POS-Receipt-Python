# 🍔 Munch Craze Mix ’n Match Ordering System
*A simple Python console-based food ordering program*

---

## 📖 Overview
**Munch Craze Mix ’n Match** is a simple **Point-of-Sale (POS)** simulation for a fast-food promo.  
It allows customers to choose a **main dish** and an **add-on** for ₱75 per set.  
The program computes VAT, discounts, and prints a complete receipt.

---

## ⚙️ Features
- Display main and add-on menus
- Order multiple combos
- Compute VAT (12%)
- Apply senior citizen/PWD discount (20%)
- Handle payment and calculate change
- Generate a receipt with date/time and details

---

## 🧠 How It Works
### 1. Menu
The program displays available items:


### 2. Order
You can type the item codes (e.g., `m1` and `p2`), then specify quantity.  
Type `done` to finish ordering.

### 3. Computation
- Each meal combo = ₱75
- VAT = 12%
- Optional discount = 20% (for seniors/PWD)

### 4. Payment
The program validates payment and computes change.

### 5. Receipt
A formatted receipt is shown with:
- Order summary
- VAT
- Discount (if any)
- Total cost
- Change
- Date/time and thank-you message

---

## 💻 How to Run
### Requirements
- Python 3.x installed

### Run Command
```bash
python munch_craze.py
