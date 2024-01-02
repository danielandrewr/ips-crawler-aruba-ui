from CollectorInterface import CollectorInterface
from Database import DatabaseInterface

class SingleAPDataCollector(CollectorInterface):
    def __init__(self, 
                 ap_name: str,
                 aruba_username: str,
                 aruba_password: str,
                 aruba_ipaddress: str,
                 duration: int,
                 database: DatabaseInterface
                ):
        self.ap_name = ap_name
        self.ARUBA_USERNAME = aruba_username
        self.ARUBA_PASSWORD = aruba_password
        self.ARUBA_IPADDRESS = aruba_ipaddress
        self.duration = duration
        self.database = database
