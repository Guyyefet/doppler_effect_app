import matplotlib.pyplot as plt
from view.gui import create_gui
from presenter.simulation_presenter import SimulationPresenter

def main():
    fig, ax, sliders, start_button = create_gui()
    presenter = SimulationPresenter(fig, ax, sliders, start_button)
    plt.show()

if __name__ == "__main__":
    main()