from services.controller import Controller


def run_simulation():
    """ The entrypoint for the simulation """

    controller = Controller()
    while True:
        controller.update()
        controller.draw()


if __name__ == "__main__":
    run_simulation()
