class api_store:

    def key(self, service):
        keys = {
            "newsapi": "b5619995d112438c9d8136fa973b699d",
            "openWeather": "b64ecc91465d15cc0b58b805b3c01928"
        }

        service = keys[service]
        return service
