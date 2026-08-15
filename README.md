# 🎓 College Friendship Network Analyzer

An interactive data science application for analyzing college friendship networks using Graph Theory, NetworkX and Streamlit.

The project represents students as nodes and friendships as edges, allowing users to explore the structure and influence of individuals within a social network.

---

## 🚀 Live Demo

👉 **[Open the College Friendship Network Analyzer](https://college-friendship-network-analyzer-sbhra2gckzusuqv8wmb8e3.streamlit.app/)**

The application is deployed using Streamlit Community Cloud and can be used directly in the browser.

[![Open App](https://img.shields.io/badge/Live%20Demo-Streamlit-red?logo=streamlit)](https://college-friendship-network-analyzer-sbhra2gckzusuqv8wmb8e3.streamlit.app/)

---

## 📌 Project Overview

Social relationships can be represented mathematically using graph theory.

In this project:

- Students are represented as **nodes**
- Friendships are represented as **edges**
- Network metrics are used to identify influential students
- Community detection is used to identify groups
- Interactive visualizations help understand the structure of the network

The application allows users to dynamically create and analyze their own friendship network.

---

## ✨ Features

- 👥 Dynamic student network creation
- 🤝 Interactive friendship selection
- 🕸️ Network visualization
- 📊 Multiple centrality measures
- 🧩 Community detection
- 🔍 Student-level analysis
- 📈 Centrality visualizations
- 📥 CSV, TXT and PDF export
- 📄 Professional automated reporting
- 🌐 Live Streamlit deployment

### 📊 Network Metrics

The application calculates several important Graph Theory metrics:

#### Degree Centrality

Measures how well-connected a student is within the network.

#### Betweenness Centrality

Measures how frequently a student lies on the shortest paths between other students.

#### Closeness Centrality

Measures how close a student is to all other students in the network.

#### PageRank

Measures the relative importance of students based on the structure of their connections.

#### Clustering Coefficient

Measures how strongly a student's friends are connected to each other.

#### Network Density

Measures how many friendship connections exist compared with the maximum possible number of connections.

---

## 🏘️ Community Detection

The application uses the **Greedy Modularity Community Detection** algorithm to identify groups of closely connected students.

The detected communities are displayed separately in the dashboard.

---

## 👥 Connected Components

The application identifies disconnected groups within the friendship network.

This helps determine whether the entire student network is connected or consists of multiple independent groups.

---

## 🔍 Individual Student Analysis

Users can select an individual student and view:

- Number of friendships
- Degree centrality
- Betweenness centrality
- PageRank
- Friends
- Community membership

---

## 📈 Data Visualization

The application provides several visualizations:

- Friendship network graph
- Degree centrality chart
- Centrality comparison chart
- Community-based network visualization

---

## 📥 Export & Reporting

The application provides multiple export options:

- 📊 Friendship Network CSV
- 📈 Network Centrality CSV
- 📝 Text Report
- 📄 Professional PDF Report

Users can generate and download reports directly from the application.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Streamlit** — Interactive web application
- **NetworkX** — Graph and network analysis
- **Matplotlib** — Data visualization
- **Pandas** — Data handling and analysis
- **ReportLab** — Professional PDF report generation

## 🧠 Graph Theory Concepts

The project applies several concepts from Graph Theory and Social Network Analysis:

- Nodes — Represent students
- Edges — Represent friendships
- Degree Centrality
- Betweenness Centrality
- Closeness Centrality
- PageRank
- Clustering Coefficient
- Network Density
- Connected Components
- Community Detection

## 📸 Screenshots

### 🏠 Dashboard

![Dashboard](screenshots/dashboard.png)

### 🌐 Network Visualization

![Network Visualization](screenshots/network.png)

### 📊 Centrality Analysis

![Centrality Analysis](screenshots/centrality.png)

### 📈 Centrality Visualization 1

![Centrality Visualization 1](screenshots/centrality1.png)

### 📈 Centrality Visualization 2

![Centrality Visualization 2](screenshots/centrality2.png)

### 🏘️ Community Detection

![Community Detection](screenshots/communities.png)

### 🔍 Student-Level Analysis

![Student-Level Analysis](screenshots/student-analysis.png)

## ⚠️ Disclaimer

This project is an educational demonstration of Graph Theory and Social Network Analysis.

The student names shown in the screenshots are sample representations and do not represent real personal relationship data.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/college-friendship-network-analyzer.git
```text
A, B, C, D, E, F, G
