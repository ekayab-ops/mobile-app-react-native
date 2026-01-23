import os
import argparse
from typing import List

def get_environment() -> str:
    environment = os.environ.get('ENVIRONMENT')
    if environment:
        return environment
    return 'development'

def get_base_url() -> str:
    environment = get_environment()
    if environment == 'production':
        return 'https://example.com/api'
    return 'http://localhost:8080/api'

def get_api_endpoints() -> List[str]:
    base_url = get_base_url()
    return [
        f'{base_url}/users',
        f'{base_url}/products',
        f'{base_url}/orders',
    ]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mobile App React Native')
    parser.add_argument('--config', type=str, help='Path to configuration file')
    parser.add_argument('--mode', type=str, help='Mode to run in (production/development)')
    args = parser.parse_args()

    environment = args.mode
    if environment and environment not in ['production', 'development']:
        parser.error('Invalid mode. Please use either production or development.')

    if args.config:
        print(f'Running in mode: {environment}')
        print(f'Config file: {args.config}')
    else:
        environment = get_environment()
        print(f'Running in mode: {environment}')
        print(f'Config file: {os.getcwd()}/config.json')