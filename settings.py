class Settings:
    use_images = True

    @staticmethod
    def toggle_use_images():
        Settings.use_images = not Settings.use_images