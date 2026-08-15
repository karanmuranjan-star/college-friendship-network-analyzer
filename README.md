# 🎓 College Friendship Network Analyzer

An interactive data science application for analyzing college friendship networks using Graph Theory, NetworkX and Streamlit.

The project represents students as nodes and friendships as edges, allowing users to explore the structure and influence of individuals within a social network.

---

## 🚀 Live Demo

🌐 **Streamlit App:**  
..[https://college-friendship-network-analyzer-sbhra2gckzusuqv8wmb8e3.streamlit.app/]

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

### 🕸️ Interactive Network Visualization

Visualizes students and their friendship connections using NetworkX.

The network graph includes:

- Student nodes
- Friendship edges
- Community-based node grouping
- Interactive Streamlit interface

---

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

## 📥 Export Options

Users can export:

- Friendship network CSV
- Centrality analysis CSV
- Text report
- Professional PDF report

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| NetworkX | Graph creation and network analysis |
| Matplotlib | Network and statistical visualization |
| Pandas | Data processing and tabular analysis |
| ReportLab | PDF report generation |

---

# 🧠 Graph Theory Concepts Used

The project demonstrates practical applications of:

- Graphs
- Nodes
- Edges
- Degree
- Degree Centrality
- Betweenness Centrality
- Closeness Centrality
- PageRank
- Clustering Coefficient
- Connected Components
- Community Detection
- Network Density

---

# 📊 Example Network

A sample network can contain students such as:

## 📸 Screenshots

### 🏠 Dashboard

![Dashboard](screenshots/dashboard.png)

### 🕸️ Network Visualization

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

```text
A, B, C, D, E, F, G
