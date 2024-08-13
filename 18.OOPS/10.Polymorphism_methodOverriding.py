class Iphone6:
    def home(self):
        print('Home button is clicked')

class IphoneX(Iphone6):
    def home(self):
        print('Home button is touched')    # add super to call parent class method.
        super().home()

i6 = Iphone6()
i6.home()

ix = IphoneX()
ix.home()   # to call parent class function we need to write super.
            # Home button is touched
            # Home button is clicked
