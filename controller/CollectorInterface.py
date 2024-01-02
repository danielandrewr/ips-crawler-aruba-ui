class CollectorInterface:
    def get_aruba_token(self):
        pass

    def get_ap_data(self, token, ap_name):
        pass

    def get_eirp_data(self, token, ap_name):
        pass

    def collect_and_store_data(self):
        pass