import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import tempfile
import os

from networkx.algorithms import community
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="College Friendship Network Analyzer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #9ca3af;
        margin-bottom: 25px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 15px;
        background: linear-gradient(135deg, #172033, #202b45);
        border: 1px solid #334155;
        text-align: center;
    }

    .metric-title {
        font-size: 14px;
        color: #94a3b8;
    }

    .metric-value {
        font-size: 30px;
        font-weight: 700;
    }

    .insight-card {
        padding: 18px;
        border-radius: 12px;
        background-color: #172554;
        border-left: 5px solid #3b82f6;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎓 College Friendship Network Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze student relationships using Graph Theory, NetworkX and Data Visualization'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚙️ Network Controls")

num_students = st.sidebar.slider(
    "Number of Students",
    min_value=3,
    max_value=15,
    value=7
)

students = [
    chr(65 + i)
    for i in range(num_students)
]

st.sidebar.markdown("---")

st.sidebar.subheader("👥 Students")

st.sidebar.write(", ".join(students))

st.sidebar.markdown("---")

st.sidebar.subheader("🤝 Select Friendships")

friendships = []

for i in range(num_students):

    for j in range(i + 1, num_students):

        friendship = st.sidebar.checkbox(
            f"{students[i]} ↔ {students[j]}",
            key=f"friendship_{students[i]}_{students[j]}"
        )

        if friendship:
            friendships.append(
                (students[i], students[j])
            )


# ============================================================
# CREATE GRAPH
# ============================================================

G = nx.Graph()

G.add_nodes_from(students)

G.add_edges_from(friendships)


# ============================================================
# BASIC NETWORK INFORMATION
# ============================================================

number_students = G.number_of_nodes()
number_friendships = G.number_of_edges()

density = nx.density(G)


# ============================================================
# NETWORK METRICS
# ============================================================

degree_centrality = nx.degree_centrality(G)

betweenness_centrality = nx.betweenness_centrality(G)

closeness_centrality = nx.closeness_centrality(G)

clustering = nx.clustering(G)

components = list(
    nx.connected_components(G)
)


# ============================================================
# PAGERANK
# ============================================================

if number_friendships > 0:

    try:
        pagerank = nx.pagerank(
            G,
            alpha=0.85
        )

    except Exception:
        pagerank = {
            node: 0
            for node in students
        }

else:

    pagerank = {
        node: 0
        for node in students
    }


# ============================================================
# COMMUNITY DETECTION
# ============================================================

if number_friendships > 0:

    communities = list(
        community.greedy_modularity_communities(G)
    )

else:

    communities = [
        frozenset([student])
        for student in students
    ]


# ============================================================
# COMMUNITY MAPPING
# ============================================================

community_map = {}

for community_id, group in enumerate(communities):

    for student in group:

        community_map[student] = community_id


# ============================================================
# TOP STUDENTS
# ============================================================

if students:

    top_degree = max(
        degree_centrality,
        key=degree_centrality.get
    )

    top_betweenness = max(
        betweenness_centrality,
        key=betweenness_centrality.get
    )

    top_closeness = max(
        closeness_centrality,
        key=closeness_centrality.get
    )

    top_pagerank = max(
        pagerank,
        key=pagerank.get
    )


# ============================================================
# DASHBOARD METRICS
# ============================================================

st.subheader("📊 Network Overview")

metric1, metric2, metric3, metric4, metric5 = st.columns(5)

with metric1:

    st.metric(
        "👥 Students",
        number_students
    )

with metric2:

    st.metric(
        "🤝 Friendships",
        number_friendships
    )

with metric3:

    st.metric(
        "🌐 Density",
        f"{density:.2f}"
    )

with metric4:

    st.metric(
        "👥 Groups",
        len(components)
    )

with metric5:

    st.metric(
        "🏘️ Communities",
        len(communities)
    )


st.markdown("---")


# ============================================================
# MAIN TABS
# ============================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🕸️ Network",
        "📊 Centrality",
        "🏘️ Communities",
        "🔍 Student Analysis",
        "📥 Export"
    ]
)


# ============================================================
# TAB 1 - NETWORK VISUALIZATION
# ============================================================

with tab1:

    st.subheader("🕸️ Friendship Network")

    if number_students > 0:

        fig, ax = plt.subplots(
            figsize=(10, 7)
        )

        pos = nx.spring_layout(
            G,
            seed=42,
            k=1.2
        )

        # Create node colors based on communities

        node_colors = [
            community_map.get(node, 0)
            for node in G.nodes()
        ]

        nx.draw_networkx_edges(
            G,
            pos,
            ax=ax,
            edge_color="gray",
            width=1.8,
            alpha=0.7
        )

        nx.draw_networkx_nodes(
            G,
            pos,
            ax=ax,
            node_color=node_colors,
            cmap=plt.cm.tab10,
            node_size=1800,
            edgecolors="black",
            linewidths=1
        )

        nx.draw_networkx_labels(
            G,
            pos,
            ax=ax,
            font_size=13,
            font_weight="bold"
        )

        ax.set_title(
            "College Friendship Network",
            fontsize=18,
            fontweight="bold"
        )

        ax.axis("off")

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

    st.info(
        "Each node represents a student and each edge represents a friendship."
    )


# ============================================================
# TAB 2 - CENTRALITY
# ============================================================

with tab2:

    st.subheader("📊 Network Centrality Analysis")

    centrality_df = pd.DataFrame(
        {
            "Student": students,
            "Degree Centrality": [
                degree_centrality[s]
                for s in students
            ],
            "Betweenness Centrality": [
                betweenness_centrality[s]
                for s in students
            ],
            "Closeness Centrality": [
                closeness_centrality[s]
                for s in students
            ],
            "PageRank": [
                pagerank[s]
                for s in students
            ],
            "Clustering Coefficient": [
                clustering[s]
                for s in students
            ]
        }
    )

    st.dataframe(
        centrality_df.style.format(
            {
                "Degree Centrality": "{:.3f}",
                "Betweenness Centrality": "{:.3f}",
                "Closeness Centrality": "{:.3f}",
                "PageRank": "{:.3f}",
                "Clustering Coefficient": "{:.3f}"
            }
        ),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("🏆 Top Network Positions")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success(
            f"⭐ Degree\n\n**{top_degree}**"
        )

    with c2:
        st.info(
            f"🌉 Betweenness\n\n**{top_betweenness}**"
        )

    with c3:
        st.warning(
            f"🎯 Closeness\n\n**{top_closeness}**"
        )

    with c4:
        st.success(
            f"🚀 PageRank\n\n**{top_pagerank}**"
        )

    st.markdown("---")

    # Degree centrality chart

    st.subheader("📈 Degree Centrality")

    degree_chart = pd.DataFrame(
        {
            "Student": students,
            "Degree Centrality": [
                degree_centrality[s]
                for s in students
            ]
        }
    )

    st.bar_chart(
        degree_chart.set_index("Student")
    )

    # Comparison chart

    st.subheader("📊 Centrality Comparison")

    comparison_df = pd.DataFrame(
        {
            "Degree": [
                degree_centrality[s]
                for s in students
            ],
            "Betweenness": [
                betweenness_centrality[s]
                for s in students
            ],
            "Closeness": [
                closeness_centrality[s]
                for s in students
            ],
            "PageRank": [
                pagerank[s]
                for s in students
            ]
        },
        index=students
    )

    st.line_chart(
        comparison_df
    )


# ============================================================
# TAB 3 - COMMUNITIES
# ============================================================

with tab3:

    st.subheader("🏘️ Community Detection")

    st.write(
        "Communities represent groups of students that have stronger "
        "connections within the network."
    )

    for index, group in enumerate(
        communities,
        start=1
    ):

        members = ", ".join(
            sorted(group)
        )

        st.success(
            f"Community {index}: {members}"
        )

    st.markdown("---")

    st.subheader("🔗 Connected Components")

    for index, component in enumerate(
        components,
        start=1
    ):

        members = ", ".join(
            sorted(component)
        )

        st.info(
            f"Component {index}: {members}"
        )


# ============================================================
# TAB 4 - INDIVIDUAL STUDENT ANALYSIS
# ============================================================

with tab4:

    st.subheader("🔍 Student-Level Analysis")

    selected_student = st.selectbox(
        "Select a student",
        students
    )

    student_degree = G.degree(
        selected_student
    )

    student_neighbors = list(
        G.neighbors(selected_student)
    )

    st.markdown("---")

    a, b, c, d = st.columns(4)

    with a:

        st.metric(
            "🤝 Friendships",
            student_degree
        )

    with b:

        st.metric(
            "⭐ Degree",
            f"{degree_centrality[selected_student]:.3f}"
        )

    with c:

        st.metric(
            "🌉 Betweenness",
            f"{betweenness_centrality[selected_student]:.3f}"
        )

    with d:

        st.metric(
            "🚀 PageRank",
            f"{pagerank[selected_student]:.3f}"
        )

    st.markdown("---")

    st.subheader(
        f"👥 Friends of {selected_student}"
    )

    if student_neighbors:

        st.write(
            ", ".join(student_neighbors)
        )

    else:

        st.warning(
            f"{selected_student} currently has no friendships."
        )

    st.subheader("🏘️ Community")

    student_community = community_map.get(
        selected_student
    )

    st.write(
        f"Community {student_community + 1}"
    )


# ============================================================
# TAB 5 - EXPORT
# ============================================================

with tab5:

    st.subheader("📥 Export Your Analysis")

    # --------------------------------------------------------
    # NETWORK DATA
    # --------------------------------------------------------

    st.markdown("### 📄 Network Data")

    network_data = pd.DataFrame(
        friendships,
        columns=[
            "Student 1",
            "Student 2"
        ]
    )

    csv_data = network_data.to_csv(
        index=False
    )

    st.download_button(
        label="⬇️ Download Friendship CSV",
        data=csv_data,
        file_name="friendship_network.csv",
        mime="text/csv"
    )

    # --------------------------------------------------------
    # CENTRALITY DATA
    # --------------------------------------------------------

    centrality_csv = centrality_df.to_csv(
        index=False
    )

    st.download_button(
        label="⬇️ Download Centrality CSV",
        data=centrality_csv,
        file_name="network_centrality.csv",
        mime="text/csv"
    )

    # --------------------------------------------------------
    # TEXT REPORT
    # --------------------------------------------------------

    report_text = f"""
COLLEGE FRIENDSHIP NETWORK ANALYZER
====================================

Network Overview
----------------
Students: {number_students}
Friendships: {number_friendships}
Network Density: {density:.3f}
Connected Components: {len(components)}
Communities: {len(communities)}

Top Students
------------
Highest Degree Centrality: {top_degree}
Highest Betweenness Centrality: {top_betweenness}
Highest Closeness Centrality: {top_closeness}
Highest PageRank: {top_pagerank}

Friendships
-----------
{friendships}

Communities
-----------
{communities}
"""

    st.download_button(
        label="⬇️ Download Text Report",
        data=report_text,
        file_name="friendship_network_report.txt",
        mime="text/plain"
    )

    st.markdown("---")

    # ========================================================
    # PDF REPORT
    # ========================================================

    st.subheader("📄 Professional PDF Report")

    def generate_pdf():

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        pdf_path = temp_file.name

        doc = SimpleDocTemplate(
            pdf_path,
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40
        )

        styles = getSampleStyleSheet()

        content = []

        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        content.append(
            Paragraph(
                "College Friendship Network Analyzer",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 15)
        )

        content.append(
            Paragraph(
                "Graph Theory Based Social Network Analysis",
                styles["Heading2"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        # ----------------------------------------------------
        # OVERVIEW
        # ----------------------------------------------------

        content.append(
            Paragraph(
                "Network Overview",
                styles["Heading2"]
            )
        )

        overview_data = [
            ["Metric", "Value"],
            ["Students", str(number_students)],
            ["Friendships", str(number_friendships)],
            ["Network Density", f"{density:.3f}"],
            ["Connected Components", str(len(components))],
            ["Communities", str(len(communities))]
        ]

        overview_table = Table(
            overview_data,
            colWidths=[250, 150]
        )

        overview_table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#1f4e78")
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey
                    ),
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER"
                    ),
                    (
                        "PADDING",
                        (0, 0),
                        (-1, -1),
                        8
                    )
                ]
            )
        )

        content.append(
            overview_table
        )

        content.append(
            Spacer(1, 20)
        )

        # ----------------------------------------------------
        # TOP STUDENTS
        # ----------------------------------------------------

        content.append(
            Paragraph(
                "Key Network Insights",
                styles["Heading2"]
            )
        )

        insights = [
            f"Highest Degree Centrality: {top_degree}",
            f"Highest Betweenness Centrality: {top_betweenness}",
            f"Highest Closeness Centrality: {top_closeness}",
            f"Highest PageRank: {top_pagerank}"
        ]

        for insight in insights:

            content.append(
                Paragraph(
                    "• " + insight,
                    styles["Normal"]
                )
            )

            content.append(
                Spacer(1, 5)
            )

        content.append(
            Spacer(1, 15)
        )

        # ----------------------------------------------------
        # CENTRALITY TABLE
        # ----------------------------------------------------

        content.append(
            Paragraph(
                "Centrality Analysis",
                styles["Heading2"]
            )
        )

        centrality_table_data = [
            [
                "Student",
                "Degree",
                "Betweenness",
                "Closeness",
                "PageRank"
            ]
        ]

        for student in students:

            centrality_table_data.append(
                [
                    student,
                    f"{degree_centrality[student]:.3f}",
                    f"{betweenness_centrality[student]:.3f}",
                    f"{closeness_centrality[student]:.3f}",
                    f"{pagerank[student]:.3f}"
                ]
            )

        centrality_table = Table(
            centrality_table_data,
            repeatRows=1
        )

        centrality_table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#1f4e78")
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey
                    ),
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER"
                    ),
                    (
                        "FONTSIZE",
                        (0, 0),
                        (-1, -1),
                        8
                    ),
                    (
                        "PADDING",
                        (0, 0),
                        (-1, -1),
                        6
                    )
                ]
            )
        )

        content.append(
            centrality_table
        )

        content.append(
            Spacer(1, 20)
        )

        # ----------------------------------------------------
        # COMMUNITIES
        # ----------------------------------------------------

        content.append(
            Paragraph(
                "Detected Communities",
                styles["Heading2"]
            )
        )

        for index, group in enumerate(
            communities,
            start=1
        ):

            members = ", ".join(
                sorted(group)
            )

            content.append(
                Paragraph(
                    f"Community {index}: {members}",
                    styles["Normal"]
                )
            )

            content.append(
                Spacer(1, 5)
            )

        content.append(
            Spacer(1, 20)
        )

        # ----------------------------------------------------
        # FRIENDSHIPS
        # ----------------------------------------------------

        content.append(
            Paragraph(
                "Friendship Connections",
                styles["Heading2"]
            )
        )

        for friendship in friendships:

            content.append(
                Paragraph(
                    f"{friendship[0]} ↔ {friendship[1]}",
                    styles["Normal"]
                )
            )

        content.append(
            Spacer(1, 20)
        )

        content.append(
            Paragraph(
                "Generated using Python, NetworkX, Streamlit and ReportLab.",
                styles["Normal"]
            )
        )

        doc.build(content)

        return pdf_path

    if st.button(
        "📄 Generate PDF Report"
    ):

        pdf_path = generate_pdf()

        with open(
            pdf_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                label="⬇️ Download PDF Report",
                data=pdf_file,
                file_name="college_friendship_network_report.pdf",
                mime="application/pdf"
            )

        os.unlink(pdf_path)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#94a3b8;">
        🎓 College Friendship Network Analyzer<br>
        Built with Python • NetworkX • Streamlit • Matplotlib • ReportLab
    </div>
    """,
    unsafe_allow_html=True
)
