# 🤖 AI Lab 1 – Vacuum Cleaner Problem (Python)

![AI](https://img.shields.io/badge/Field-Artificial%20Intelligence-blue)
![Language](https://img.shields.io/badge/Language-Python-yellow)
![Status](https://img.shields.io/badge/Project-AI%20Lab-green)

---

# 📘 Project Overview

This repository contains implementations of the **Vacuum Cleaner Problem**, one of the most fundamental examples used in **Artificial Intelligence (AI)** to explain how intelligent agents perceive environments and take actions.

The project demonstrates how an **AI agent senses the environment and performs actions like moving and cleaning based on the state of the environment**.

This experiment is part of **Artificial Intelligence Laboratory work**.

---

# 🧠 Vacuum Cleaner World

The **Vacuum Cleaner World** is a simple environment consisting of:

* Two locations: **A** and **B**
* Each location may contain **dirt** or be **clean**
* The agent (vacuum cleaner) can move and clean the environment

### Environment Representation

![Vacuum World](https://upload.wikimedia.org/wikipedia/commons/3/3f/Vacuum-cleaner-world.svg)

The vacuum cleaner agent follows simple rules:

| Condition         | Action       |
| ----------------- | ------------ |
| Dirt detected     | Suck         |
| At location A     | Move Right   |
| At location B     | Move Left    |
| Clean environment | No Operation |

---

# 🧩 AI Concepts Demonstrated

This project demonstrates several important AI concepts:

### 1️⃣ Intelligent Agents

An **agent** is an entity that:

* perceives its environment
* takes actions to achieve goals.

### 2️⃣ Environment Types

The vacuum world is an example of:

* Observable environment
* Deterministic environment
* Sequential environment

### 3️⃣ Simple Reflex Agent

The agent follows **condition–action rules**:

```
IF location is dirty → clean
IF location is clean → move to other location
```

---

# 📂 Project Structure

```
ailab1/
│
├── vaccum.py
├── vaccum2.py
├── vaccum3.py
├── vaccum4.py
├── vaccum5.py
└── README.md
```

### File Descriptions

| File         | Description                             |
| ------------ | --------------------------------------- |
| `vaccum.py`  | Basic vacuum cleaner simulation         |
| `vaccum2.py` | Vacuum agent with additional conditions |
| `vaccum3.py` | Improved environment representation     |
| `vaccum4.py` | Enhanced decision logic                 |
| `vaccum5.py` | Extended AI simulation model            |

---

# ⚙️ Requirements

You only need:

* Python **3.x**

Download Python:

https://www.python.org/downloads/

Check installation:

```
python --version
```

---

# ▶️ How to Run the Programs

### 1️⃣ Clone the Repository

```
git clone https://github.com/vinayaka29j/ailab1.git
```

### 2️⃣ Navigate to the Folder

```
cd ailab1
```

### 3️⃣ Run the Python Program

Example:

```
python vaccum.py
```

or

```
python vaccum5.py
```

---

# 🖥️ Example Output

```
Location A is Dirty
Vacuum Cleaner is Cleaning...
Location A is Clean

Moving to Location B

Location B is Dirty
Vacuum Cleaner is Cleaning...
Location B is Clean
```

---

# 🧪 AI Lab Experiment

### Aim

To implement the **Vacuum Cleaner Problem using Python** and simulate the behavior of a simple reflex agent.

### Algorithm

1. Start the program
2. Initialize environment with dirt locations
3. Sense the current location
4. If dirty → clean
5. If clean → move to next location
6. Repeat until environment is clean
7. Stop

---

# 📊 AI Agent Architecture

![Agent Model](https://miro.medium.com/v2/resize\:fit:1200/1*J9E1JQy-2sSNQwasI50KPw.png)

The agent consists of:

* **Sensors** → Detect environment state
* **Decision Logic** → Apply condition-action rules
* **Actuators** → Perform actions like cleaning or moving

---

# 🚀 Future Improvements

Possible improvements to this project:

* GUI simulation using **Tkinter**
* Grid-based vacuum environment
* Multiple vacuum agents
* Reinforcement learning based cleaning
* Random dirt generation

---

# 👨‍💻 Author

**Vinayaka J**

Artificial Intelligence Laboratory
Computer Science / AI Projects

GitHub Profile:
https://github.com/vinayaka29j

---

# 📜 License

This project is intended for **educational and learning purposes** as part of an **Artificial Intelligence Laboratory course**.

---

⭐ If you like this project, consider **starring the repository**.
