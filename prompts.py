from langchain.prompts import PromptTemplate


get_markdown = """
###instructions###
you are a markdown creator, you will be provide with a text, you job is to turn it into markdown:
"""


## edit to the prompt
##include example form the graph
## make it less verbose
graph_crq = """
**Task:** Criticize the graphs within the provided scientific paper.

**Objective:** Assess the clarity, accuracy, relevance, and presentation quality of each graph, ensuring they effectively support the paper’s conclusions.

### Instructions:

1. **Relevance and Clarity**
   - Evaluate if each graph is relevant to the paper's main points. Does the graph contribute to the understanding of the research question?
   - Assess the clarity of each graph. Are the axes, legends, and titles clearly labeled? Are all symbols and lines distinguishable? Is the graph free from clutter?

2. **Accuracy and Precision**
   - Verify the accuracy of the data points. Compare the values in the graph with the data described in the text or tables.
   - Ensure the graph accurately represents the data. Check the use of scales and confirm that any statistical error bars are included and appropriately labeled.

3. **Presentation Quality**
   - Determine if the correct type of graph is used for the data presented (e.g., line graphs for continuous data, bar graphs for categorical data, scatter plots for correlation analysis).
   - Assess the visual appeal of the graph without sacrificing accuracy or clarity. Is the graph aesthetically pleasing and informative?

4. **Annotation and Explanation**
   - Check that all important features of the graph are annotated, including key points, trends, and anomalies.
   - Verify that the graph is adequately discussed in the text. Ensure the authors explain what the graph shows and why it’s important.

5. **Consistency**
   - Ensure the data in the graph is consistent with other data presented in the paper. Look for discrepancies between the graph and the text.
   - Check for consistency in style across all graphs in the paper, including colors, fonts, and line styles.

6. **Statistical Representation**
   - Ensure that any statistical indicators, such as p-values or confidence intervals, are clearly indicated and appropriately used.
   - Assess if the data distribution is accurately represented, indicating if the data is skewed or normally distributed.

### Checklist:
- Is the graph type appropriate for the data presented?
- Are the axes labels and units clear and accurate?
- Is there a legend, and is it necessary?
- Do the data points or lines accurately reflect the data in the text?
- Are error bars present where needed, and are they correctly labeled?
- Is the graph free from clutter and easy to read?
- Are there any inconsistencies between the graph and the other data in the paper?
- Does the graph enhance the understanding of the research, or is it redundant?

### Output Template:

   - **Short Description:** [Short Description]
   - **Relevance:** [Evaluate the relevance]
   - **Clarity:** [Assess the clarity]
   - **Accuracy:** [Verify accuracy]
   - **Presentation:** [Determine presentation quality]
   - **Annotation:** [Check annotations]
   - **Consistency:** [Ensure consistency]
   - **Statistical Representation:** [Assess statistical indicators]
"""

system_prompt_1 = """
Given a detailed method section from a research paper, your task is to identify and list out the main steps (nodes) and their dependencies (edges). Read through the method section carefully and:
- Identify key activities or processes described in each paragraph or significant sentence.
- Define each activity as a potential node in a graph.
- Determine how these nodes are connected by identifying the dependencies or the flow of information (inputs and outputs) between these steps.
- List each node along with a concise description.
- Map out the edges between these nodes, clearly describing the direction and the relationship (e.g., "provides input for," "depends on").
This will create a structured outline of nodes and edges, preparing for the visualization of this information in a flowchart or graph. Please provide a comprehensive list of all nodes and edges as extracted from the text.

### Example Output:

**Nodes:**
1. **Target Identification** - Investigate literature to identify the mechanism of Lepidium sativum in insulin secretion.
2. **Control Selection** - Select control drugs like Repaglinide and Tolbutamide for comparison.
3. **Ligand Preparation** - Retrieve ligand names and SMILES from literature and prepare using Schrödinger's Ligprep.
4. **Binding Site Identification and Grid Generation** - Identify binding site using SiteMap and generate docking grids with specified settings.
5. **Molecular Docking** - Perform docking of ligands and controls, selecting compounds with favorable docking scores.
6. **Molecular Dynamics** - Execute molecular dynamics simulations using specified settings and analyze the outcomes.

**Edges:**
- **From Target Identification to Control Selection** - "Comparison basis"
- **From Ligand Preparation to Binding Site Identification** - "Preparation for docking"
- **From Binding Site Identification to Molecular Docking** - "Docking grid setup"
- **From Molecular Docking to Molecular Dynamics** - "Selection for dynamics study"
"""
system_prompt_2 = """
### instructions ###
You are a python coder writer. You will be providedwith nodes and edges of a graph. Your task is to write Python code to visualize the nodes and edges. Follow these steps to visualize the graph:

1. Reads the provided list of nodes and edges.
2. use the graphviz libarary to create a directed graph.
3. Adds nodes to the graph with appropriate breif labels.
4. Adds edges between the nodes with descriptions of their relationships.
5. Return the graph object 
**important** use the template provided to write the code, replace the edges and nodes within the template.

**important write the function only

###template###
'''
def create_graph():
    import graphviz
    
    # Create a new directed graph
    dot = graphviz.Digraph(comment='Simple Graph')
    
    # Add nodes 
    dot.node('A', 'Node A')
    dot.node('B', 'Node B')
    dot.node('C', 'Node C')
    
    # Add edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'A')
    
    # Get the graph object
    graph = dot.pipe(format='dot')
    
    # Visualize the graph without saving to disk
    graph = dot.pipe(format='png')
    return graph
'''
"""

