from internal.config import config


def main():
    print(config.get_server_info())
    print(config.get_project_root_path())

if __name__ == '__main__':
    main()