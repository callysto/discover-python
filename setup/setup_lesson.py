from IPython.display import HTML, Javascript, IFrame, clear_output
help(IFrame)

def setup(): 
    """ 
    Sets up: 
        run button
        blockly code blocks
    """ 
    clear_output()

    # adds run button to side of each cell
    add_run_button()
    setup_blockly()
    
    # make blockly windows appear
    
def add_run_button(): 
    # set up run button for every cell
    display(HTML("<style>div.run_this_cell{display:block;}table {margin-left: 0 !important;}</style>"))

def setup_blockly():
    display(Javascript('Jupyter.notebook.execute_cell_range(3,40)'))
    #Javascript(IPython.notebook.execute_cell_range(2,26))

