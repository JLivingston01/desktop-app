
import PySimpleGUI as sg
import numpy as np

Menu = sg.Menu(
    [['File', ['Exit']]],
    k='MENUBAR'
)

Row1 = [
        [sg.Text('Profiteer'),]
    ]

col1 =[
    
        [sg.Text('Startup Costs: '),sg.Input(s=45,k='INIT_COSTS')],
        [sg.Text('YoY Growth: '),sg.Slider(range=(0,1),resolution=.01,k='GROWTH')],
        [sg.Text('Y1 Customers: '),sg.Input(s=45,k='INIT_CUSTS')],
        [sg.Text('Revenue per Cust: '),sg.Input(s=45,k='RP_CUST')],
        [sg.Text('Cost per Cust: '),sg.Input(s=45,k='CP_CUST')],
        
        [sg.Button("Ready!")]
    
]

col2 =[
        [sg.Text("Analysis will be here",s=(35,35),k="OUTPUT")],
]

layout = [
    [Menu],
    [Row1],
    [
        sg.Column(col1),
        sg.VSeparator(),
        sg.Column(col2),
    ]
]

window = sg.Window("Test App", 
                   layout,)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Ready!":
        INIT_COSTS = float(values['INIT_COSTS'])
        GROWTH = float(values['GROWTH'])
        INIT_CUSTS = float(values['INIT_CUSTS'])
        RP_CUST = float(values['RP_CUST'])
        CP_CUST = float(values['CP_CUST'])

        growth_factor = np.sum([(1+GROWTH)**i for i in range(5)])
        future_custs = INIT_CUSTS*growth_factor
        future_revenue = future_custs*RP_CUST
        future_costs = future_custs*CP_CUST

        net_outcome = future_revenue - future_costs - INIT_COSTS

        emote = "Uh oh" if net_outcome < 0 else "Awesome!"
        text_out = f"Your net income projected is: {net_outcome}. {emote}"

        output = window['OUTPUT']
        output.update(text_out)


window.close()

