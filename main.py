from dotenv import load_dotenv
import os
import argparse
from controller.APDataCollector import APDataCollector
from controller.Database import Database


load_dotenv()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--t',
        '--time',
        help='crawler active duration (minutes)',
        dest='time',
        default=5,
        type=int
    )

    parser.add_argument(
        '--cn',
        '--collection_name',
        help="db collection name to store data into",
        dest='collection_name',
        default='raw_data',
        type=str
    )

    parser.add_argument(
        '--f',
        '--file',
        help='file name that contains list of AP names',
        dest='file',
        type=str
    )

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as file:
            ap_names = [line.strip() for line in file if line.strip()]
    else:  
        ap_names = ['FT-ICELL-LT3-LAB.KOM1-AP1', 'FT-ICELL-LT3-LAB.KOM2-AP2', 
                    'FT-ICELL-LT3-LAB.KOM3-AP3', 'FT-ICELL-LT3-LAB.PRINTING-AP5',
                    'FT-ICELL-LT3-LAB.PRINTING-AP6', 'FT-ICELL-LT3-LOBBY-AP4']

    aruba_username = os.getenv('ARUBA_USERNAME')
    aruba_password = os.getenv('ARUBA_PASSWORD')
    aruba_ipaddress = os.getenv('ARUBA_IPADDRESS')

    database = Database()

    duration = args.time
    collection_name = args.collection_name

    data_controller = APDataCollector(
        ap_names, aruba_username, aruba_password, aruba_ipaddress, duration, database, collection_name)
    data_controller.collect_and_store_data()
