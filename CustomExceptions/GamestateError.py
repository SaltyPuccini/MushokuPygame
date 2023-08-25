class UnknownGamestateError(Exception):
    """Exception raised when invalid gamestate appears.

    Attributes:
        gamestate -- current gamestate
        message -- explanation of the error
    """

    def __init__(self, gamestate):
        self.message = f"Current gamestate: \"${gamestate}\" is invalid."
        super().__init__(self.message)