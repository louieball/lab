class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):
        """
        Method that stores the TV channel, volume, and status.
        The __powerup attribute is used to dictate the power
        The __volume attribute is used to dictate volume
        The __channel attribute is used to dictate the channel
        """

        self.__powerup = False
        self.__volume = 0
        self.__channel = 0

        pass

    def power(self):
        """
        This Method turns the TV on and off.
        It uses the __powerup attribute to dictate whether it is on or off.
        """

        if self.__powerup == False:
            self.__powerup = True
        elif self.__powerup == True:
            self.__powerup = False

        pass

    def channel_up(self):
        """
        This Method adjusts the TV channel by incrementing its value, and should only work if the TV is on.
        If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        __powerup tells if it is on or not.
        __channel to increment the channel value.
        """
        if self.__powerup == True:
            if self.__channel < 3:
                self.__channel += 1
            elif self.__channel == 3:
                self.__channel = 0
        else:

            pass

    def channel_down(self):
        """
        This method should be used to adjust the TV channel by decrementing its value.
        It should only work for a TV that is on.
        If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        __powerup tells if it is on or not.
        __channel decrements the channel value.
        """
        if self.__powerup == True:
            if self.__channel > 0:
                self.__channel -= 1
            elif self.__channel == 0:
                self.__channel = 3

        else:
            pass

    def volume_up(self):
        """
        This method should be used to adjust the TV volume by incrementing its value.
        It should only work for a TV that is on.
        If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        __powerup tells if it is on or not.
        __volume increments the volume value.
        """
        if self.__powerup == True:
            if self.__volume < 2:
                self.__volume += 1


        else:
            pass

    def volume_down(self):
        """
        This method should be used to adjust the TV volume by decrementing its value.
        It should only work for a TV that is on.
        If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        __powerup tells if it is on or not.
        __volume decrements the volume value.
        """
        if self.__powerup == True:
            if self.__volume > 0:
                self.__volume -= 1


        else:
            pass

    def __str__(self) -> str:
        """
        This method should be used to return the TV status.
        :return: string containing status of __powerup, __channel, and __volume.
        """

        return 'TV status: Is on = {}, Channel = {}, Volume = {}'.format(self.__powerup, self.__channel, self.__volume)

        pass


