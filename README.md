# Dashboard design via dash
## Interactive Sales Statistics Dashboard 

<img width="1902" height="869" alt="dashboard" src="https://github.com/user-attachments/assets/a791ab32-a6ab-41be-b1c2-d632b82c9159" />

A professional and interactive **Dash** and **Plotly** web application designed to visualize and cross-filter sales data across economic cycles.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Dash-0080FF?style=for-the-badge&logo=dash&logoColor=white" alt="Dash" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
  <img src="https://img.shields.io/badge/License-MIT-44CC11?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="MIT License" />
</p>

<img width="1908" height="866" alt="Animation" src="https://github.com/user-attachments/assets/601a65e1-0f59-49ed-a9b3-52f16e36cd2f" />

It features;
* dynamic data reloading,
* cross-graph slicing,
* a state-reset mechanism,
* and secure remote deployment.

## 🚀 Key Features

🎛️ Dynamic Multi-Layer Filtering: Select between recessionary/non-recessionary states to dynamically update available target years.

📋 Summary of User-Selections for Smooth Navigation: Monitor summary of selections at the top of plots area to navigate smoothly.

🎯 Advanced Cross-Filtering: Clicking on any data point within any plot automatically slices the remaining charts by that specific dimension (e.g., Vehicle Type, Month, etc.) in real-time.

🔄 State-Aware Reset Mechanism: A robust, single-click reset functionality to flush UI state, and restore initial layouts.

🌐 Secure Remote Access: Optimized to run over secure tunnels (e.g., Ngrok) for instant global sharing.

---

## 🛠️ Tech Stack & Libraries

* **Framework:** Dash 2.0+ (Python)
* **Frontend UI:** Dash Bootstrap Components (DBC), Dash Core Components (DCC), Dash HTML Components
* **Data Processing:** Pandas
* **Visualization:** Plotly Express / Graphical Objects

---

## 💻 Installation & Setup

Follow these steps to run the dashboard locally on your machine:

### 1. Clone the Repository

git clone [https://github.com/ali-can-turan/dash-dashboard-design](https://github.com/ali-can-turan/dash-dashboard-design)

cd ...

### 2. Install libaries
``` shell
pip install dash dash-bootstrap-components pandas plotly
```
