import read_config.config
import request_dnf_api.get_server
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def main():
    config = read_config.config.Config()
    print(config.job_info)
    print(config.server_info)


if __name__ == "__main__":
    main()
